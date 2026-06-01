from faster_whisper import WhisperModel

print("Loading model...")

model = WhisperModel(
    "medium",
    compute_type="int8"
)

print("Transcribing...")

segments, info = model.transcribe(
    "media-2.mp3"
)

with open("transcript.txt", "w", encoding="utf-8") as f:
    for segment in segments:
        line = (
            f"[{segment.start:.1f} - "
            f"{segment.end:.1f}] "
            f"{segment.text}\n"
        )

        print(line)
        f.write(line)

print("Done!")
print("Transcript saved to transcript.txt")