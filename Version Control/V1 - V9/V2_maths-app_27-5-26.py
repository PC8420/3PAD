import tkinter as tk 
from tkinter import *
from tkinter import ttk, messagebox
import random
import os
from PIL import Image, ImageTk
from collections import namedtuple

CUSTOM_FONT = "comic sans MS"

COLOUR_1 = "#d04b48"

def main_menu():
    main_window = Tk()
    main_window.geometry("1280x640")
    main_window.configure (bg="#584353")
    main_window.title("Maths Mania! | Home Menu")
    
    main_bg = tk.PhotoImage(file = "images/main_bg.png")
    play = tk.PhotoImage(file = "images/play.png")

    main_canvas = Canvas(main_window, width = 1280, height = 640, bg="purple")
    main_canvas.pack(fill="both", expand=True)
    main_canvas.create_image(0,0, image=main_bg, anchor="nw")

    quit_button = Button(main_canvas, bg = COLOUR_1, text="X", font=(CUSTOM_FONT, 30, "bold"), fg = "white", height = 1, width = 4, command = quit)    
    win_quit_button = main_canvas.create_window((1113,30), anchor= "nw", window=quit_button)

    play_button = Button(main_canvas, bg = COLOUR_1, text="PLAY", font=(CUSTOM_FONT, 30, "bold"), fg = "white", image = play)    
    win_play_button = main_canvas.create_window((50,30), anchor= "nw", window=play_button)

    main_window.mainloop()

main_menu()