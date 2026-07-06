import tkinter as tk 
from tkinter import *
from tkinter import ttk, messagebox
import random
import os
from PIL import Image, ImageTk
from collections import namedtuple
import pygame
#import customtkinter

CUSTOM_FONT = "comic sans MS"
FILE_PATH = "USER"

COLOUR_1 = "#000000"
COLOUR_2 = "#d04b48"
COLOUR_3 = "#ffffff"
COLOUR_4 = "#3dd67e"
COLOUR_5 = "#ffbc1f"
COLOUR_6 = "#d6bfff"
COLOUR_7 = "#896abf"

WINDOW_HEIGHT = 640
WINDOW_LENGTH = 1280

PASSWORD_MAX = 30
PASSWORD_MIN = 5
USERNAME_MAX = 15
USERNAME_MIN = 5

#====================================================================================================================================================================
# Opens file path (USER.txt) and joins data using ,
def write_user_data(data, edit_type):
    with open(FILE_PATH, edit_type) as file:
        # test = data
        # print(test)
        for entry in data:
            line = ",".join(map(str, entry))
            print(line)
            file.write(line + "\n")

# Reads data by first checking whether the text file exists, if not return an empty list. If file exists, program will read the file using .readlines().
# And is copied into the variable "lines". This variable is then split into many sub lists within one list.
def read_user_data():
    if not os.path.exists(FILE_PATH):
        return []
    with open(FILE_PATH, "r") as file:
        lines = file.readlines()
    return [line.strip().split(",") for line in lines]
#====================================================================================================================================================================

def verify_account(window_type, user_password, username):
    verify_password = user_password.get()
    verify_username = username.get()

    if not verify_password or not verify_username:
        messagebox.showerror("Error", "Account could not be found", parent=window_type)
        return False

    if " " in verify_password or " " in verify_username or "," in verify_password or "," in verify_username:
        messagebox.showerror("Error", "Account could not be found", parent=window_type)
        return False

    return True

def find_account(window_type, user_password, username):
    if verify_account(window_type, user_password, username) == True:
        confirm = True

        file_data = read_user_data()
        user_info = []

        verify_password = user_password.get()
        verify_username = username.get()

        user_info.append([verify_username, verify_password])
        user_info = user_info[0]

        # print("TEST:", file_data)
        # print("USER", user_info)

        for login_detail in file_data:
            # print(login_detail)
            # print(user_info, "\n")

            if login_detail == user_info:
                    login_window.withdraw()    
                    main_menu()

        else:
            messagebox.showerror("Error", "Account could not be found", parent=window_type)
                # print("found")
                # print("PASSWORD FILE:", login_detail, "USER INFO: ", user_info)

#====================================================================================================================================================================

def save_data(window_type, user_password, username):
    user_login_info = []

    user_password = user_password.get()
    username = username.get()

    user_login_info.append([username, user_password])    
    write_user_data(user_login_info, "a")
    
    messagebox.showinfo("Account Created", f"Your account has been created. Welcome to Maths Mania {username}!", parent=window_type)
    login_window.withdraw()    
    main_menu()

#====================================================================================================================================================================

def create_account(window_type, user_password, username):
    if verify_create_account(window_type, user_password, username) == True:
        save_data(window_type, user_password, username)

def verify_create_account(window_type, user_password, username):
    verify_password = user_password.get()
    verify_username = username.get()

    if not verify_password or not verify_username:
        messagebox.showerror("Account could not be created", "Please create a username and password.", parent=window_type)
        return False

    if " " in verify_password or " " in verify_username or "," in verify_password or "," in verify_username:
        messagebox.showerror("Account could not be created", "Your username and password must not have spaces or commas in them.", parent=window_type)
        return False

    if len(verify_username) > USERNAME_MAX or len(verify_password) > PASSWORD_MAX or len(verify_username) < USERNAME_MIN or len(verify_password) < PASSWORD_MIN:
        messagebox.showerror("Account could not be created", f"Your username must be between {USERNAME_MIN} and {USERNAME_MAX} characters.\nYour password must be between {PASSWORD_MIN} and {PASSWORD_MAX} characters.", parent=window_type)
        return False
    
    user_data = read_user_data()
    if [row for row in user_data if (str(row[0])) == verify_username]:
        messagebox.showerror("Account could not be created", f"This username already exists.\nYour Username: {verify_username}.", parent=window_type)
        return False

    return True

