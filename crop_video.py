from moviepy.editor import VideoFileClip

def split_video_by_frames(input_video_path, output_video_path, start_frame, end_frame):
    """
    Split a video by frames.
    :param input_video_path: Path to the input video
    :param output_video_path: Path for the output video
    :param start_frame: The starting frame number
    :param end_frame: The ending frame number
    """
    # Load the video file
    clip = VideoFileClip(input_video_path)

    # Calculate start and end times in seconds
    start_time = start_frame / clip.fps
    end_time = end_frame / clip.fps

    # Cut the video according to the frame numbers
    new_clip = clip.subclip(start_time, end_time)

    # Save the new video
    new_clip.write_videofile(output_video_path, codec='libx264', audio_codec='aac')

def split_video_by_time(input_video_path, output_video_path, start_time, end_time):
    """
    Split a video by time.
    :param input_video_path: Path to the input video
    :param output_video_path: Path for the output video
    :param start_time: The start time in seconds
    :param end_time: The end time in seconds
    """
    # Load the video file
    clip = VideoFileClip(input_video_path)

    # Cut the video according to the time
    new_clip = clip.subclip(start_time, end_time)

    # Save the new video
    new_clip.write_videofile(output_video_path, codec='libx264', audio_codec='aac')

# Example usage
input_video_path = 'Path_to_video'  # Replace with your video path
output_video_path = 'Path_to_save_cropped_video'  # Replace with your desired output path

# Choose a format (frame or time) to perform video segmentation

# Split by frames
start_frame = 4650
end_frame = 5550
split_video_by_frames(input_video_path, output_video_path, start_frame, end_frame)

# Split by time
start_time = 150  # in seconds
end_time = 200  # in seconds
split_video_by_time(input_video_path, output_video_path, start_time, end_time)

