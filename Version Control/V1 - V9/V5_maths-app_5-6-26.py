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
COLOUR_3 = "#ffffff"
COLOUR_4 = "#3dd67e"
COLOUR_5 = "#ffbc1f"
COLOUR_6 = "#d6bfff"
COLOUR_7 = "#896abf"

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

    login_bg = tk.PhotoImage(file = "images/login_bg.png")
    quit = tk.PhotoImage(file = "images/quit.png")

#====================================================================================================================================================================

    login_canvas = Canvas(login_window, width = 1280, height = 640, bg="purple")
    login_canvas.pack(fill="both", expand=True)
    login_canvas.create_image(0,0, image=login_bg, anchor="nw")

#====================================================================================================================================================================
    login_title_frame = Frame(login_canvas, bg=COLOUR_7)
    login_title_frame.pack(fill = "x", expand=1, pady=(0,20))

    login_title_label = Label(login_title_frame, bg = COLOUR_2, text="WELCOME", font=(CUSTOM_FONT, 20, "bold"), fg=COLOUR_3, width = 12, height = 1)
    login_title_label.pack(padx=(250,0), side=LEFT)

    quit_button = Button(login_title_frame, bg = COLOUR_1, text="X", font=(CUSTOM_FONT, 30, "bold"), fg = "white", command = lambda: quit_program(login_window), image = quit)    
    quit_button.pack(side=RIGHT, padx=(0,50))
    #win_quit_button = login_canvas.create_window((1115,25), anchor= "nw", window=quit_button)

#====================================================================================================================================================================

    user_info_frame = Frame(login_canvas, bg=COLOUR_7)
    user_info_frame.pack(fill=("x"), expand=1, pady=(30, 30), padx=50)

#====================================================================================================================================================================

    username_frame = Frame(user_info_frame, bg = COLOUR_7)
    username_frame.pack(fill=("x"), expand=1, pady=(50, 20), padx=(50, 50))

    username_label = Label(username_frame, bg = COLOUR_6, text="USERNAME", font=(CUSTOM_FONT, 20, "bold"), width = 12, height = 1)
    username_label.pack(padx=(50,0), pady=(0,0), side = LEFT)

    username_entry = Entry(username_frame, bg = "#aaaaaa", font=(CUSTOM_FONT, 20, "bold"), width = 45)
    username_entry.pack(padx=(40), pady=(0,0), side = LEFT)

#====================================================================================================================================================================

    password_frame = Frame(user_info_frame, bg = COLOUR_7)
    password_frame.pack(fill=("x"), expand=1, pady=(0, 20), padx=50)

    password_label = Label(password_frame, bg = COLOUR_6, text="PASSWORD", font=(CUSTOM_FONT, 20, "bold"), width = 12, height = 1)
    password_label.pack(padx=(50,0), pady=(0,0), side = LEFT)

    password_entry = Entry(password_frame, bg = "#aaaaaa", font=(CUSTOM_FONT, 20, "bold"), width = 45)
    password_entry.pack(padx=(40), pady=(0,0), side = LEFT)

#====================================================================================================================================================================

    user_button_frame = Frame(user_info_frame, bg = COLOUR_7)
    user_button_frame.pack(fill=BOTH, expand=1, pady=(0, 50), padx=50)

    confirm_button = Button(user_button_frame, bg = COLOUR_4, text="CONFIRM LOGIN", font=(CUSTOM_FONT, 20, "bold"), fg = COLOUR_1, width = 20)
    confirm_button.pack(side=LEFT, padx=(200,20))

    create_account_button = Button(user_button_frame, bg = COLOUR_5, text="CREATE ACCOUNT", font=(CUSTOM_FONT, 20, "bold"), fg = COLOUR_1, width = 20)
    create_account_button.pack(side=RIGHT, padx=(20,200))

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