#====================================================================================================================================================================

def quit_program(window_type):
    # Quit command
    if window_type == login_window:
        os._exit(0)
        
    else:
        window_type.destroy()

#====================================================================================================================================================================

# def game_menu(difficulty, window_type):
#     game_window = Toplevel(login_window)
#     game_window.geometry("1280x640")
#     game_window.configure (bg="#584353")
#     game_window.title("Maths Mania! | Game")

#     print(difficulty)

#     window_type.destroy()
#     img = tk.PhotoImage(file = "images/main_bg.png")
#     quit = tk.PhotoImage(file = "images/quit.png")
    
#     game_canvas = Canvas(game_window, width = 1280, height = 640, bg="purple")
#     game_canvas.pack(fill="both", expand=True)
#     game_canvas.create_image(0,0, image=img, anchor="nw")
#     game_canvas.image = img

#     test = "gidf"
#     question_num = 0

#     question_banner = Label(game_canvas, bg = COLOUR_5, font = (CUSTOM_FONT, 31, "bold"), text = (f"Question {question_num}: {test}"), width = 51, height = 2)    
#     win_question_banner = game_canvas.create_window((0,0), anchor= "nw", window=question_banner)

def minigame_pygame():
    print("yes")

    screen = pygame.display.set_mode((WINDOW_LENGTH, WINDOW_HEIGHT))
    pygame.display.set_caption('Button Demo')
    pygame.quit()

    # start_img = pygame.image.load('images/addition.png').convert_alpha()
    # exit_img = pygame.image.load('images/subtraction.png').convert_alpha()

    class Button():
        def __init__(self, x, y, image):
            self.image = image
            self.rect = self.image.get_rect()
            self.rect.topleft = (x, y)
        
        def draw(self):
            screen.blit(self.image, (self.rect.x, self.rect.y))

    # start_button = Button(100, 200, start_img)
    # exit_button = Button(100, 200, exit_img)

    run = True
    while run:
        screen.fill((200, 300, 200))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False


def remove_this(a,b):
    print("hi")

def mode_menu(window_type):
    mode_window = Toplevel(login_window)
    mode_window.geometry("1280x640")
    mode_window.configure (bg="#584353")
    mode_window.title("Maths Mania! | Gamemode Menu")

    window_type.destroy()

    ROW_BUTTON_1 = 110
    ROW_BUTTON_2 = 330

# Import images
    img = tk.PhotoImage(file = "images/main_bg.png")
    quit = tk.PhotoImage(file = "images/quit.png")

    addition_img = tk.PhotoImage(file = "images/addition.png")
    division_img = tk.PhotoImage(file = "images/division.png")
    multiplication_img = tk.PhotoImage(file = "images/multiplication.png")
    fractions_img = tk.PhotoImage(file = "images/fractions.png")
    exponents_img = tk.PhotoImage(file = "images/exponents.png")
    algebra_img = tk.PhotoImage(file = "images/algebra.png")
    statistics_img = tk.PhotoImage(file = "images/statistics.png")
    subtraction_img = tk.PhotoImage(file = "images/subtraction.png")
    
    mode_canvas = Canvas(mode_window, width = 1280, height = 640, bg="purple")
    mode_canvas.pack(fill="both", expand=True)
    mode_canvas.create_image(0,0, image=img, anchor="nw")
    mode_canvas.image = img

    banner_label = Label(mode_canvas, bg = COLOUR_5, font = (CUSTOM_FONT, 20, "bold"), text = "SELECT GAMEMODE", width = 75, height = 2)    
    win_banner_label = mode_canvas.create_window((0,0), anchor= "nw", window=banner_label)
    
    quit_button = Button(mode_canvas, bg = COLOUR_1, command = lambda: [quit_program(mode_window), main_menu()], image = quit)    
    win_quit_button = mode_canvas.create_window((1115,5), anchor= "nw", window=quit_button)
    quit_button.image = quit

# ====================================================================================================================================================

    # KEEP THESE BUTTONS
    # easy_button = Button(mode_canvas, bg = COLOUR_4, font = (CUSTOM_FONT, 18, "bold"), text = "EASY", command = lambda: remove_this("EASY", mode_window), width = 15, height = 1)    
    # medium_button = Button(mode_canvas, bg = COLOUR_5, font = (CUSTOM_FONT, 18, "bold"), text = "MEDIUM", command = lambda: remove_this("MEDIUM", mode_window), width = 15, height = 1)    
    # hard_button = Button(mode_canvas, bg = COLOUR_2, font = (CUSTOM_FONT, 18, "bold"), text = "HARD", command = lambda: remove_this("HARD", mode_window), width = 15, height = 1)    

