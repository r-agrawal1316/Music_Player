import pygame
import tkinter as tkr
from tkinter.filedialog import askdirectory
import os

music_player = tkr.Tk()
music_player.title("My Music Player")
music_player.geometry("550x450")
music_dir = os.path.join(os.path.expanduser("~"), "Music")
directory = askdirectory(initialdir=music_dir, title="Music Files")

song_list = [os.path.join(directory, item) for item in os.listdir(directory) if item.endswith(('.mp3', '.wav'))]

play_list = tkr.Listbox(music_player, font="Helvetica 12 bold", bg='yellow', selectmode=tkr.SINGLE)
# play_list.insert(0, file_path)
for item in song_list:
    pos = 0
    play_list.insert(pos, item)
    pos += 1
pygame.init()
pygame.mixer.init()
current_song_index = 0


def play():
    pygame.mixer.music.load(song_list[current_song_index])
    var.set(song_list[current_song_index])
    pygame.mixer.music.play()
    update_song_index()


def stop():
    pygame.mixer.music.stop()


def pause():
    pygame.mixer.music.pause()


def unpause():
    pygame.mixer.music.unpause()


def next_song():
    global current_song_index
    current_song_index = (current_song_index + 1) % len(song_list)
    play()


def previous_song():
    global current_song_index
    current_song_index = (current_song_index - 1) % len(song_list)
    play()


def update_song_index():
    global current_song_index
    for i in range(len(play_list.get(0, tkr.END))):
        if play_list.get(i) == song_list[current_song_index]:
            play_list.selection_clear(0, tkr.END)
            play_list.activate(i)
            play_list.selection_set(i)
            break


var = tkr.StringVar()
song_title = tkr.Label(music_player, font="Helvetica 12 bold", textvariable=var)

song_title.pack()
Btn1 = tkr.Button(music_player, width=5, height=3, font="Helvetica 12 bold", text="PLAY", command=play, bg="blue",
                  fg="white")
Btn2 = tkr.Button(music_player, width=5, height=3, font="Helvetica 12 bold", text="STOP", command=stop, bg="red",
                  fg="white")
Btn3 = tkr.Button(music_player, width=5, height=3, font='Helvetica 12 bold', text='PAUSE', command=pause, bg='purple',
                  fg="white")
Btn4 = tkr.Button(music_player, width=5, height=3, font="Helvetica 12 bold", text="UNPAUSE", command=unpause,
                  bg="orange", fg="white")
Btn5 = tkr.Button(music_player, width=5, height=3, font="Helvetica 12 bold", text="Next", command=next_song, bg="green",
                  fg="white")
Btn6 = tkr.Button(music_player, width=5, height=3, font="Helvetica 12 bold", text="Previous", command=previous_song,
                  bg="gray", fg="white")


Btn1.pack(fill="x")
Btn2.pack(fill="x")
Btn3.pack(fill="x")
Btn4.pack(fill="x")
Btn5.pack(fill="x")
Btn6.pack(fill="x")
play_list.pack(fill="both", expand=1)
music_player.mainloop()
