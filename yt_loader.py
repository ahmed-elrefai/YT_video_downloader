from pytube import YouTube

link = input("Enter the video link: ")
video = YouTube(link)
video = video.streams.get_highest_resolution()
video.download()
print("successful")