# ====================================================================================================================================================

    easy_button = Button(mode_canvas, bg = COLOUR_4, font = (CUSTOM_FONT, 18, "bold"), text = "EASY", command = lambda: minigame_pygame())
    medium_button = Button(mode_canvas, bg = COLOUR_5, font = (CUSTOM_FONT, 18, "bold"), text = "MEDIUM", command = lambda: minigame_pygame())    
    hard_button = Button(mode_canvas, bg = COLOUR_2, font = (CUSTOM_FONT, 18, "bold"), text = "HARD", command = lambda: minigame_pygame())


    def activate_btn(name_change):
        win_easy_button = mode_canvas.create_window((195, 555), anchor= "nw", window=easy_button)
        win_medium_button = mode_canvas.create_window((525, 555), anchor= "nw", window=medium_button)
        win_hard_button = mode_canvas.create_window((855, 555), anchor= "nw", window=hard_button)
        banner_label.config(text= f"GAMEMODE SELECTED: {name_change}")


    addition_button = Button(mode_canvas, bg = COLOUR_1, image = addition_img, command = lambda: activate_btn("ADDITION"))    
    win_addition_button = mode_canvas.create_window((195, ROW_BUTTON_1), anchor= "nw", window=addition_button)
    addition_button.image = addition_img

    subtraction_button = Button(mode_canvas, bg = COLOUR_1, image = subtraction_img, command = lambda: activate_btn("SUBTRACTION"))    
    win_subtraction_button = mode_canvas.create_window((425, ROW_BUTTON_1), anchor= "nw", window=subtraction_button)
    subtraction_button.image = subtraction_img

    division_button = Button(mode_canvas, bg = COLOUR_1, image = division_img, command = lambda: activate_btn("DIVISION"))    
    win_division_button = mode_canvas.create_window((655, ROW_BUTTON_1), anchor= "nw", window=division_button)
    division_button.image = division_img

    multiplication_button = Button(mode_canvas, bg = COLOUR_1, image = multiplication_img, command = lambda: activate_btn("MULTIPLICATION"))    
    win_multiplication_button = mode_canvas.create_window((885, ROW_BUTTON_1), anchor= "nw", window=multiplication_button)
    multiplication_button.image = multiplication_img

    fractions_button = Button(mode_canvas, bg = COLOUR_1, image = fractions_img, command = lambda: activate_btn("FRACTIONS"))    
    win_fractions_button = mode_canvas.create_window((195, ROW_BUTTON_2), anchor= "nw", window=fractions_button)
    fractions_button.image = fractions_img

    exponents_button = Button(mode_canvas, bg = COLOUR_1, image = exponents_img, command = lambda: activate_btn("EXPONENTS"))    
    win_exponents_button = mode_canvas.create_window((425, ROW_BUTTON_2), anchor= "nw", window=exponents_button)
    exponents_button.image = exponents_img

    algebra_button = Button(mode_canvas, bg = COLOUR_1, image = algebra_img, command = lambda: activate_btn("ALGEBRA"))    
    win_algebra_button = mode_canvas.create_window((655, ROW_BUTTON_2), anchor= "nw", window=algebra_button)
    algebra_button.image = algebra_img

    statistics_button = Button(mode_canvas, bg = COLOUR_1, image = statistics_img, command = lambda: activate_btn("STATISTICS"))    
    win_statistics_button = mode_canvas.create_window((885, ROW_BUTTON_2), anchor= "nw", window=statistics_button)
    statistics_button.image = statistics_img

#====================================================================================================================================================================

def main_menu():
# Main window settings
    global main_window
    main_window = Toplevel(login_window)
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
    title_label = Label(main_canvas, image = title, bg=COLOUR_1, borderwidth=0, highlightthickness=0)    
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

def login_menu():
    global login_window
    login_window = Tk()
    login_window.geometry("1280x640")
    login_window.configure (bg="#aaaaaa")
    login_window.title("Maths Mania! | Login Menu")

#====================================================================================================================================================================

    login_bg = tk.PhotoImage(file = "images/login_bg.png")
    quit = tk.PhotoImage(file = "images/quit.png")
    password_hide = tk.PhotoImage(file = "images/password_hide.png")
    password_unhide = tk.PhotoImage(file = "images/password_unhide.png")

