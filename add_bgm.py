from pydub import AudioSegment
import imageio_ffmpeg

# Optional: Set ffmpeg path if needed
AudioSegment.converter = imageio_ffmpeg.get_ffmpeg_exe()

def add_bgm(primary_path, bg_music_path, output_path, bg_volume_reduction_db=20):
    # Load the primary audio and background music
    primary = AudioSegment.from_file(primary_path)
    background = AudioSegment.from_file(bg_music_path)

    # Reduce background music volume (e.g., -20 dB)
    background = background - bg_volume_reduction_db

    # Loop background music if it's shorter than primary
    if len(background) < len(primary):
        times = int(len(primary) / len(background)) + 1
        background = background * times

    # Trim to match primary length
    background = background[:len(primary)]

    # Overlay the background music on the primary audio
    combined = primary.overlay(background)

    # Export the final audio
    combined.export(output_path, format="mp3")
    print(f"Saved mixed audio at: {output_path}")
