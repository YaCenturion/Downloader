from pytube import Playlist

py = Playlist("https://www.youtube.com/playlist?list=PLk7JM19SQtzDBkM_hGPzNGT_5cCrK7F6O")

print(f'Downloading playlist: {py.title}')

for video in py.videos:

    try:
        # video.streams.filter(res='720p', file_extension='mp4').first().download()
        video.streams.filter(only_audio=True).first().download()
        print(f'Downloaded: {video.title}')
    except:
        print(f'!Video {video.title} is unavaialable, skipping.')

print("Done...")
