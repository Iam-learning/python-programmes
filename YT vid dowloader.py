#First install pytube by running "pip install pytube" in the console.
#Dowloaded vid will be saved where this py file is located.

from pytube import YouTube
link = input("Enter the link: ")
video = YouTube(link)
stream = video.streams.get_highest_resolution()
stream.download()