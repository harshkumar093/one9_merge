def merge_audios(audio_files, output_file="merged_output.mp3"):
    with open(output_file, "wb") as outfile:
        for fname in audio_files:
            with open(fname, "rb") as infile:
                outfile.write(infile.read())
    print(f"✅ Merged audio saved as: {output_file}")
