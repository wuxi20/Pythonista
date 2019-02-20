from pytube import YouTube

yt = YouTube(str(eval(input("Enter the video link: "))))
videos = yt.get_videos()

s = 1
for v in videos:
    print((str(s)+". "+str(v)))
    s += 1

n = int(eval(input("Enter the number of the video: ")))
vid = videos[n-1]

destination = str(eval(input("Enter the destination: ")))
vid.download(destination)

print((yt.filename+"\nHas been successfully downloaded"))

