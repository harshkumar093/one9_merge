from pydub import AudioSegment
import os

def merge_audios(audio_files, output_file="merged_output.mp3"):
    merged = AudioSegment.empty()

    for file in audio_files:
        if os.path.basename(file).startswith("silence_") and file.endswith("s"):
            try:
                # Extract duration from filename like "silence_3s" or "silence_5s"
                duration = int(file.split("_")[1].replace("s", "")) * 1000
                print(f"🔇 Inserting {duration // 1000}s silence from: {file}")
                merged += AudioSegment.silent(duration=duration)
            except Exception as e:
                print(f"❌ Failed to parse silence duration from {file}: {e}")
        else:
            try:
                audio = AudioSegment.from_file(file)
                if len(audio) == 0:
                    print(f"⚠️ Skipped 0-length audio: {file}")
                else:
                    print(f"🎧 Merging: {file} ({len(audio) / 1000:.2f}s)")
                    merged += audio
            except Exception as e:
                print(f"❌ Error processing {file}: {e}")

    merged.export(output_file, format="mp3")
    print(f"\n✅ Merged audio saved as: {output_file}")
