import os
from moviepy.video.io.VideoFileClip import VideoFileClip


def cut_video(video_path):
    try:
        output_folder = "video_clips"
        clip_duration = 60
        # create the folder if it doesn't exist
        if not os.path.exists(output_folder):
            os.makedirs(output_folder)

        # load original video
        video = VideoFileClip(video_path)
        total_duration = video.duration

        # Cut it up into 1-minute clips
        start_frame = 0
        clip_frame = 0
        while start_frame < total_duration:
            end_frame = min(start_frame + clip_duration, total_duration)
            clip = video.subclip(start_frame, end_frame)
            clip_name = f"{clip_frame}thFrame.mp4"
            clip_path = os.path.join(output_folder, clip_name)
            clip.write_videofile(clip_path, codec="libx264")

            start_frame += clip_duration
            clip_frame += int(clip.fps * clip.duration)

        video.close()
    except Exception as e:
        print(f"Error trying to cut the video: {e}")


if __name__ == "__main__":
    path_video = "airshow.mp4"
    cut_video(path_video)
