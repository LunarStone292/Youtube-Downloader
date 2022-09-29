try:
    import pytube, os
    os.system("cls||clear")
except:
    print(" Pytube not found, first install requirements.txt")
    exit()

print('''
██████╗ ██╗   ██╗████████╗██╗   ██╗██████╗ ███████╗
██╔══██╗╚██╗ ██╔╝╚══██╔══╝██║   ██║██╔══██╗██╔════╝
██████╔╝ ╚████╔╝    ██║   ██║   ██║██████╔╝█████╗  
██╔═══╝   ╚██╔╝     ██║   ██║   ██║██╔══██╗██╔══╝  
██║        ██║      ██║   ╚██████╔╝██████╔╝███████╗
╚═╝        ╚═╝      ╚═╝    ╚═════╝ ╚═════╝ ╚══════╝
                                                   
''')

url = input(" Enter the Youtube url: ")

try:
    yt = pytube.YouTube(url)
except:
    print(" Error")
    exit()

print('\n Title:', yt.title)
print(' Author:', yt.author)
print(' Published date:', yt.publish_date.strftime("%Y-%m-%d"))
print(' Number of views:', yt.views)
print(' Length of video:', yt.length, 'seconds')

print("\n Downloading the Video...")

try:
    yt.streams.get_highest_resolution().download()
    print("\n Done.")
except:
    print(" Error")
    exit()