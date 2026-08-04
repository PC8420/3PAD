#Author Name: Pascal Chan
#Program Name: Julie's Party Shop
#Program use: Provide an alternative method for younger students struggling to learn maths
#Help: go to README.txt
#6.7.26

#Importing different non core libraries
import tkinter as tk 
from tkinter import *
from tkinter import ttk, messagebox
import random
import os
from PIL import Image, ImageTk
from collections import namedtuple
import pygame
from enum import Enum
from fractions import Fraction
import math
#import customtkinter as ctk

# CONSTANTS
CUSTOM_FONT = "comic sans MS"
FILE_PATH = "USER"

# Colours to be used for fonts, backgrounds, labels etc
COLOUR_1 = "#000000"
COLOUR_2 = "#d04b48"
COLOUR_3 = "#ffffff"
COLOUR_4 = "#3dd67e"
COLOUR_5 = "#ffbc1f"
COLOUR_6 = "#d6bfff"
COLOUR_7 = "#896abf"

# Constant window size 
WINDOW_HEIGHT = 640
WINDOW_LENGTH = 1280

# Password and username limits.
PASSWORD_MAX = 30
PASSWORD_MIN = 5
USERNAME_MAX = 15
USERNAME_MIN = 5

# Game settings.
QUESTIONS_PER_GAME = 5

#====================================================================================================================================================================

class Difficulty(Enum):
    EASY = 1
    MEDIUM = 2
    HARD = 3

class GameType(Enum):
    ADDITION = 1
    SUBTRACTION = 2
    MULTIPLICATION = 3
    DIVISION = 4
    ALGEBRA = 5
    EXPONENTS = 6
    FRACTIONS = 7
    STATISTICS = 8

#====================================================================================================================================================================

class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password

#=======================================================================================================================================

class Player:
    def __init__(self):
        self.lives = 3
        self.score = 0
        self.question_asked = 0

#=======================================================================================================================================
class Question:
    def __init__(self, game_type):
        self.game_type = game_type

        self.answer = 0
        self.num_1 = 0
        self.num_2 = 0
        self.num_3  = 0
        self.num_4 = 0

