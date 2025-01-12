from moviepy.editor import VideoFileClip

def convert_to_portrait(video_path, output_path):
    """
    Convert any aspect ratio video to 9:16 portrait ratio by cropping.
    
    Args:
        video_path (str): Path to the input video file.
        output_path (str): Path to save the cropped output video.
    """
    # Load the video
    clip = VideoFileClip(video_path)

    # Get video dimensions and aspect ratio
    video_width, video_height = clip.size
    aspect_ratio = video_width / video_height

    # Target aspect ratio
    target_ratio = 9 / 16

    if aspect_ratio > target_ratio:
        # Video is wider than 9:16, crop the width
        new_width = int(video_height * target_ratio)
        crop_x1 = (video_width - new_width) // 2
        crop_x2 = crop_x1 + new_width
        cropped_clip = clip.crop(x1=crop_x1, x2=crop_x2, y1=0, y2=video_height)
    else:
        # Video is taller than 9:16, crop the height
        new_height = int(video_width / target_ratio)
        crop_y1 = (video_height - new_height) // 2
        crop_y2 = crop_y1 + new_height
        cropped_clip = clip.crop(x1=0, x2=video_width, y1=crop_y1, y2=crop_y2)

    # Resize the cropped clip to 9:16 resolution while keeping original pixel quality
    portrait_clip = cropped_clip.resize(height=1080)  # Set height to 1080 pixels for 9:16 videos
    portrait_clip = portrait_clip.set_fps(clip.fps)  # Match the original FPS

    # Write the output file
    portrait_clip.write_videofile(output_path, codec="libx264", audio_codec="aac")

    # Close the clip
    clip.close()
    portrait_clip.close()