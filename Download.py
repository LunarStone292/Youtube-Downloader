try:
    import pytube, os
    from pytube import Playlist
    os.system("cls||clear")
except:
    print(" Pytube not found, first install requirements.txt")
    exit()

print('''\u001b[31m
██████╗ ██╗   ██╗████████╗██╗   ██╗██████╗ ███████╗
██╔══██╗╚██╗ ██╔╝╚══██╔══╝██║   ██║██╔══██╗██╔════╝
██████╔╝ ╚████╔╝    ██║   ██║   ██║██████╔╝█████╗  
██╔═══╝   ╚██╔╝     ██║   ██║   ██║██╔══██╗██╔══╝  
██║        ██║      ██║   ╚██████╔╝██████╔╝███████╗
╚═╝        ╚═╝      ╚═╝    ╚═════╝ ╚═════╝ ╚══════╝
                                                   
''')

print("\u001b[34m 1. Download a video")
print(" 2. Download a playlist")

scelta = int(input("\n PyTube => "))

if(scelta == 1):
    url = input(" Enter the Youtube url: ")
    try:
        yt = pytube.YouTube(url)
    except:
        print(" Error")
        exit()
    print("\n")
    print('\u001b[33m Title:', yt.title)
    print(' Author:', yt.author)
    print(' Published date:', yt.publish_date.strftime("%Y-%m-%d"))
    print(' Number of views:', yt.views)
    print(' Length of video:', yt.length, 'seconds')
    print("\n Downloading the Video...")
    try:
        yt.streams.get_highest_resolution().download()
        print("\n Done.")
    except:
        print("\u001b[37m Error")
        exit()
    
elif(scelta == 2):
    urlP = input("\n Enter the Youtube Playlist url: ")
    p = Playlist(f'{urlP}')
    print(f'\n Downloading: {p.title}')
    print('\n Number of videos in playlist: %s' % len(p.video_urls))
    for video in p.videos:
        audioStream = video.streams.get_by_itag('140')
        audioStream.download('Playlists_Downloads')