#=======================================================================================================================================
class SimpleQuestion(Question):
    def generate_question(self, game_type):
        self.num_1 = random.randint(-10, 10)
        self.num_2 = random.randint(-10, 10)

        match game_type:
            case GameType.ADDITION:
                operation = "+"
                self.answer = self.num_1 + self.num_2
                self.answer = str(self.answer)
                self.question_text = f"What is {self.num_1} {operation} {self.num_2}? " 

            case GameType.SUBTRACTION:
                operation = "-"
                self.answer = self.num_1 - self.num_2
                self.answer = str(self.answer)
                self.question_text = f"What is {self.num_1} {operation} {self.num_2}? " 

            case GameType.MULTIPLICATION:
                operation = "x"
                self.answer = self.num_1 * self.num_2
                self.answer = str(self.answer)
                self.question_text = f"What is {self.num_1} {operation} {self.num_2}? " 

            case GameType.DIVISION:
                operation = "÷"
                self.answer = self.num_2
                self.answer = str(self.answer)
                self.question_text = f"What is {self.num_1 * self.num_2} {operation} {self.num_1}?"
            
            case GameType.EXPONENTS:
                operation = "^"
                self.num_1 = random.randint(0, 5)
                self.num_2 = random.randint(0, 4)
                
                self.answer = self.num_1 ** self.num_2
                self.answer = str(self.answer)
                self.question_text = f"What is {self.num_1} {operation} {self.num_2}? " 

            case GameType.ALGEBRA:
                self.operation = random.randint(1, 2)
                self.num_3 = random.randint(-10, 10)

                if self.operation == 1:
                    operation = "+"
                    result = (self.num_1 * self.num_2) + self.num_3

                elif self.operation == 2:
                    operation = "-"
                    result = (self.num_1 * self.num_2) - self.num_3

                self.answer = self.num_2
                self.answer = str(self.answer)
                self.question_text = f"Solve for 𝑥: {self.num_1}𝑥 {operation} {self.num_3} = {result}"

            case GameType.FRACTIONS:
                self.operation = random.randint(5, 5)
                self.num_3 = random.randint(-10, 10)

                self.num_1 = 0
                self.num_3 = 0
                self.num_2 = 0
                self.num_4 = 0

                while self.num_2 == 0 or self.num_4 ==0 or self.num_3==0:
                    self.num_1 = random.randint(-20, 20)
                    self.num_2 = random.randint(-20, 20)
                    self.num_3 = random.randint(-20, 20)
                    self.num_4 = random.randint(-20, 20)

                n1 = Fraction (numerator=self.num_1, denominator=self.num_2)
                n2 = Fraction (numerator=self.num_3, denominator=self.num_4)
                print(n1, n2)

                if self.operation == 1:
                    operation = "+"
                    self.question_text = f"What is {self.num_1}/{self.num_2} {operation} {self.num_3}/{self.num_4}? " 
                    print(n1, n2)
                    self.answer = n1 + n2
                    self.answer = str(self.answer)
                    
                elif self.operation == 2:
                    operation = "-"
                    self.question_text = f"What is {self.num_1}/{self.num_2} {operation} {self.num_3}/{self.num_4}? " 
                    self.answer = n1 - n2
                    self.answer = str(self.answer)

                elif self.operation == 3:
                    operation = "x"
                    self.question_text = f"What is {self.num_1}/{self.num_2} {operation} {self.num_3}/{self.num_4}? " 
                    self.answer = n1 * n2
                    self.answer = str(self.answer)

                elif self.operation == 4:
                    operation = "÷"
                    self.question_text = f"What is {self.num_1}/{self.num_2} {operation} {self.num_3}/{self.num_4}? " 
                    self.answer = n1/n2
                    self.answer = str(self.answer)

                elif self.operation == 5:
                    while math.gcd((self.num_1*self.num_2), (self.num_3*self.num_4)) == 1 or self.num_3*self.num_4 == 0 or self.num_1*self.num_2 == 0:
                        self.num_1 = random.randint(-5, 10)
                        self.num_3 = random.randint(-10, 5)
                        print("COMMON DENOMINATOR", math.gcd((self.num_1*self.num_2), (self.num_3*self.num_4)))

                    self.question_text = f"Simplify this fraction fully: {self.num_1*self.num_2}/{self.num_3*self.num_4}"
                    self.answer = Fraction(numerator=(self.num_1*self.num_2), denominator= (self.num_3*self.num_4))
                    self.answer = str(self.answer)

#=======================================================================================================================================

def score_menu(window_type, player_score, lives_left, total_questions):
    window_type.destroy()
    
    score_window = Toplevel(login_window)
    score_window.geometry("1280x640")
    score_window.configure (bg="#584353")
    score_window.title("Maths Mania! | Game")
    img = tk.PhotoImage(file = "images/main_bg.png")
    quit = tk.PhotoImage(file = "images/quit.png")
    
    score_canvas = Canvas(score_window, width = 1280, height = 640, bg="purple")
    score_canvas.pack(fill="both", expand=True)
    score_canvas.create_image(0,0, image=img, anchor="nw")
    score_canvas.image = img
    
    login_title_label = Label(score_canvas, text= f"You have scored {player_score}/{total_questions} {user_detail.username}.", bg = COLOUR_5, font=(CUSTOM_FONT, 20, "bold italic"), fg=COLOUR_1, width = 30, height = 1)
    login_title_label.pack()

    submit_btn = Button(score_canvas, bg = COLOUR_4, font=(CUSTOM_FONT, 20, "bold italic"), text = "New game", fg=COLOUR_1, width = 30, height = 1, command = lambda: mode_menu(score_window))
    submit_btn.pack()

    submit_btn = Button(score_canvas, bg = COLOUR_5, font=(CUSTOM_FONT, 20, "bold italic"), text = "Home", fg=COLOUR_1, width = 30, height = 1, command = lambda: [score_window.destroy(), main_menu()])
    submit_btn.pack()

