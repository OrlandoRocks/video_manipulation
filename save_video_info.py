import os
from moviepy.video.io.VideoFileClip import VideoFileClip
from datetime import datetime
from database import get_connection


def get_video_info(clip_path):
    try:
        video = VideoFileClip(clip_path)
        name = os.path.splitext(os.path.basename(clip_path))[0]
        extension = os.path.splitext(clip_path)[1]
        duration = video.duration
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        info_video = {
            "name": name,
            "extension": extension,
            "duration": duration,
            "path": clip_path,
            "timestamp": timestamp
        }

        return info_video
    except Exception as e:
        print(f"Error getting video info {clip_path}: {e}")
        return None


def get_video_clips(folder):
    info_videos = []
    try:
        for video_clip in os.listdir(folder):
            if video_clip.endswith(".mov") or video_clip.endswith(".mp4"):
                clip_path = os.path.join(folder, video_clip)
                info_video = get_video_info(clip_path)
                if info_video:
                    info_videos.append(info_video)
    except Exception as e:
        print(f"Error reading folder {folder}: {e}")

    return info_videos


if __name__ == "__main__":
    video_clips_folder = "video_clips"
    videos_info = get_video_clips(video_clips_folder)
    try:
        conn = get_connection()
        cursor = conn.cursor()
        query = "INSERT INTO video_data (clip_name, clip_file_extension, clip_duration, clip_location, insert_timestamp) VALUES (%s, %s, %s, %s, %s)"

        for video_info in videos_info:
            data = (
                video_info["name"],
                video_info["extension"],
                video_info["duration"],
                video_info["path"],
                video_info["timestamp"]
            )
            cursor.execute(query, data)
            conn.commit()

        cursor.close()
        conn.close()

        print("Video info was successfully added to video_clip table :D")
    except Exception as e:
        print("Error trying to add info to the video_clip table:", e)
