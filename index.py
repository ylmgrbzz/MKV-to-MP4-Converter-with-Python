import os
from moviepy.editor import VideoFileClip


def convert_and_download_videos(input_folder, output_folder):
    for filename in os.listdir(input_folder):
        if filename.endswith(".mkv"):
            input_file = os.path.join(input_folder, filename)
            output_file = os.path.join(
                output_folder, os.path.splitext(filename)[0] + ".mp4"
            )

            try:
                video = VideoFileClip(input_file)
                video.write_videofile(output_file, codec="libx264")
                print(f"{input_file} dönüştürüldü ve indirildi.")
            except Exception as e:
                print(f"{input_file} dönüştürülürken hata oluştu:", str(e))


input_folder = "/C:/Users/yalim/Videos/ylm.mkv"
output_folder = "/C:/Users/yalim/Videos"

convert_and_download_videos(input_folder, output_folder)
