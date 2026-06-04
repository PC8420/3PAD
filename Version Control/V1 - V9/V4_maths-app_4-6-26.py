import tkinter as tk 
from tkinter import *
from tkinter import ttk, messagebox
import random
import os
from PIL import Image, ImageTk
from collections import namedtuple

CUSTOM_FONT = "comic sans MS"

COLOUR_1 = "#000000"
COLOUR_2 = "#d04b48"

#====================================================================================================================================================================

def quit_program(window_type):
    # Quit command
    window_type.destroy()

#====================================================================================================================================================================

def login_menu():
    login_window = Tk()
    login_window.geometry("1280x640")
    login_window.configure (bg="#aaaaaa")
    login_window.title("Maths Mania! | Login Menu")

#====================================================================================================================================================================

    login_bg = tk.PhotoImage(file = "images/main_bg.png")
    quit = tk.PhotoImage(file = "images/quit.png")

#====================================================================================================================================================================

    login_canvas = Canvas(login_window, width = 1280, height = 640, bg="purple")
    login_canvas.pack(fill="both", expand=True)
    login_canvas.create_image(0,0, image=login_bg, anchor="nw")

#====================================================================================================================================================================
    test_frame = Frame(login_canvas, bg=COLOUR_1, width=2000, height = 120)
    test_frame.pack(pady=(0))

    quit_button = Button(login_canvas, bg = COLOUR_1, text="X", font=(CUSTOM_FONT, 30, "bold"), fg = "white", command = lambda: quit_program(login_window), image = quit)    
    win_quit_button = login_canvas.create_window((1115,30), anchor= "nw", window=quit_button)

    # login_label = Label(login_canvas, bg = "#d6bfff", text="LOGIN", font=(CUSTOM_FONT, 35, "bold"), height = 1, width = 30)
    # login_label.pack(fill=BOTH, expand=1, pady = 20)

    scroll_main_frame = Frame(login_canvas, bg=COLOUR_1)
    scroll_main_frame.pack(fill=BOTH, expand=1, pady=(100, 50), padx=100)

    login_window.mainloop()

#====================================================================================================================================================================

def mode_menu(window_type):
    mode_window = Toplevel(window_type)
    mode_window.geometry("1280x640")
    mode_window.configure (bg="#584353")
    mode_window.title("Maths Mania! | Gamemode Menu")

def main_menu():
#====================================================================================================================================================================

# Main window settings

    main_window = Tk()
    main_window.geometry("1280x640")
    main_window.configure (bg="#584353")
    main_window.title("Maths Mania! | Home Menu")

#====================================================================================================================================================================

# Import images
    main_bg = tk.PhotoImage(file = "images/main_bg.png")
    play = tk.PhotoImage(file = "images/play_test.png")
    leaderboard = tk.PhotoImage(file = "images/leaderboard_test.png")
    settings = tk.PhotoImage(file = "images/settings_test.png")
    quit = tk.PhotoImage(file = "images/quit.png")
    title = tk.PhotoImage(file = "images/test_title.png")

# Add images

    main_canvas = Canvas(main_window, width = 1280, height = 640, bg="purple")
    main_canvas.pack(fill="both", expand=True)
    main_canvas.create_image(0,0, image=main_bg, anchor="nw")

#====================================================================================================================================================================

# Main window widgets with custom images

    title_label = Label(main_canvas, image = title, bg=COLOUR_1)    
    win_title_label = main_canvas.create_window((450,20), anchor= "nw", window=title_label)

    quit_button = Button(main_canvas, bg = COLOUR_1, text="X", font=(CUSTOM_FONT, 30, "bold"), fg = "white", command = lambda: quit_program(main_window), image = quit)    
    win_quit_button = main_canvas.create_window((1115,30), anchor= "nw", window=quit_button)

    play_button = Button(main_canvas, bg = COLOUR_1, text="PLAY", font=(CUSTOM_FONT, 30, "bold"), fg = "white", image = play, command = lambda: mode_menu(main_window))    
    win_play_button = main_canvas.create_window((80,205), anchor= "nw", window=play_button)

    leaderboard_button = Button(main_canvas, bg = COLOUR_1, text="PLAY", font=(CUSTOM_FONT, 30, "bold"), fg = "white", image = leaderboard)    
    win_leaderboard_button = main_canvas.create_window((770,205), anchor= "nw", window=leaderboard_button)

    setting_button = Button(main_canvas, bg = COLOUR_1, text="PLAY", font=(CUSTOM_FONT, 30, "bold"), fg = "white", image = settings)    
    win_setting_button = main_canvas.create_window((770,430), anchor= "nw", window=setting_button)

    main_window.mainloop()

#====================================================================================================================================================================

def main():
    login_menu()
    main_menu()

main()