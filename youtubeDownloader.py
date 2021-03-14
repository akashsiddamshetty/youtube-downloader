import pytube
from pytube import YouTube

link = input("enter the link : ")

yt = YouTube(link)

print("title: ",yt.title)
print("lenth of video: ",yt.length)

ys = yt.streams.get_highest_resolution()

print("Downloading...")
ys.download('/home/ktk/Downloads')
print("Download completed!!")