def game_menu(window_type, difficulty, game_type):
    def next_question(game_type):
        if test2.lives <= 0 or test2.question_asked >= QUESTIONS_PER_GAME:
            lives_left = test2.lives
            total_questions = test2.question_asked
            player_score = test2.score
            score_menu(game_window, player_score, lives_left, total_questions)

        else:
            test.generate_question(game_type)
            login_title_label.config(text = f"{test.question_text}")

    def submit_answer(user_entry, test, test2):
        user_ans = user_entry.get()
        if user_ans == test.answer:
            answer_label.config(bg = COLOUR_4, text = f"Correct! The answer is {test.answer}")
            test2.score = test2.score + 1
            test2.question_asked = test2.question_asked + 1
            q_left_label.config(text = f"Questions remaining: {QUESTIONS_PER_GAME - test2.question_asked}")
            score_label.config(text = f"SCORE: {test2.score}/{QUESTIONS_PER_GAME}")

        else:
            answer_label.config(bg = COLOUR_2, text = f"Wrong! The correct answer is {test.answer}")
            test2.lives = test2.lives - 1
            test2.question_asked = test2.question_asked + 1
            q_left_label.config(text = f"Questions remaining: {QUESTIONS_PER_GAME - test2.question_asked}")
            live_label.config(text = f"LIVES LEFT {test2.lives}")

        user_entry.delete(0, END)        
        next_question(game_type)
    
    window_type.destroy()
    
    question_counter = 20
    gamemode = "addition"

    game_window = Toplevel(login_window)
    game_window.geometry("1280x640")
    game_window.configure (bg="#584353")
    game_window.title("Maths Mania! | Game")
    img = tk.PhotoImage(file = "images/main_bg.png")
    quit = tk.PhotoImage(file = "images/quit.png")
    
    game_canvas = Canvas(game_window, width = 1280, height = 640, bg="purple")
    game_canvas.pack(fill="both", expand=True)
    game_canvas.create_image(0,0, image=img, anchor="nw")
    game_canvas.image = img

    login_title_label = Label(game_canvas, text= "", bg = COLOUR_5, font=(CUSTOM_FONT, 25, "bold italic"), fg=COLOUR_1, width = 40, height = 1)
    login_title_label.pack(fill=("x"))
    
    answer_label = Label(game_canvas, text= "", bg = COLOUR_5, font=(CUSTOM_FONT, 20, "bold italic"), fg=COLOUR_1, width = 30, height = 1)
    answer_label.pack(fill=("x"), padx=100, pady=20)
    
    live_label = Label(game_canvas, text= "Lives left: 3", bg = COLOUR_6, font=(CUSTOM_FONT, 20, "bold italic"), fg=COLOUR_1, width = 30, height = 1)
    live_label.pack()

    score_label = Label(game_canvas, text= f"0/{QUESTIONS_PER_GAME}", bg = COLOUR_6, font=(CUSTOM_FONT, 20, "bold italic"), fg=COLOUR_1, width = 30, height = 1)
    score_label.pack()

    q_left_label = Label(game_canvas, text= f"Questions Remaining: {QUESTIONS_PER_GAME}", bg = COLOUR_6, font=(CUSTOM_FONT, 20, "bold italic"), fg=COLOUR_1, width = 30, height = 1)
    q_left_label.pack()

    user_entry = Entry(game_canvas, bg = "#aaaaaa", font=(CUSTOM_FONT, 20, "bold"), width = 45)
    user_entry.pack()

    test = SimpleQuestion(gamemode)
    test2 = Player()
    next_question(game_type)
    
    submit_btn = Button(game_canvas, bg = COLOUR_5, font=(CUSTOM_FONT, 20, "bold italic"), text = "submit", fg=COLOUR_1, width = 30, height = 1, command = lambda: submit_answer(user_entry, test, test2))
    submit_btn.pack()

