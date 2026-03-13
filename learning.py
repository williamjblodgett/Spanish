"""
Learning mode orchestration.
Coordinates voice I/O, content, progress tracking, and Claude API.
"""

import difflib
import unicodedata
import random

import voice
import progress
import conversation as conv
from content import VOCABULARY


EXIT_COMMANDS = {"salir", "exit", "quit", "terminar", "bye", "adios", "adiós", "stop", "para"}


def _normalize(text: str) -> str:
    """Lowercase, strip accents, remove punctuation."""
    # Strip accents
    nfkd = unicodedata.normalize("NFD", text.lower())
    ascii_text = "".join(c for c in nfkd if not unicodedata.combining(c))
    # Remove non-alphanumeric (keep spaces)
    return "".join(c for c in ascii_text if c.isalnum() or c.isspace()).strip()


def _is_match(user_said: str | None, expected: str, threshold: float = 0.70) -> bool:
    """
    Fuzzy match between user's speech and expected phrase.
    Returns True if the normalized ratio is >= threshold.
    Handles accent differences, missing punctuation, and minor STT errors.
    """
    if user_said is None:
        return False
    user_norm = _normalize(user_said)
    expected_norm = _normalize(expected)
    ratio = difflib.SequenceMatcher(None, user_norm, expected_norm).ratio()
    return ratio >= threshold


def _detect_exit_command(text: str | None) -> bool:
    """Return True if user said an exit command."""
    if text is None:
        return False
    words = _normalize(text).split()
    return any(w in EXIT_COMMANDS for w in words)


def _retry_listen(language: str = voice.STT_LANGUAGE) -> str | None:
    """Listen once more after a failed attempt, with a prompt."""
    voice.speak_english("I didn't hear you. Try again.")
    return voice.listen_for_speech(language=language)


# ---------------------------------------------------------------------------
# Mode 1: Vocabulary Drill
# ---------------------------------------------------------------------------

def run_vocabulary_drill(client, num_words: int = 10) -> None:
    """
    Pronunciation drill: app speaks Spanish, user repeats it back.
    Progress is recorded for spaced repetition.
    """
    print("\n--- VOCABULARY DRILL ---")
    print("Listen carefully, then repeat the Spanish phrase.\n")

    due_words = progress.get_due_words(VOCABULARY, limit=num_words)

    if not due_words:
        voice.speak_english("Amazing! You have no words due for review right now. Come back tomorrow!")
        return

    correct = 0
    total = 0

    for i, word in enumerate(due_words, 1):
        print(f"\n[{i}/{len(due_words)}]")
        print(f"  English:  {word['english']}")
        if word.get("notes"):
            print(f"  Note:     {word['notes']}")

        # Speak it once slow, then at normal speed
        voice.speak_spanish(word["spanish"], slow=True)
        voice.speak_spanish(word["spanish"], slow=False)
        voice.speak_english("Now you say it.")

        user_said = voice.listen_for_speech()

        if user_said is None:
            user_said = _retry_listen()

        if _detect_exit_command(user_said):
            voice.speak_english("Stopping drill. Good work!")
            break

        if _is_match(user_said, word["spanish"]):
            voice.speak_english("Great job!")
            progress.record_attempt(word["spanish"], success=True)
            correct += 1
        else:
            voice.speak_english("Not quite. Listen again.")
            voice.speak_spanish(word["spanish"], slow=True)
            voice.speak_english("One more try.")

            retry = voice.listen_for_speech()
            if _is_match(retry, word["spanish"]):
                voice.speak_english("Yes! Much better.")
                progress.record_attempt(word["spanish"], success=True)
                correct += 1
            else:
                voice.speak_spanish(word["spanish"])
                progress.record_attempt(word["spanish"], success=False)

        total += 1

    if total > 0:
        pct = int(correct / total * 100)
        summary = f"Drill complete. {correct} out of {total} correct. {pct} percent."
        voice.speak_english(summary)
        print(f"\n  Result: {correct}/{total} ({pct}%)")


# ---------------------------------------------------------------------------
# Mode 2: Translation Challenge
# ---------------------------------------------------------------------------

