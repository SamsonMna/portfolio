# Lets download something on the internet
import internetdownloadmanager as idm

def Loader(url, download):
    pyloader = idm.Downloader(worker=20,
        part_size=10000,
        resumable=True)
    pyloader.download(url, output)
Loader('input url link to your download wish', 'input the desired output')
Loader('youtube.com', 'video.mkv')
