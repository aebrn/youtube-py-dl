import pafy
import tkinter as tk

root = tk.Tk()

root.title("youtube-py-dl")
canvas = tk.Canvas(root, width=400, height=200, relief='raised')
canvas.pack()

label = tk.Label(root, text='Enter YouTube URL')
label.config(font=('verdana', 12))
canvas.create_window(200, 100, window=label)

entry = tk.Entry(root)
canvas.create_window(200, 140, window=entry)


def download():
    video = pafy.new(entry.get())
    best = video.getbest()
    best.download()


button = tk.Button(text='Download', command=download, bg='white', fg='black', font=('verdana', 12))
canvas.create_window(200, 180, window=button)

root.mainloop()