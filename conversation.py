"""
Claude API integration for AI conversation partner and translation feedback.
"""

import os
from anthropic import Anthropic
from content import SYSTEM_PROMPT_CONVERSATION

MODEL = "claude-sonnet-4-6"
MAX_TOKENS = 300
MAX_HISTORY_TURNS = 10  # Keep last N turns to control token usage


def create_client() -> Anthropic:
    """Create and return an Anthropic client. Requires ANTHROPIC_API_KEY in environment."""
    api_key = os.environ.get("ANTHROPIC_API_KEY")
    if not api_key:
        raise EnvironmentError(
            "ANTHROPIC_API_KEY is not set.\n"
            "1. Copy .env.example to .env\n"
            "2. Add your API key: ANTHROPIC_API_KEY=sk-ant-...\n"
            "3. Get a key at https://console.anthropic.com"
        )
    return Anthropic(api_key=api_key)


def get_conversation_response(
    client: Anthropic,
    conversation_history: list,
    user_message: str,
) -> str:
    """
    Send a user message to Sofía and get a response.

    Maintains conversation_history in place (caller passes the same list each turn).
    Automatically trims history to MAX_HISTORY_TURNS * 2 messages.

    Returns the assistant's response text.
    """
    conversation_history.append({"role": "user", "content": user_message})

    # Trim history to avoid token overflow
    if len(conversation_history) > MAX_HISTORY_TURNS * 2:
        conversation_history[:] = conversation_history[-(MAX_HISTORY_TURNS * 2):]

    try:
        response = client.messages.create(
            model=MODEL,
            max_tokens=MAX_TOKENS,
            system=SYSTEM_PROMPT_CONVERSATION,
            messages=conversation_history,
        )
        assistant_text = response.content[0].text
        conversation_history.append({"role": "assistant", "content": assistant_text})
        return assistant_text

    except Exception as e:
        error_msg = f"Lo siento, hay un problema técnico. ({e})"
        conversation_history.append({"role": "assistant", "content": error_msg})
        return error_msg


def get_translation_feedback(
    client: Anthropic,
    english_phrase: str,
    user_spanish: str,
    expected_spanish: str,
) -> str:
    """
    Ask Claude to judge whether the user's Spanish translation is correct/close enough.

    Used for ambiguous answers in Translation Challenge mode.
    Returns 1-2 sentence feedback in Spanish.
    """
    prompt = (
        f"The user was asked to translate this English phrase into Spanish:\n"
        f"English: \"{english_phrase}\"\n"
        f"Expected answer: \"{expected_spanish}\"\n"
        f"The user said: \"{user_spanish}\"\n\n"
        f"Was the user's answer correct or close enough to be accepted as a valid translation? "
        f"If yes, say '¡Correcto!' and give brief encouragement. "
        f"If no, gently provide the correct answer. "
        f"Respond in Spanish only. Keep it to 1-2 sentences."
    )

    try:
        response = client.messages.create(
            model=MODEL,
            max_tokens=150,
            messages=[{"role": "user", "content": prompt}],
        )
        return response.content[0].text

    except Exception as e:
        return f"(No se pudo obtener retroalimentación: {e})"


def get_session_summary(client: Anthropic, conversation_history: list) -> str:
    """
    Ask Claude for a brief encouraging summary of the conversation session.
    Called at the end of free conversation mode.
    """
    if len(conversation_history) < 2:
        return "¡Buen trabajo empezando a practicar! Vuelve pronto."

    prompt = (
        "The Spanish practice conversation session just ended. "
        "Give the learner a short (2-3 sentence) encouraging summary in Spanish: "
        "what topics they covered, one thing they did well, and one encouragement to keep practicing. "
        "Be warm and enthusiastic."
    )

    try:
        response = client.messages.create(
            model=MODEL,
            max_tokens=150,
            system=SYSTEM_PROMPT_CONVERSATION,
            messages=conversation_history + [{"role": "user", "content": prompt}],
        )
        return response.content[0].text

    except Exception:
        return "¡Excelente práctica hoy! Sigue así y pronto hablarás como nativo. ¡Hasta la próxima!"
