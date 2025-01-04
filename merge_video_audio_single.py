import os
from moviepy.editor import VideoFileClip, AudioFileClip, concatenate_videoclips
# Merging downloaded video with create audio.
def merge_video_audio(video_path, audio_path, output_path):
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    # Load video and audio clips
    video_clip = VideoFileClip(video_path)
    audio_clip = AudioFileClip(audio_path)

    # Get durations of video and audio clips
    video_duration = video_clip.duration
    audio_duration = audio_clip.duration

    # Calculate how many times to repeat the video to match the audio length
    repeat_times = int(audio_duration / video_duration)

    # Repeat the video clip if necessary
    repeated_video_clips = [video_clip] * repeat_times
    remaining_duration = audio_duration % video_duration
    if remaining_duration > 0:
        repeated_video_clips.append(video_clip.subclip(0, remaining_duration))

    # Concatenate video clips
    final_video_clip = concatenate_videoclips(repeated_video_clips)

    # Set audio of the final video
    final_video_clip = final_video_clip.set_audio(audio_clip)

    # Write the final video to a file
    final_video_clip.write_videofile(output_path, codec='libx264', audio_codec='aac')