#====================================================================================================================================================================

    login_canvas = Canvas(login_window, width = 1280, height = 640, bg="purple")
    login_canvas.pack(fill="both", expand=True)
    login_canvas.create_image(0,0, image=login_bg, anchor="nw")

#====================================================================================================================================================================
    login_title_frame = Frame(login_canvas, bg=COLOUR_7)
    login_title_frame.pack(fill = "x", pady=(0,20))

    login_title_label = Label(login_title_frame, bg = COLOUR_5, text="WELCOME TO MATHS MANIA!", font=(CUSTOM_FONT, 20, "bold italic"), fg=COLOUR_1, width = 30, height = 1)
    login_title_label.pack(padx=(400,0), side=LEFT)

    quit_button = Button(login_title_frame, bg = COLOUR_1, text="X", font=(CUSTOM_FONT, 30, "bold"), fg = "white", command = lambda: quit_program(login_window), image = quit)    
    quit_button.pack(side=RIGHT, padx=(0,50), pady=(20))

#====================================================================================================================================================================

    user_info_frame = Frame(login_canvas, bg=COLOUR_7)
    user_info_frame.pack(fill=("x"), expand=1, pady=(30, 30), padx=50)

#====================================================================================================================================================================

    username_frame = Frame(user_info_frame, bg = COLOUR_7)
    username_frame.pack(fill=("x"), expand=1, pady=(50, 20), padx=(50, 50))

    username_label = Label(username_frame, bg = COLOUR_6, text="USERNAME", font=(CUSTOM_FONT, 20, "bold italic"), width = 12, height = 1)
    username_label.pack(padx=(50,0), pady=(0,0), side = LEFT)

    username_entry = Entry(username_frame, bg = "#aaaaaa", font=(CUSTOM_FONT, 20, "bold"), width = 45)
    username_entry.pack(padx=(40), pady=(0,0), side = LEFT)

#====================================================================================================================================================================
    show_password = True

    def password_setting():
        nonlocal show_password
        if show_password == True:
            unhide_button.config(image = password_hide)
            password_entry.config(show="")
            show_password = False
            #print("TEST: ", show_password)
        
        else:
            unhide_button.config(image = password_unhide)
            password_entry.config(show="*")
            show_password = True
            #print("BUTTON COMMAND", show_password)


    password_frame = Frame(user_info_frame, bg = COLOUR_7)
    password_frame.pack(fill=("x"), expand=1, pady=(0, 20), padx=50)

    password_label = Label(password_frame, bg = COLOUR_6, text="PASSWORD", font=(CUSTOM_FONT, 20, "bold italic"), width = 12, height = 1)
    password_label.pack(padx=(50,0), pady=(0,0), side = LEFT)

    password_entry = Entry(password_frame, bg = "#aaaaaa", font=(CUSTOM_FONT, 20, "bold"), width = 41, show="*")
    password_entry.pack(padx=(40,0), pady=(0,0), side = LEFT)

    unhide_button = Button(password_frame, bg = COLOUR_1, text="X", font=(CUSTOM_FONT, 30, "bold"), fg = "white", command = password_setting, image = password_unhide)    
    unhide_button.pack(side=LEFT, padx=(15,0))

#====================================================================================================================================================================

    user_button_frame = Frame(user_info_frame, bg = COLOUR_7)
    user_button_frame.pack(fill=BOTH, expand=1, pady=(0, 50), padx=50)

    # def verify_account():
    #     test = False
    #     print("test")

    #     if test == True:
    #         main_menu()
    #         login_window.withdraw()

    confirm_button = Button(user_button_frame, bg = COLOUR_4, text="CONFIRM LOGIN", font=(CUSTOM_FONT, 20, "bold"), fg = COLOUR_1, width = 20, command= lambda: (find_account(login_window,password_entry, username_entry)))
    confirm_button.pack(side=LEFT, padx=(200,20))

    create_account_button = Button(user_button_frame, bg = COLOUR_5, text="CREATE ACCOUNT", font=(CUSTOM_FONT, 20, "bold"), fg = COLOUR_1, width = 20, command= lambda: (create_account(login_window, password_entry, username_entry)))
    create_account_button.pack(side=RIGHT, padx=(20,200))

    login_window.mainloop()

def main():
    login_menu()
    main_menu()

main()