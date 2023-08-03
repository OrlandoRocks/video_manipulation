import csv
import os
from database import get_connection


def get_video_clips_info():
    conn = get_connection()
    video_query = "SELECT * FROM video_data"
    try:
        cursor = conn.cursor()
        cursor.execute(video_query)
        data_video = cursor.fetchall()
        cursor.close()
        conn.close()

        return data_video
    except Exception as e:
        print("Error getting the data from video_data:", e)


def create_video_csv(data):
    try:
        if not os.path.exists('report'):
            os.makedirs('report')

        csv_file = "report/generated_video_files.csv"

        headers = ["clip_name", "clip_file_extension", "clip_duration", "clip_location", "insert_timestamp"]

        with open(csv_file, mode="w", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(headers)
            writer.writerows(video_data)

        print("Video CSV file was created successfully!")

    except Exception as e:
        print("Error creating the video csv file:", e)


if __name__ == "__main__":
    video_data = get_video_clips_info()
    create_video_csv(video_data)
