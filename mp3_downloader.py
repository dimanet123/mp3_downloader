from pytube import YouTube
import os


file1 = open("list.txt", "r")
folder = "audio\\"

while True:
    try:
        list  = file1.readline()
        if not list:
            break
        video = YouTube(list)
        stream = video.streams.filter(only_audio=True).first()
        char_remov = [":","\\","/","*","?","\"","<",">","|"]
        filename=f"{video.title}.mp3"
        for char in char_remov:
            filename = filename.replace(char,'')
        if (os.path.exists(folder + filename)) == False:
            stream.download(filename = folder + filename)
            print("The video is downloaded in MP3")
        else:
            print("File exists")
    except KeyError:
        print("Unable to fetch video information. Please check the video URL or your network connection.")