#Importing all the necessary modules for python youtube video downloader
from tkinter import *
from tkinter import messagebox as mb
from pytube import YouTube

# Defining the downloader function for YouTube Video Downloader project using Python
def downloader(link, directory, filename):
    yt_link = link.get()
    save_path = directory.get()
    aftersave_filename = filename.get()

    try:
        yt = YouTube(yt_link)
        video = yt.streams.first()
        video.download(save_path, aftersave_filename)
    except:
        mb.showerror('Error', 'Connection Error! You are offline!')


def reset(l_strvar, d_strvar, fn_strvar):
    l_strvar.set('')
    d_strvar.set('')
    fn_strvar.set('')


