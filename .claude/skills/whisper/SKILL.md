# Whisper - Speech-to-Text Transcription

Use this skill to transcribe audio files to text using OpenAI's Whisper model.

## When to invoke
- User runs `/whisper` with or without a file argument
- User asks to transcribe an audio file
- User asks to convert speech/audio to text

## Setup (first time)

Before transcribing, ensure Whisper is installed:

```bash
pip install openai-whisper
# Also requires ffmpeg:
# Ubuntu/Debian: sudo apt-get install ffmpeg
# macOS: brew install ffmpeg
```

## Usage

### Transcribe a file
```bash
whisper <audio_file> --model base
```

### Available models (trade-off: speed vs accuracy)
- `tiny`   — fastest, ~39M params
- `base`   — good balance (recommended for most uses)
- `small`  — more accurate
- `medium` — high accuracy
- `large`  — best accuracy, slowest

### Transcribe with specific language (faster than auto-detect)
```bash
whisper audio.mp3 --model base --language Spanish
```

### Translate non-English audio to English
```bash
whisper audio.mp3 --model base --task translate
```

### Output formats
```bash
whisper audio.mp3 --model base --output_format txt   # plain text
whisper audio.mp3 --model base --output_format srt   # subtitles
whisper audio.mp3 --model base --output_format json  # with timestamps
```

### Output to specific directory
```bash
whisper audio.mp3 --model base --output_dir ./transcripts
```

## Steps when user invokes /whisper

1. Check if the user provided a file path. If not, ask: "Which audio file would you like to transcribe?"
2. Verify the file exists using the Read or Bash tool.
3. Check if `openai-whisper` is installed (`pip show openai-whisper`). If not, install it.
4. Check if `ffmpeg` is available (`which ffmpeg`). Warn if missing.
5. Run the transcription using the Bash tool.
6. Display the transcribed text to the user.
7. Optionally save to a file if the user requests it.

## Supported audio formats
MP3, MP4, MPEG, MPGA, M4A, WAV, WEBM, OGG, FLAC

## Notes
- First run downloads the model weights (~140MB for `base`). Subsequent runs are fast.
- Models are cached in `~/.cache/whisper/`
- For Spanish learning: use `--language Spanish` for best accuracy on Spanish audio
