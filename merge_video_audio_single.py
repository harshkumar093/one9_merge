import os
from moviepy.editor import VideoFileClip, AudioFileClip, concatenate_videoclips

def merge_video_audio(video_path, audio_path, output_path):
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    
    video_clip = VideoFileClip(video_path)
    audio_clip = AudioFileClip(audio_path)

    video_duration = video_clip.duration
    audio_duration = audio_clip.duration

    repeat_times = int(audio_duration / video_duration)

    repeated_video_clips = [video_clip] * repeat_times
    remaining_duration = audio_duration % video_duration
    if remaining_duration > 0:
        repeated_video_clips.append(video_clip.subclip(0, remaining_duration))

    final_video_clip = concatenate_videoclips(repeated_video_clips)

    final_video_clip = final_video_clip.set_audio(audio_clip)

    final_video_clip.write_videofile(output_path, codec='libx264', audio_codec='aac')