#====================================================================================================================================================================
def write_user_data(data, edit_type):

    # Opens file path (USER.txt) and joins data using ,
    # Edit type determines whether the program is adding, reading or replacing the text file
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

    # If the password or username was not entered, then the program will say that the account can't be found.
    if not verify_password or not verify_username:
        messagebox.showerror("Error", "Account could not be found", parent=window_type)
        return False

    # If there are spaces or commas in the program (invalid username and passwords), then the program will respond and say that the account can't be found.
    if " " in verify_password or " " in verify_username or "," in verify_password or "," in verify_username:
        messagebox.showerror("Error", "Account could not be found", parent=window_type)
        return False

    return True

def find_account(window_type, user_password, username):
    global user_detail
    # Determines whether all of the required user info has been passed
    if verify_account(window_type, user_password, username) == True:
        confirm = True

        # Reads the user data from a file
        file_data = read_user_data()
        
        # Creates an empty list
        user_info = []

        # Grabs the data from the username and password entry boxes
        verify_password = user_password.get()
        verify_username = username.get()

        # Appends user info into the user_info list (empty list), then peels of the outer [], by grabbing the a sublist within the user_info list
        # So before username_info = [ [sublist] ], but by doing user_info = user_info[0], user_info is now = [ list ]
        user_info.append([verify_username, verify_password])
        user_info = user_info[0]

        # print("TEST:", file_data)
        # print("USER", user_info)

        # Uses a for loop to check each sublist found from the file_data, and compares it with the user_info list
        # If both lists are the same (same username and password), then it means that the account is valid 
        for login_detail in file_data:
            # print(login_detail)
            # print(user_info, "\n")


            # Hides the login menu and calls the main menu function
            if login_detail == user_info:
                    login_window.withdraw()    
                    user_detail = User(verify_username, verify_password)    
                    main_menu()

        # If the user_info list did not match the list from the file_data, then it means that what the user inputted was not a real account, so a messagebox will show up saying that the account can't be found.
        else:
            messagebox.showerror("Error", "Account could not be found", parent=window_type)
                # print("found")
                # print("PASSWORD FILE:", login_detail, "USER INFO: ", user_info)

#====================================================================================================================================================================

def save_data(window_type, user_password, username):
    global user_detail
    user_login_info = []

    # Grabs the user inputted password and username and appends them to an empty list.
    user_password = user_password.get()
    username = username.get()

    # Calls the write_user_data function, with "a" being passed as the program is appending to the file, rather than completely rewriting it.
    user_login_info.append([username, user_password])    
    write_user_data(user_login_info, "a")
    
    # Messagebox to confirm account was created and hides the login window and calls for the main menu function.
    messagebox.showinfo("Account Created", f"Your account has been created. Welcome to Maths Mania {username}!", parent=window_type)
    login_window.withdraw()
    
    user_detail = User(username, user_password)    
    
    main_menu()

#====================================================================================================================================================================

def create_account(window_type, user_password, username):
    
    # If the user data is valid after having it being checked in the verify_create_account function, then it will call the save_data function.
    if verify_create_account(window_type, user_password, username) == True:
        save_data(window_type, user_password, username)

def verify_create_account(window_type, user_password, username):
    
    # Grabs the user info (password and username).
    verify_password = user_password.get()
    verify_username = username.get()

    # if no username or password was entered, then the program will return false, then the program will return false and a message box will say that the account can't be created
    if not verify_password or not verify_username:
        messagebox.showerror("Account could not be created", "Please create a username and password.", parent=window_type)
        return False

    # If there is a space or comma in the username or password, then the program will return false and a message box will say that the account can't be created
    if " " in verify_password or " " in verify_username or "," in verify_password or "," in verify_username:
        messagebox.showerror("Account could not be created", "Your username and password must not have spaces or commas in them.", parent=window_type)
        return False

    # Checks whether the entered username is greater than the max length, less than the minimum length. It also checks if the entered password is less than the minimum length or greater than the max length.
    # If any of these are true, then the program will return false and a message box will say that the account can't be created
    if len(verify_username) > USERNAME_MAX or len(verify_password) > PASSWORD_MAX or len(verify_username) < USERNAME_MIN or len(verify_password) < PASSWORD_MIN:
        messagebox.showerror("Account could not be created", f"Your username must be between {USERNAME_MIN} and {USERNAME_MAX} characters.\nYour password must be between {PASSWORD_MIN} and {PASSWORD_MAX} characters.", parent=window_type)
        return False
    
    # Reads the USER_INFO file, and checks for the first item in the username and password sublist. If str(row[0]) matches with the entered username, then it means that this username has already been created
    # So the program will not allow the user to create an account with that name and will return false
    user_data = read_user_data()
    if [row for row in user_data if (str(row[0])) == verify_username]:
        messagebox.showerror("Account could not be created", f"This username already exists.\nYour Username: {verify_username}.", parent=window_type)
        return False

    # If all of these requirements are met, then the program will return a true statement back to the create_account function
    return True

