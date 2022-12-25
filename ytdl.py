
import youtube_dl

print("Enter URL:")
url = input()

options = {
    "format": "best",  # choose the best quality video
    "outtmpl": "%(title)s.%(ext)s",  # specify the output filename
    "noplaylist": True,  # don't download a playlist, just the video
}

ydl = youtube_dl.YoutubeDL(options)

ydl.download([url])