def run_translation_challenge(client, num_phrases: int = 10) -> None:
    """
    Translation drill: app speaks English, user responds in Spanish.
    Claude judges ambiguous answers.
    """
    print("\n--- TRANSLATION CHALLENGE ---")
    print("Listen to the English phrase, then say it in Spanish.\n")

    due_words = progress.get_due_words(VOCABULARY, limit=num_phrases)

    if not due_words:
        voice.speak_english("No phrases due for review. Great work keeping up!")
        return

    correct = 0
    total = 0

    for i, phrase in enumerate(due_words, 1):
        print(f"\n[{i}/{len(due_words)}]")
        print(f"  English:  {phrase['english']}")

        voice.speak_english(f"Say this in Spanish: {phrase['english']}")

        user_said = voice.listen_for_speech(language=voice.STT_LANGUAGE)

        if user_said is None:
            user_said = _retry_listen(language=voice.STT_LANGUAGE)

        if _detect_exit_command(user_said):
            voice.speak_english("Stopping challenge. Good work!")
            break

        ratio = 0.0
        if user_said:
            user_norm = _normalize(user_said)
            expected_norm = _normalize(phrase["spanish"])
            ratio = difflib.SequenceMatcher(None, user_norm, expected_norm).ratio()

        if ratio >= 0.70:
            # Clear match
            voice.speak_english("Correct!")
            voice.speak_spanish(f"¡Correcto! {phrase['spanish']}")
            progress.record_attempt(phrase["spanish"], success=True)
            correct += 1

        elif ratio >= 0.45 and user_said:
            # Ambiguous — ask Claude
            feedback = conv.get_translation_feedback(
                client,
                english_phrase=phrase["english"],
                user_spanish=user_said,
                expected_spanish=phrase["spanish"],
            )
            print(f"  Feedback: {feedback}")
            voice.speak_spanish(feedback)

            # Count as success if Claude gave thumbs up (heuristic)
            if "correcto" in feedback.lower() or "muy bien" in feedback.lower() or "exacto" in feedback.lower():
                progress.record_attempt(phrase["spanish"], success=True)
                correct += 1
            else:
                progress.record_attempt(phrase["spanish"], success=False)

        else:
            # Wrong or no answer
            voice.speak_english(f"The answer is:")
            voice.speak_spanish(phrase["spanish"])
            print(f"  Correct:  {phrase['spanish']}")
            progress.record_attempt(phrase["spanish"], success=False)

        total += 1

    if total > 0:
        pct = int(correct / total * 100)
        summary = f"Challenge complete. {correct} out of {total} correct. {pct} percent."
        voice.speak_english(summary)
        print(f"\n  Result: {correct}/{total} ({pct}%)")


# ---------------------------------------------------------------------------
# Mode 3: Free Conversation
# ---------------------------------------------------------------------------

def run_free_conversation(client) -> None:
    """
    Open-ended conversation with Sofía (Claude).
    User speaks in Spanish, Sofía responds in Spanish.
    Say 'salir', 'exit', or 'quit' to end.
    """
    print("\n--- FREE CONVERSATION WITH SOFÍA ---")
    print("Speak Spanish with your AI conversation partner.")
    print("Say 'salir' or 'exit' to end the session.\n")

    conversation_history = []

    greeting = "¡Hola! Soy Sofía, tu compañera de conversación. ¿De qué quieres hablar hoy?"
    voice.speak_spanish(greeting)
    conversation_history.append({"role": "assistant", "content": greeting})

    turn = 0
    while True:
        turn += 1
        user_said = voice.listen_for_speech(language=voice.STT_LANGUAGE, timeout=8)

        if user_said is None:
            user_said = _retry_listen(language=voice.STT_LANGUAGE)

        if user_said is None:
            voice.speak_spanish("¿Sigues ahí? No te escucho.")
            continue

        if _detect_exit_command(user_said):
            break

        # Get Sofía's response
        response = conv.get_conversation_response(client, conversation_history, user_said)
        voice.speak_spanish(response)

        # After ~15 turns, gently remind the user they can exit
        if turn == 15:
            print("\n  [Tip: Say 'salir' or 'exit' to end the conversation]")

    # Session summary
    print("\n  [Getting session summary...]")
    summary = conv.get_session_summary(client, conversation_history)
    voice.speak_spanish(summary)
    print(f"\n  {summary}\n")