#====================================================================================================================================================================

def quit_program(window_type):
    # Quit command
    # The function is passed a window varaible so that the program can dynamically delete whatever window variable it has been sent.
    # For example my program might send the main_menu window variable to this function and it will delete this window. Only the login window will use os.exit as it is a top level and can't be destroyed.
    if window_type == login_window:
        os._exit(0)
        
    else:
        window_type.destroy()

#====================================================================================================================================================================

def mode_menu(window_type):
    # Mode menu settings
    mode_window = Toplevel(login_window)
    mode_window.geometry("1280x640")
    mode_window.configure (bg="#584353")
    mode_window.title("Maths Mania! | Gamemode Menu")

    window_type.destroy()

    # Constants to determine the placement of buttons
    ROW_BUTTON_1 = 110
    ROW_BUTTON_2 = 330

    # Import images
    img = tk.PhotoImage(file = "images/main_bg_2.png")
    quit = tk.PhotoImage(file = "images/quit.png")

    addition_img = tk.PhotoImage(file = "images/addition.png")
    division_img = tk.PhotoImage(file = "images/division.png")
    multiplication_img = tk.PhotoImage(file = "images/multiplication.png")
    fractions_img = tk.PhotoImage(file = "images/fractions.png")
    exponents_img = tk.PhotoImage(file = "images/exponents.png")
    algebra_img = tk.PhotoImage(file = "images/algebra.png")
    statistics_img = tk.PhotoImage(file = "images/statistics.png")
    subtraction_img = tk.PhotoImage(file = "images/subtraction.png")

    # Creates a background canvas and adds the background image to it, this image is expanded on the x and y axis so it fills the screen.
    mode_canvas = Canvas(mode_window, width = 1280, height = 640, bg="purple")
    mode_canvas.pack(fill="both", expand=True)
    mode_canvas.create_image(0,0, image=img, anchor="nw")
    mode_canvas.image = img

    # Adds a banner at the top of the screen
    banner_label = Label(mode_canvas, bg = COLOUR_5, font = (CUSTOM_FONT, 20, "bold"), text = "SELECT GAMEMODE", width = 75, height = 2)    
    win_banner_label = mode_canvas.create_window((0,0), anchor= "nw", window=banner_label)

    # Creates a back_button, and calls for quit_program to destroy this window, then it calls the main_menu function to open the main menu.
    quit_button = Button(mode_canvas, bg = COLOUR_1, command = lambda: [quit_program(mode_window), main_menu()], image = quit)    
    win_quit_button = mode_canvas.create_window((1115,5), anchor= "nw", window=quit_button)
    quit_button.image = quit

# ====================================================================================================================================================

    # Creates difficulty buttons but does not display them yet


