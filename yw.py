#YouTube Video Downloader 
#Code to download a single video from YouTube------------------------------------------------------------
from pytube import YouTube

link ="https://www.youtube.com/watch?v=vLqTf2b6GZw"
youtube_1= YouTube(link)

print("Title of the YouTube Video :")
print(youtube_1.title)
print("URL of the thumbnail of the YouTube Video :")
print(youtube_1.thumbnail_url)
videos = youtube_1.streams.all()
# videos = youtube_1.streams.filter(only_audio=True)    #it filter out only audio streams 
vid = list(enumerate(videos))
print("Currently available streams of the video")
for i in vid:
    print(i)

strm = int(input("Enter :  "))
videos[strm].download()
print("Successfully")


#Code to download a playlist from YouTube--------------------------------------------------------------
# from pytube import Playlist

# py=Playlist("https://www.youtube.com/playlist?list=PLu0W_9lII9agwh1XjRt242xIpHhPT2llg")
# print(f'Downloading : {py.title}')
# for video in py.videos:
#     video.streams.first().download()