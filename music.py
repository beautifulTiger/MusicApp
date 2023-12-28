import pygame
from tkinter import *
from tkinter import ttk

music_on = True
def play_music():
    music_file_path = r"C:\Users\esty\Downloads\05 Instrumental.mp3"
    pygame.mixer.init()
    pygame.mixer.music.load(music_file_path)
    pygame.mixer.music.play()
 
   
def stop_music():
    pygame.mixer.music.stop()
   
    print('hello')
   
      
# window

window = Tk()
window.title('Music')
window.geometry('500x250')

#title
title = ttk.Label(master = window, text = 'My music app', font = 'calibri 24 bold')
title.pack()

# input field
input_frame = ttk.Frame(master = window)

add_music = ttk.Entry(master=input_frame)
play_music = ttk.Button(master=input_frame, text = "Play music", command = play_music)
stop_music = ttk.Button(master = input_frame, text = 'Stop music', command = stop_music)
add_music.pack(side='left', padx = 10)
play_music.pack(side = 'left')
stop_music.pack(side = 'right')
input_frame.pack(pady = 30)

#output
output_label = ttk.Label(master = window, text = "music is not playing", font = 'Calibri 20')
output_label.pack(pady = 5)
#run
window.mainloop()