#    easy_button = Button(mode_canvas, bg = COLOUR_4, font = (CUSTOM_FONT, 18, "bold"), text = "EASY", command = lambda: main_game("EASY", mode_window), width = 15, height = 1)    
#    medium_button = Button(mode_canvas, bg = COLOUR_5, font = (CUSTOM_FONT, 18, "bold"), text = "MEDIUM", command = lambda: main_game("MEDIUM", mode_window), width = 15, height = 1)    
#    hard_button = Button(mode_canvas, bg = COLOUR_2, font = (CUSTOM_FONT, 18, "bold"), text = "HARD", command = lambda: main_game("HARD", mode_window), width = 15, height = 1)    


    def activate_btn(game_type):
        # When a gamemode button is clicked, it will now activate the easy, medium, hard buttons and display them with .pack()
        easy_button = Button(mode_canvas, bg = COLOUR_4, font = (CUSTOM_FONT, 18, "bold"), text = "EASY", command = lambda: game_menu(mode_window, Difficulty.EASY, game_type), width = 15, height = 1)
        win_easy_button = mode_canvas.create_window((195, 555), anchor= "nw", window=easy_button)

        medium_button = Button(mode_canvas, bg = COLOUR_5, font = (CUSTOM_FONT, 18, "bold"), text = "MEDIUM", command = lambda: game_menu(mode_window, Difficulty.MEDIUM, game_type), width = 15, height = 1)
        win_medium_button = mode_canvas.create_window((525, 555), anchor= "nw", window=medium_button)
        
        hard_button = Button(mode_canvas, bg = COLOUR_2, font = (CUSTOM_FONT, 18, "bold"), text = "HARD", command = lambda: game_menu(mode_window, Difficulty.HARD, game_type), width = 15, height = 1)
        win_hard_button = mode_canvas.create_window((855, 555), anchor= "nw", window=hard_button)

        # Uses config to change the text on the banner
        banner_label.config(text= f"GAMEMODE SELECTED: {game_type.name}")

#====================================================================================================================================================================

    # Create buttons with images for each mode. When clicked, it will pass a certain text (EG. "ADDITION") to the activate_btn function. This is so the banner can change it's name after a mode button was clicked.
    addition_button = Button(mode_canvas, bg = COLOUR_1, image = addition_img, command = lambda: activate_btn(GameType.ADDITION))    
    win_addition_button = mode_canvas.create_window((195, ROW_BUTTON_1), anchor= "nw", window=addition_button)
    addition_button.image = addition_img

    subtraction_button = Button(mode_canvas, bg = COLOUR_1, image = subtraction_img, command = lambda: activate_btn(GameType.SUBTRACTION))    
    win_subtraction_button = mode_canvas.create_window((425, ROW_BUTTON_1), anchor= "nw", window=subtraction_button)
    subtraction_button.image = subtraction_img

    division_button = Button(mode_canvas, bg = COLOUR_1, image = division_img, command = lambda: activate_btn(GameType.DIVISION))    
    win_division_button = mode_canvas.create_window((655, ROW_BUTTON_1), anchor= "nw", window=division_button)
    division_button.image = division_img

    multiplication_button = Button(mode_canvas, bg = COLOUR_1, image = multiplication_img, command = lambda: activate_btn(GameType.MULTIPLICATION))    
    win_multiplication_button = mode_canvas.create_window((885, ROW_BUTTON_1), anchor= "nw", window=multiplication_button)
    multiplication_button.image = multiplication_img

    fractions_button = Button(mode_canvas, bg = COLOUR_1, image = fractions_img, command = lambda: activate_btn(GameType.FRACTIONS))    
    win_fractions_button = mode_canvas.create_window((195, ROW_BUTTON_2), anchor= "nw", window=fractions_button)
    fractions_button.image = fractions_img

    exponents_button = Button(mode_canvas, bg = COLOUR_1, image = exponents_img, command = lambda: activate_btn(GameType.EXPONENTS))    
    win_exponents_button = mode_canvas.create_window((425, ROW_BUTTON_2), anchor= "nw", window=exponents_button)
    exponents_button.image = exponents_img

    algebra_button = Button(mode_canvas, bg = COLOUR_1, image = algebra_img, command = lambda: activate_btn(GameType.ALGEBRA))    
    win_algebra_button = mode_canvas.create_window((655, ROW_BUTTON_2), anchor= "nw", window=algebra_button)
    algebra_button.image = algebra_img

    statistics_button = Button(mode_canvas, bg = COLOUR_1, image = statistics_img, command = lambda: activate_btn(GameType.STATISTICS))    
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

