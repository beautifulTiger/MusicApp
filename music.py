import pygame
from tkinter import *


def play_music():
    music_file_path = r"C:\Users\esty\Downloads\05 Instrumental.mp3"
    pygame.mixer.init()
    pygame.mixer.music.load(music_file_path)
    pygame.mixer.music.play()



    
    

 

    
def stop_music():
    pygame.mixer.music.stop()
    

root = Tk()
play_music = Button(root, text = "Play music",command = play_music)
play_music.pack()
stop_music = Button(root, text = "Stop music", command=stop_music)
stop_music.pack()
root.mainloop()
