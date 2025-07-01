from pydub import AudioSegment

def merge_audios(audio_files, output_file="merged_output.mp3"):
    merged = AudioSegment.empty()
    for file in audio_files:
        audio = AudioSegment.from_file(file)
        print(file, len(audio), audio.duration_seconds)
        merged += audio
    merged.export(output_file, format="mp3")
    print(f"✅ Merged audio saved as: {output_file}")