# Creates a background canvas and adds the background image to it, this image is expanded on the x and y axis so it fills the screen.

    main_canvas = Canvas(main_window, width = 1280, height = 640, bg="purple")
    main_canvas.pack(fill="both", expand=True)
    main_canvas.create_image(0,0, image=main_bg, anchor="nw")

#====================================================================================================================================================================

# Main window widgets with custom images

    title_label = Label(main_canvas, image = title, bg=COLOUR_1, borderwidth=0, highlightthickness=0)    
    win_title_label = main_canvas.create_window((450,20), anchor= "nw", window=title_label)

    # Calls the quit_program function when clicked
    quit_button = Button(main_canvas, bg = COLOUR_1, text="X", font=(CUSTOM_FONT, 30, "bold"), fg = "white", command = lambda: quit_program(main_window), image = quit)    
    win_quit_button = main_canvas.create_window((1115,30), anchor= "nw", window=quit_button)

    # Calls the mode_menu function when clicked
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

    # Loads images into the program
    login_bg = tk.PhotoImage(file = "images/login_bg.png")
    quit = tk.PhotoImage(file = "images/quit.png")
    password_hide = tk.PhotoImage(file = "images/password_hide.png")
    password_unhide = tk.PhotoImage(file = "images/password_unhide.png")

#====================================================================================================================================================================

    # Creates a canvas, and places the background image that was already loaded, this image is expanded on both the x and y axis
    login_canvas = Canvas(login_window, width = 1280, height = 640, bg="purple")
    login_canvas.pack(fill="both", expand=True)
    login_canvas.create_image(0,0, image=login_bg, anchor="nw")

#====================================================================================================================================================================

    # Creates a frame for the login title banner
    login_title_frame = Frame(login_canvas, bg=COLOUR_7)
    login_title_frame.pack(fill = "x", pady=(0,20))

    # Places the label inside the login title frame and has a text that says welcome to maths mania (pack() places this widget on the screen)
    login_title_label = Label(login_title_frame, bg = COLOUR_5, text="WELCOME TO MATHS MANIA!", font=(CUSTOM_FONT, 20, "bold italic"), fg=COLOUR_1, width = 30, height = 1)
    login_title_label.pack(padx=(400,0), side=LEFT)

    # Quits the program
    quit_button = Button(login_title_frame, bg = COLOUR_1, text="X", font=(CUSTOM_FONT, 30, "bold"), fg = "white", command = lambda: quit_program(login_window), image = quit)    
    quit_button.pack(side=RIGHT, padx=(0,50), pady=(20))

#====================================================================================================================================================================

    # Creates the background for the username entry, username label, password label and password entry frame by expanding on both the x and y axis
    user_info_frame = Frame(login_canvas, bg=COLOUR_7)
    user_info_frame.pack(fill=("x"), expand=1, pady=(30, 30), padx=50)

#====================================================================================================================================================================

    # Creates the username frame into the user info frame
    username_frame = Frame(user_info_frame, bg = COLOUR_7)
    username_frame.pack(fill=("x"), expand=1, pady=(50, 20), padx=(50, 50))

    # Places the username label into the username frame and is configured so that it is placed on the left hand side of the screen
    username_label = Label(username_frame, bg = COLOUR_6, text="USERNAME", font=(CUSTOM_FONT, 20, "bold italic"), width = 12, height = 1)
    username_label.pack(padx=(50,0), pady=(0,0), side = LEFT)

    # Places the username entry box in the user info frame and next to the username label. This is done by putting side = left which forces this widget to be placed next to the username label
    # (username label must also be side = left for this to work) Where the padx creates a distance between the username label and username entry
    username_entry = Entry(username_frame, bg = "#aaaaaa", font=(CUSTOM_FONT, 20, "bold"), width = 45)
    username_entry.pack(padx=(40), pady=(0,0), side = LEFT)

