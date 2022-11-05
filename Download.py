RED = '\x1B[31m'

x = 0
try:
    import pytube, os, time, random, platform
    from pytube import Playlist
    os.system("cls||clear")
except:
    print(RED + " Pytube not found, first install requirements.txt")
    exit()

if(platform.system() == "Windows"):
    print(RED + '''
    ██████╗ ██╗   ██╗████████╗██╗   ██╗██████╗ ███████╗
    ██╔══██╗╚██╗ ██╔╝╚══██╔══╝██║   ██║██╔══██╗██╔════╝
    ██████╔╝ ╚████╔╝    ██║   ██║   ██║██████╔╝█████╗  
    ██╔═══╝   ╚██╔╝     ██║   ██║   ██║██╔══██╗██╔══╝  
    ██║        ██║      ██║   ╚██████╔╝██████╔╝███████╗
    ╚═╝        ╚═╝      ╚═╝    ╚═════╝ ╚═════╝ ╚══════╝
          ╔════════════════════════════════════╗
          ║ opzioni                            ║
          ╠════════════════════════════════════╣
          ║ 1) Download a video                ║
          ║ 2) Download the audio              ║
          ║ 3) Download a playlist             ║
          ╚════════════════════════════════════╝
    ''')

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
        print("\n Downloading the Audio...")
        try:
            t=yt.streams.filter(only_audio=True).all()
            t[0].download()
            out_file = yt.title + ".mp4"
            base, ext = os.path.splitext(out_file)
            new_file = base + '.mp3'
            os.rename(out_file, new_file)
            print("\n Done")
        except:
            print("\u001b[37m Error")
            exit()

    elif(scelta == 3):
        urlP = input("\n Enter the Youtube Playlist url: ")
        p = Playlist(f'{urlP}')
        print(f'\n Downloading: {p.title}')
        print('\n Number of videos in playlist: %s' % len(p.video_urls))
        for video in p.videos:
            audioStream = video.streams.get_by_itag('140')
            audioStream.download('Playlists_Downloads')

else:
    os.system('''./colorize_ascii -t "PyTube"''')
    print('''
╔════════════════════════════════════╗
║ opzioni                            ║
╠════════════════════════════════════╣
║ 1) Download a video                ║
║ 2) Download the audio              ║
║ 3) Download a playlist             ║
╚════════════════════════════════════╝
''')
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
