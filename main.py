import pafy


url = input("url:")
video = pafy.new(url)
best = video.getbest()
best.download()
print("downloaded")