#====================================================================================================================================================================
    show_password = True

    def password_setting():
        nonlocal show_password
        # this function is a true or false switch that determines if the user can see their password or not.

        # Checks if the show password is true and if so, it will use .config to change the image of the button and .config will show the password as is it showing nothing ("")
        # It will then change show_password to = false 
        if show_password == True:
            unhide_button.config(image = password_hide)
            password_entry.config(show="")
            show_password = False
            #print("TEST: ", show_password)
        
        # If the show password isn't true then the program will show the "*" symbol when you type, and change the image of the button back to password unhide
        else:
            unhide_button.config(image = password_unhide)
            password_entry.config(show="*")
            show_password = True
            #print("BUTTON COMMAND", show_password)

    # Creates the password frame into the user info frame
    password_frame = Frame(user_info_frame, bg = COLOUR_7)
    password_frame.pack(fill=("x"), expand=1, pady=(0, 20), padx=50)

    # Places the password label into the password frame and is configured so that it is placed on the left hand side of the screen
    password_label = Label(password_frame, bg = COLOUR_6, text="PASSWORD", font=(CUSTOM_FONT, 20, "bold italic"), width = 12, height = 1)
    password_label.pack(padx=(50,0), pady=(0,0), side = LEFT)

    # Places the password entry box in the user info frame and next to the password label. This is done by putting side = left which forces this widget to be placed next to the password label
    # (password label must also be side = left for this to work) Where the padx creates a distance between the password label and password entry. Show "*" makes it so that when you type something into the entry box, it will show *
    password_entry = Entry(password_frame, bg = "#aaaaaa", font=(CUSTOM_FONT, 20, "bold"), width = 41, show="*")
    password_entry.pack(padx=(40,0), pady=(0,0), side = LEFT)

    # When clicking this button, the button will call the password settings function
    unhide_button = Button(password_frame, bg = COLOUR_1, text="X", font=(CUSTOM_FONT, 30, "bold"), fg = "white", command = password_setting, image = password_unhide)    
    unhide_button.pack(side=LEFT, padx=(15,0))

#====================================================================================================================================================================

    # Creates a frame for the buttons, and is placed inside the user info frame with the same background colour so that the user_button_frame blends in.
    user_button_frame = Frame(user_info_frame, bg = COLOUR_7)
    user_button_frame.pack(fill=BOTH, expand=1, pady=(0, 50), padx=50)

    # def verify_account():
    #     test = False
    #     print("test")

    #     if test == True:
    #         main_menu()
    #         login_window.withdraw()

    # Calls the find_account function and passes various variables to it.
    confirm_button = Button(user_button_frame, bg = COLOUR_4, text="CONFIRM LOGIN", font=(CUSTOM_FONT, 20, "bold"), fg = COLOUR_1, width = 20, command= lambda: (find_account(login_window,password_entry, username_entry)))
    confirm_button.pack(side=LEFT, padx=(200,20))

    # Calls the create_account function and passes various variables to it.
    create_account_button = Button(user_button_frame, bg = COLOUR_5, text="CREATE ACCOUNT", font=(CUSTOM_FONT, 20, "bold"), fg = COLOUR_1, width = 20, command= lambda: (create_account(login_window, password_entry, username_entry)))
    create_account_button.pack(side=RIGHT, padx=(20,200))

    login_window.mainloop()

def main():
    # Function to start the program
    login_menu()
    #main_menu()

# Starts the program
main()

#========================================

# def minigame_pygame():
#     # WORK IN PROGRESS
    
#     print("yes")

#     screen = pygame.display.set_mode((WINDOW_LENGTH, WINDOW_HEIGHT))
#     pygame.display.set_caption('Button Demo')
#     pygame.quit()

#     # start_img = pygame.image.load('images/addition.png').convert_alpha()
#     # exit_img = pygame.image.load('images/subtraction.png').convert_alpha()

#     class Button():
#         def __init__(self, x, y, image):
#             self.image = image
#             self.rect = self.image.get_rect()
#             self.rect.topleft = (x, y)
        
#         def draw(self):
#             screen.blit(self.image, (self.rect.x, self.rect.y))

#     # start_button = Button(100, 200, start_img)
#     # exit_button = Button(100, 200, exit_img)

#     run = True
#     while run:
#         screen.fill((200, 300, 200))
#         for event in pygame.event.get():
#             if event.type == pygame.QUIT:
#                 run = False