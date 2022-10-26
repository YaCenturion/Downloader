from pytube import Playlist

py = Playlist("https://www.youtube.com/playlist?list=PLg5SS_4L6LYs5IZZSY0viHRQFPa2P-R8H")

print(f'Downloading playlist: {py.title}')

for video in py.videos:

    try:
        # For video
        # video.streams.filter(res='720p', file_extension='mp4').first().download()

        # For just audio
        video.streams.filter(only_audio=True).first().download()
        print(f'Downloaded: {video.title}')
    except:
        print(f'!Video {video.title} is unavaialable, skipping.')

print("Done...")
