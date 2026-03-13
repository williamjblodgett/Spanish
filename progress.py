"""
Progress tracking with spaced repetition.
Persists data to progress.json alongside this script.
"""

import json
import os
from datetime import datetime, timedelta

PROGRESS_FILE = os.path.join(os.path.dirname(os.path.abspath(__file__)), "progress.json")
MAX_INTERVAL_DAYS = 30
DATE_FORMAT = "%Y-%m-%dT%H:%M:%S"


def _empty_progress() -> dict:
    return {
        "words": {},
        "session_stats": {
            "total_sessions": 0,
            "total_practice_time_seconds": 0,
        },
    }


def load_progress() -> dict:
    if not os.path.exists(PROGRESS_FILE):
        return _empty_progress()
    try:
        with open(PROGRESS_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    except (json.JSONDecodeError, IOError):
        return _empty_progress()


def save_progress(data: dict) -> None:
    with open(PROGRESS_FILE, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)


def record_attempt(spanish: str, success: bool) -> None:
    data = load_progress()
    words = data["words"]
    now = datetime.now()

    if spanish not in words:
        words[spanish] = {
            "attempts": 0,
            "successes": 0,
            "last_seen": None,
            "interval_days": 1,
            "next_review": now.strftime(DATE_FORMAT),
        }

    entry = words[spanish]
    entry["attempts"] += 1
    if success:
        entry["successes"] += 1

    # Spaced repetition: success doubles interval (capped), failure resets to 1
    if success:
        entry["interval_days"] = min(entry["interval_days"] * 2, MAX_INTERVAL_DAYS)
    else:
        entry["interval_days"] = 1

    entry["last_seen"] = now.strftime(DATE_FORMAT)
    entry["next_review"] = (now + timedelta(days=entry["interval_days"])).strftime(DATE_FORMAT)

    save_progress(data)


def get_due_words(vocabulary: list, limit: int = 20) -> list:
    """Return words due for review, new words first then most overdue."""
    data = load_progress()
    words_data = data["words"]
    now = datetime.now()

    new_words = []
    due_words = []

    for item in vocabulary:
        spanish = item["spanish"]
        if spanish not in words_data:
            new_words.append(item)
        else:
            next_review_str = words_data[spanish].get("next_review")
            if next_review_str:
                next_review = datetime.strptime(next_review_str, DATE_FORMAT)
                if next_review <= now:
                    due_words.append((next_review, item))

    # Sort due words: most overdue first
    due_words.sort(key=lambda x: x[0])
    sorted_due = [item for _, item in due_words]

    combined = new_words + sorted_due
    return combined[:limit]


def get_success_rate(spanish: str) -> float:
    data = load_progress()
    entry = data["words"].get(spanish)
    if not entry or entry["attempts"] == 0:
        return 0.0
    return entry["successes"] / entry["attempts"]


def get_stats_summary() -> dict:
    data = load_progress()
    words = data["words"]

    if not words:
        return {
            "total_words_practiced": 0,
            "average_success_rate": 0.0,
            "total_attempts": 0,
        }

    total_attempts = sum(w["attempts"] for w in words.values())
    total_successes = sum(w["successes"] for w in words.values())
    avg_rate = total_successes / total_attempts if total_attempts > 0 else 0.0

    return {
        "total_words_practiced": len(words),
        "average_success_rate": avg_rate,
        "total_attempts": total_attempts,
    }


def display_stats() -> None:
    data = load_progress()
    words = data["words"]

    print("\n" + "=" * 56)
    print("  PROGRESS REPORT")
    print("=" * 56)

    if not words:
        print("  No practice sessions recorded yet.")
        print("  Start with Vocabulary Drill or Translation Challenge!")
        print("=" * 56)
        return

    summary = get_stats_summary()
    print(f"  Words practiced:    {summary['total_words_practiced']}")
    print(f"  Total attempts:     {summary['total_attempts']}")
    print(f"  Average success:    {summary['average_success_rate']:.0%}")
    print()

    # Show hardest words (lowest success rate, at least 2 attempts)
    practiced = [
        (spanish, entry)
        for spanish, entry in words.items()
        if entry["attempts"] >= 2
    ]
    practiced.sort(key=lambda x: x[1]["successes"] / x[1]["attempts"])

    if practiced:
        print("  HARDEST WORDS (practice these most):")
        print(f"  {'Spanish':<30} {'Success':>8}  {'Tries':>5}")
        print("  " + "-" * 46)
        for spanish, entry in practiced[:10]:
            rate = entry["successes"] / entry["attempts"]
            display = spanish[:28] + ".." if len(spanish) > 30 else spanish
            print(f"  {display:<30} {rate:>7.0%}  {entry['attempts']:>5}")

    # Show words due for review
    now = datetime.now()
    due_count = sum(
        1 for entry in words.values()
        if entry.get("next_review") and
        datetime.strptime(entry["next_review"], DATE_FORMAT) <= now
    )
    new_count = 0  # Would need vocab to compute, skip here

    print()
    print(f"  Words due for review: {due_count}")
    print("=" * 56 + "\n")


def increment_session_count() -> None:
    data = load_progress()
    data["session_stats"]["total_sessions"] += 1
    save_progress(data)
