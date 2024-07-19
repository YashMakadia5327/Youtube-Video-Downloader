import os
import yt_dlp
import tkinter as tk
from tkinter import filedialog
from pytube import YouTube


def video_download(url, save_path):
    try:
        yt = YouTube(url)
        stream = yt.streams.filter(progressive=True, file_extension='mp4')
        highest_resolution_stream = stream.get_highest_resolution("mp4")
        highest_resolution_stream.download(output_path=save_path)
        print("Download video successfully.")

    except Exception as error:
        print(error)
        print("Error")


def open_file_dialog():
    folder = filedialog.askdirectory()
    if folder:
        print(f"Select Folder : {folder}")

    return folder


if __name__ == "__main__":
    root = tk.Tk()
    root.withdraw()

    video_url = input("Please Enter the youtube url : ")
    save_dir = open_file_dialog()

    # if not os.path.exists(save_dir):
    #     os.makedirs(save_dir)

    ydl_opts = {'outtmpl': os.path.join(save_dir, '%(title)s.%(ext)s')}
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([video_url])

