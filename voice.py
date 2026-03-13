"""
Text-to-speech and speech-to-text layer.
All audio I/O lives here; other modules import these functions.

Requirements:
  pip install gTTS pygame SpeechRecognition PyAudio
  Linux: sudo apt-get install portaudio19-dev python3-dev libsdl2-dev
"""

import os
import tempfile

# Lazy imports so the app can still start even if a package is missing
_pygame = None
_gtts = None
_sr = None

# STT language code. "es-MX" (Mexican Spanish) is more neutral for Americas.
# Change to "es-ES" for Spain Spanish.
STT_LANGUAGE = "es-MX"


def _get_pygame():
    global _pygame
    if _pygame is None:
        import pygame
        _pygame = pygame
    return _pygame


def _get_gtts():
    global _gtts
    if _gtts is None:
        from gtts import gTTS
        _gtts = gTTS
    return _gtts


def _get_sr():
    global _sr
    if _sr is None:
        import speech_recognition as sr
        _sr = sr
    return _sr


def init_audio() -> None:
    """Initialize pygame mixer for audio playback. Call once at startup."""
    try:
        pygame = _get_pygame()
        pygame.init()
        pygame.mixer.init()
    except Exception as e:
        print(f"[audio] Warning: Could not initialize audio: {e}")
        print("[audio] Install: pip install pygame")
        print("[audio] Linux: sudo apt-get install libsdl2-dev")


def cleanup_audio() -> None:
    """Cleanup pygame on exit."""
    try:
        pygame = _get_pygame()
        pygame.quit()
    except Exception:
        pass


def _speak(text: str, lang: str, slow: bool = False) -> None:
    """Internal: synthesize text and play audio via pygame."""
    try:
        gTTS = _get_gtts()
        pygame = _get_pygame()

        tts = gTTS(text=text, lang=lang, slow=slow)

        # Write to a temp file
        tmp = tempfile.NamedTemporaryFile(suffix=".mp3", delete=False)
        tmp_path = tmp.name
        tmp.close()
        tts.save(tmp_path)

        # Play via pygame mixer
        pygame.mixer.music.load(tmp_path)
        pygame.mixer.music.play()
        clock = pygame.time.Clock()
        while pygame.mixer.music.get_busy():
            clock.tick(10)

        # Release file before deleting (needed on Windows, harmless on Linux)
        pygame.mixer.music.unload()
        os.unlink(tmp_path)

    except Exception as e:
        print(f"[TTS] Error speaking '{text[:40]}': {e}")
        print("[TTS] Make sure gTTS is installed: pip install gTTS")
        print("[TTS] Note: gTTS requires an internet connection.")


def speak_spanish(text: str, slow: bool = False) -> None:
    """Speak text in Spanish. Use slow=True for pronunciation drills."""
    print(f"  [Sofia]: {text}")
    _speak(text, lang="es", slow=slow)


def speak_english(text: str) -> None:
    """Speak text in English (for instructions and prompts)."""
    print(f"  [App]:   {text}")
    _speak(text, lang="en", slow=False)


def listen_for_speech(language: str = STT_LANGUAGE, timeout: int = 5, phrase_time_limit: int = 10) -> str | None:
    """
    Listen for speech and return recognized text, or None on failure.

    Args:
        language: BCP-47 language code (e.g. "es-MX", "en-US")
        timeout: Seconds to wait for speech to start
        phrase_time_limit: Max seconds to record after speech starts

    Returns:
        Recognized text string, or None if recognition failed
    """
    sr = _get_sr()
    recognizer = sr.Recognizer()
    recognizer.energy_threshold = 300
    recognizer.pause_threshold = 0.8

    try:
        with sr.Microphone() as source:
            print("  [Listening...]", end="", flush=True)
            recognizer.adjust_for_ambient_noise(source, duration=0.5)
            audio = recognizer.listen(source, timeout=timeout, phrase_time_limit=phrase_time_limit)

        print(" done.")
        text = recognizer.recognize_google(audio, language=language)
        print(f"  [You]:   {text}")
        return text

    except sr.WaitTimeoutError:
        print("\n  [Timeout] No speech detected.")
        return None
    except sr.UnknownValueError:
        print("\n  [STT] Could not understand the audio.")
        return None
    except sr.RequestError as e:
        print(f"\n  [STT] Network error: {e}")
        print("  [STT] Speech recognition requires an internet connection.")
        return None
    except OSError as e:
        print(f"\n  [Mic] Microphone error: {e}")
        print("  [Mic] Linux fix: sudo apt-get install portaudio19-dev python3-dev")
        print("  [Mic] Then: pip install PyAudio")
        return None
    except Exception as e:
        print(f"\n  [STT] Unexpected error: {e}")
        return None


def listen_for_english(timeout: int = 5) -> str | None:
    """Listen for English speech."""
    return listen_for_speech(language="en-US", timeout=timeout)
