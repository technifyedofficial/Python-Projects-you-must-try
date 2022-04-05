from pytube import YouTube
URL = "Enter video URL"
video = YouTube(URL)
video_streams = video.streams.filter(file_extension='mp4').get_by_itag(18)
video_streams.download(output_path = "video_path")