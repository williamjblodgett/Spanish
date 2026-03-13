"""
Spanish Voice Trainer - Main entry point.

Setup:
  1. pip install -r requirements.txt
  2. Linux: sudo apt-get install portaudio19-dev python3-dev libsdl2-dev
  3. cp .env.example .env  (then add your ANTHROPIC_API_KEY)
  4. python main.py
"""

import sys
import os

from dotenv import load_dotenv

import voice
import progress
import learning
import conversation as conv


BANNER = """
╔══════════════════════════════════════╗
║     SPANISH VOICE TRAINER           ║
║     Aprende espanol hablando        ║
╚══════════════════════════════════════╝
"""

MENU = """
  1.  Vocabulary Drill        (listen and repeat)
  2.  Translation Challenge   (English -> Spanish)
  3.  Free Conversation       (talk with Sofia)
  4.  View Progress
  5.  Exit

  Choose [1-5]: """


def print_banner() -> None:
    print(BANNER)


def get_menu_choice() -> str:
    while True:
        try:
            choice = input(MENU).strip()
            if choice in {"1", "2", "3", "4", "5"}:
                return choice
            print("  Please enter a number from 1 to 5.")
        except (KeyboardInterrupt, EOFError):
            return "5"


def check_api_key() -> bool:
    key = os.environ.get("ANTHROPIC_API_KEY", "")
    if not key or key == "your_key_here":
        print("\n  ERROR: ANTHROPIC_API_KEY is not configured.")
        print("  1. Copy .env.example to .env")
        print("  2. Edit .env and add your key: ANTHROPIC_API_KEY=sk-ant-...")
        print("  3. Get a key at: https://console.anthropic.com\n")
        return False
    return True


def main() -> None:
    # Load .env file
    load_dotenv()

    print_banner()

    # Validate API key before initializing audio
    if not check_api_key():
        sys.exit(1)

    # Initialize audio
    voice.init_audio()

    # Create Claude client
    try:
        client = conv.create_client()
    except EnvironmentError as e:
        print(f"\n  ERROR: {e}\n")
        voice.cleanup_audio()
        sys.exit(1)

    progress.increment_session_count()

    print("  Audio initialized. Ready to start!\n")
    print(f"  Vocabulary loaded: {len(learning.VOCABULARY)} phrases")
    print("  Say 'salir' or 'exit' at any time to stop a mode.\n")

    # Main menu loop
    while True:
        choice = get_menu_choice()

        if choice == "1":
            try:
                num = int(input("  How many words? [default 10]: ").strip() or "10")
                num = max(1, min(num, 50))
            except (ValueError, KeyboardInterrupt, EOFError):
                num = 10
            learning.run_vocabulary_drill(client, num_words=num)

        elif choice == "2":
            try:
                num = int(input("  How many phrases? [default 10]: ").strip() or "10")
                num = max(1, min(num, 50))
            except (ValueError, KeyboardInterrupt, EOFError):
                num = 10
            learning.run_translation_challenge(client, num_phrases=num)

        elif choice == "3":
            learning.run_free_conversation(client)

        elif choice == "4":
            progress.display_stats()

        elif choice == "5":
            break

    voice.cleanup_audio()
    print("\n  ¡Hasta luego! Keep practicing every day!\n")


if __name__ == "__main__":
    main()
