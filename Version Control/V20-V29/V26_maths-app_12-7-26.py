# Author Name: Pascal Chan
# Program Name: Maths Mania
# Program use: Provide an alternative method for younger students struggling to learn maths
# Help: go to README.txt
# 6.7.26

# Importing different non core libraries
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
import customtkinter as ctk

# CONSTANTS
CUSTOM_FONT = "comic sans MS"
CUSTOM_FONT_2 = "arial rounded mt bold"
USER_INFO = "USER"

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
QUESTIONS_PER_GAME = 50
CORRECT_ANS_XP = 50
XP_PER_LEVEL = 10000

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

# Namedtuple that is organised into this format (name, price, image).
DifficultySetting = namedtuple('DifficultySetting', ['min_1', 'max_1', 'min_2', 'max_2'])

addition_settings = {Difficulty.EASY: DifficultySetting(1, 10, 1, 10),
                    Difficulty.MEDIUM: DifficultySetting(-50, 50, -20, 10),
                    Difficulty.HARD: DifficultySetting(-1000, 1000, -1000, 1000)}

subtraction_settings = {Difficulty.EASY: DifficultySetting(1, 10, 1, 10),
                    Difficulty.MEDIUM: DifficultySetting(-50, 50, -20, 10),
                    Difficulty.HARD: DifficultySetting(-1000, 1000, -1000, 1000)}

multiplication_settings = {Difficulty.EASY: DifficultySetting(0, 5, 0, 10),
                    Difficulty.MEDIUM: DifficultySetting(-12, 12, -12, 12),
                    Difficulty.HARD: DifficultySetting(-80, 80, -40, 40)}

division_settings = {Difficulty.EASY: DifficultySetting(1, 10, 0, 5),
                    Difficulty.MEDIUM: DifficultySetting(-10, 20, -20, 20),
                    Difficulty.HARD: DifficultySetting(-100, 100, -200, 200)}

exponent_settings = {Difficulty.EASY: DifficultySetting(1, 5, 0, 2),
                    Difficulty.MEDIUM: DifficultySetting(0, 9, 3, 4),
                    Difficulty.HARD: DifficultySetting(-9, 9, 3, 4)}

algebra_settings = {Difficulty.EASY: DifficultySetting(1, 1, 1, 10),
                    Difficulty.MEDIUM: DifficultySetting(1, 10, -20, 10),
                    Difficulty.HARD: DifficultySetting(-100, 100, -200, 200)}

fraction_settings = {Difficulty.EASY: DifficultySetting(1, 10, 1, 10),
                    Difficulty.MEDIUM: DifficultySetting(-20, 20, -20, 20),
                    Difficulty.HARD: DifficultySetting(-50, 50, -50, 50)}
#====================================================================================================================================================================

class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password

#=======================================================================================================================================

class Player:
    def __init__(self):
        self.combo = 0
        self.highest_combo = 0
        self.score = 0
        self.question_asked = 0
        self.session_xp = 0

#=======================================================================================================================================
class Question:
    def __init__(self, game_type, difficulty_type):
        self.game_type = game_type
        self.difficulty_type = difficulty_type

        self.answer = 0
        self.num_1 = 0
        self.num_2 = 0
        self.num_3  = 0
        self.num_4 = 0

#=======================================================================================================================================
class SimpleQuestion(Question):
    def addition_mode(self):
        operation = "+"
        self.num_1 = random.randint(addition_settings[self.difficulty_type].min_1, addition_settings[self.difficulty_type].max_1)
        self.num_2 = random.randint(addition_settings[self.difficulty_type].min_2, addition_settings[self.difficulty_type].max_2)

        if self.difficulty_type == Difficulty.HARD:
            self.num_2 = self.num_2/4
            if self.num_2 == int(self.num_2): 
                self.num_2= int(self.num_2)

        self.answer = self.num_1 + self.num_2

        if self.answer == int(self.answer):
            self.answer = int(self.answer)

        self.answer = str(self.answer)
        self.question_text = f"What is {self.num_1} {operation} {self.num_2}?"

    def subtraction_mode(self):
        operation = "-"
        self.num_1 = random.randint(subtraction_settings[self.difficulty_type].min_1, subtraction_settings[self.difficulty_type].max_1)
        self.num_2 = random.randint(subtraction_settings[self.difficulty_type].min_2, subtraction_settings[self.difficulty_type].max_2)

        if self.difficulty_type == Difficulty.HARD:
            self.num_2 = self.num_2/4
            if self.num_2 == int(self.num_2): 
                self.num_2= int(self.num_2)

        self.answer = self.num_1 - self.num_2

        if self.answer == int(self.answer):
            self.answer = int(self.answer)

        self.answer = str(self.answer)
        self.question_text = f"What is {self.num_1} {operation} {self.num_2}?"

    def multiplication_mode(self):
        operation = "x"
        self.num_1 = random.randint(multiplication_settings[self.difficulty_type].min_1, multiplication_settings[self.difficulty_type].max_1)
        self.num_2 = random.randint(multiplication_settings[self.difficulty_type].min_2, multiplication_settings[self.difficulty_type].max_2)
        
        if self.difficulty_type == Difficulty.HARD:
            self.num_2 = self.num_2/4
            if self.num_2 == int(self.num_2): 
                self.num_2= int(self.num_2)

        self.answer = self.num_1 * self.num_2

        if self.answer == int(self.answer):
            self.answer = int(self.answer)

        self.answer = str(self.answer)
        self.question_text = f"What is {self.num_1} {operation} {self.num_2}? "

    def division_mode(self):
        operation = "÷"
        self.num_1 = random.randint(division_settings[self.difficulty_type].min_1, division_settings[self.difficulty_type].max_1)
        
        while self.num_1 == 0:
            self.num_1 = random.randint(division_settings[self.difficulty_type].min_1, division_settings[self.difficulty_type].max_1)

        self.num_2 = random.randint(division_settings[self.difficulty_type].min_2, division_settings[self.difficulty_type].max_2)

        if self.difficulty_type == Difficulty.HARD:
            self.num_2 = self.num_2/4
            if self.num_2 == int(self.num_2): 
                self.num_2= int(self.num_2)

        self.answer = self.num_2
        self.answer = str(self.answer)
        combined_num  = self.num_1 * self.num_2
        if combined_num == int(combined_num):
            combined_num = int(combined_num)

        self.question_text = f"What is {combined_num} {operation} {self.num_1}?"

    def exponent_mode(self):
        operation = "^"
        self.num_1 = random.randint(exponent_settings[self.difficulty_type].min_1, exponent_settings[self.difficulty_type].max_1)
        self.num_2 = random.randint(exponent_settings[self.difficulty_type].min_2, exponent_settings[self.difficulty_type].max_2)
        self.answer = self.num_1 ** self.num_2
        self.answer = str(self.answer)
        self.question_text = f"What is ({self.num_1}) {operation} {self.num_2}? "

    def algebra_mode(self):
        self.num_1 = random.randint(algebra_settings[self.difficulty_type].min_1, algebra_settings[self.difficulty_type].max_1)
        while self.num_1 == 0:
            self.num_1 = random.randint(algebra_settings[self.difficulty_type].min_1, algebra_settings[self.difficulty_type].max_1)

        self.num_2 = random.randint(algebra_settings[self.difficulty_type].min_2, algebra_settings[self.difficulty_type].max_2)
        self.num_3 = random.randint(algebra_settings[self.difficulty_type].min_2, algebra_settings[self.difficulty_type].max_2)

        self.operation = random.randint(1, 2)

        if self.operation == 1:
            operation = "+"
            result = (self.num_1 * self.num_2) + self.num_3

        elif self.operation == 2:
            operation = "-"
            result = (self.num_1 * self.num_2) - self.num_3

        self.answer = self.num_2
        self.answer = str(self.answer)
        self.question_text = f"Solve for 𝑥: {self.num_1}𝑥 {operation} {self.num_3} = {result}"

    def fraction_mode(self):
        self.operation = random.randint(1, 5)

        self.num_1 = 0
        self.num_2 = 0
        self.num_3 = 0
        self.num_4 = 0

        while self.num_2 == 0 or self.num_4 ==0 or self.num_3==0:
            self.num_1 = random.randint(fraction_settings[self.difficulty_type].min_1, fraction_settings[self.difficulty_type].max_1)
            self.num_2 = random.randint(fraction_settings[self.difficulty_type].min_2, fraction_settings[self.difficulty_type].max_2)
            self.num_3 = random.randint(fraction_settings[self.difficulty_type].min_1, fraction_settings[self.difficulty_type].max_1)
            self.num_4 = random.randint(fraction_settings[self.difficulty_type].min_2, fraction_settings[self.difficulty_type].max_2)

        fraction_1 = Fraction(numerator=self.num_1, denominator=self.num_2)
        fraction_2 = Fraction(numerator=self.num_3, denominator=self.num_4)
        print(fraction_1, fraction_2)

        if self.operation == 1:
            operation = "+"
            self.question_text = f"What is {self.num_1}/{self.num_2} {operation} {self.num_3}/{self.num_4}? " 
            print(fraction_1, fraction_2)
            self.answer = fraction_1 + fraction_2
            self.answer = str(self.answer)
            
        elif self.operation == 2:
            operation = "-"
            self.question_text = f"What is {self.num_1}/{self.num_2} {operation} {self.num_3}/{self.num_4}? " 
            self.answer = fraction_1 - fraction_2
            self.answer = str(self.answer)

        elif self.operation == 3:
            operation = "x"
            self.question_text = f"What is {self.num_1}/{self.num_2} {operation} {self.num_3}/{self.num_4}? " 
            self.answer = fraction_1 * fraction_2
            self.answer = str(self.answer)

        elif self.operation == 4:
            operation = "÷"
            self.question_text = f"What is {self.num_1}/{self.num_2} {operation} {self.num_3}/{self.num_4}? " 
            self.answer = fraction_1/fraction_2
            self.answer = str(self.answer)

        elif self.operation == 5:
            while math.gcd((self.num_1*self.num_2), (self.num_3*self.num_4)) == 1 or self.num_3*self.num_4 == 0 or self.num_1*self.num_2 == 0:
                self.num_1 = random.randint(-5, 7)
                self.num_3 = random.randint(-7, 5)
                print("COMMON DENOMINATOR", math.gcd((self.num_1*self.num_2), (self.num_3*self.num_4)))

            self.question_text = f"Simplify this fraction fully: {self.num_1*self.num_2}/{self.num_3*self.num_4}"
            self.answer = Fraction(numerator=(self.num_1*self.num_2), denominator= (self.num_3*self.num_4))
            self.answer = str(self.answer)


    def generate_question(self, game_type, difficulty_type):
        match game_type:
            case GameType.ADDITION:
                self.addition_mode()
            case GameType.SUBTRACTION:
                self.subtraction_mode()
            case GameType.MULTIPLICATION:
                self.multiplication_mode()
            case GameType.DIVISION:
                self.division_mode()
            case GameType.EXPONENTS:
                self.exponent_mode()
            case GameType.ALGEBRA:
                self.algebra_mode()
            case GameType.FRACTIONS:
                self.fraction_mode()
#=======================================================================================================================================
def write_user_data(data, edit_type, file_path):

    # Opens file path (USER.txt) and joins data using ,
    # Edit type determines whether the program is adding, reading or replacing the text file
    with open(file_path, edit_type) as file:
        for entry in data:
            line = ",".join(map(str, entry))
            #print(line)
            file.write(line + "\n")

    # Reads data by first checking whether the text file exists, if not return an empty list. If file exists, program will read the file using .readlines().
    # And is copied into the variable "lines". This variable is then split into many sub lists within one list.

def read_user_data(file_path):
    if not os.path.exists(file_path):
        return []
    with open(file_path, "r") as file:
        lines = file.readlines()
    return [line.strip().split(",") for line in lines]

#====================================================================================================================================================================

def score_menu(window_type, session_xp, combo, player_score, total_questions):
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

    highest_combo_label = Label(score_canvas, text= f"Your highest combo was {combo}.", bg = COLOUR_5, font=(CUSTOM_FONT, 20, "bold italic"), fg=COLOUR_1, width = 30, height = 1)
    highest_combo_label.pack()

    highest_combo_label = Label(score_canvas, text= f"XP GAINED: {session_xp}.", bg = COLOUR_5, font=(CUSTOM_FONT, 20, "bold italic"), fg=COLOUR_1, width = 30, height = 1)
    highest_combo_label.pack()

    submit_btn = Button(score_canvas, bg = COLOUR_4, font=(CUSTOM_FONT, 20, "bold italic"), text = "New game", fg=COLOUR_1, width = 30, height = 1, command = lambda: mode_menu(score_window))
    submit_btn.pack()

    submit_btn = Button(score_canvas, bg = COLOUR_5, font=(CUSTOM_FONT, 20, "bold italic"), text = "Home", fg=COLOUR_1, width = 30, height = 1, command = lambda: [score_window.destroy(), main_menu()])
    submit_btn.pack()

def save_session_data(window_type, test2):
        session_data = []
        user_file_name = f"{user_detail.username}"

        combo = str(test2.highest_combo)
        total_questions = str(test2.question_asked)
        player_score = str(test2.score)
        session_xp = str(test2.session_xp)
        game_played = "1"

        # Read user data.
        reading = read_user_data(user_file_name)

        if reading == []:
            best_session = session_xp
            best_combo = combo

            session_data.append([best_session, best_combo, session_xp, total_questions, player_score, game_played, user_detail.username])
            write_user_data(session_data, "a", user_file_name)

        # If there is data.
        elif not reading == []:

            # Updating user progress.
            total_xp = int(reading[0][2]) + int(session_xp)
            total_questions_asked = int(reading[0][3]) + int(total_questions)
            total_correct = int(reading[0][4]) + int(player_score)
            total_games_played = int(reading[0][5]) + 1

            testing_best_game = reading[0][0]
            testing_combo = reading[0][1]

            if int(session_xp) > int(session_xp[0][0]):
                testing_best_game = session_xp

            if int(combo) > int(reading[0][1]):
                testing_combo = combo

            session_data.append([testing_best_game, testing_combo, total_xp, total_questions_asked, total_correct, total_games_played, user_detail.username])

        write_user_data(session_data, "w", user_file_name)

        score_menu(window_type, session_xp, combo, player_score, total_questions)

def game_menu(window_type, difficulty_type, game_type):
    def next_question(game_type, window_type):
        if test2.question_asked >= QUESTIONS_PER_GAME:
            save_session_data(window_type, test2)

        else:
            test.generate_question(game_type, difficulty_type)
            login_title_label.config(text = f"{test.question_text}")

    def submit_answer(user_entry, test, test2):
        user_ans = user_entry.get()
        print( f"USER ANSWER: {user_ans}, MODEL ANSWER: {test.answer}")
        
        if user_ans == test.answer:
            answer_label.config(bg = COLOUR_4, text = f"Correct! The answer is {test.answer}")
            test2.score = test2.score + 1
            test2.question_asked = test2.question_asked + 1
            test2.combo = test2.combo + 1
            
            print(f"CURRENT XP: {test2.session_xp}")
            test2.session_xp = test2.session_xp + (CORRECT_ANS_XP + CORRECT_ANS_XP * test2.combo)
            print(f"XP GAINED: {CORRECT_ANS_XP} + {CORRECT_ANS_XP * test2.combo}")

            if test2.combo > test2.highest_combo:
                test2.highest_combo = test2.combo

            print(f"HIGHEST COMBO: {test2.highest_combo}")
            print(f"CURRENT COMBO: {test2.combo}")
            print(f"TOTAL XP GAINED: {test2.session_xp}\n")

            q_left_label.config(text = f"Questions remaining: {QUESTIONS_PER_GAME - test2.question_asked}")
            score_label.config(text = f"SCORE: {test2.score}/{QUESTIONS_PER_GAME}")
            live_label.config(text = f"COMBO: {test2.combo}")

        else:
            if test2.combo > test2.highest_combo:
                test2.highest_combo = test2.combo

            print(f"HIGHEST COMBO: {test2.highest_combo}")
            print(f"CURRENT COMBO: {test2.combo}")
            test2.combo = 0

            answer_label.config(bg = COLOUR_2, text = f"Wrong! The correct answer is {test.answer}")
            test2.question_asked = test2.question_asked + 1
            q_left_label.config(text = f"Questions remaining: {QUESTIONS_PER_GAME - test2.question_asked}")
            live_label.config(text = f"COMBO: {test2.combo}")

        user_entry.delete(0, END)        
        next_question(game_type, game_window)
    
    # ========================================================================================================================

    window_type.destroy()
    
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

    test = SimpleQuestion(game_type, difficulty_type)
    test2 = Player()
    next_question(game_type, game_window)
    
    submit_btn = Button(game_canvas, bg = COLOUR_5, font=(CUSTOM_FONT, 20, "bold italic"), text = "submit", fg=COLOUR_1, width = 30, height = 1, command = lambda: submit_answer(user_entry, test, test2))
    submit_btn.pack()

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
        file_data = read_user_data(USER_INFO)
        
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
                    break

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
    write_user_data(user_login_info, "a", USER_INFO)
    
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
    user_data = read_user_data(USER_INFO)
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

def profile_menu(window_type):
    window_type.destroy()
    
    user_file_name = f"{user_detail.username}"
    reading = read_user_data(user_file_name)

    if reading == []:
        print("no data found")

    # If there is data.
    elif not reading == []:
        # Updating user progress.
        reading = reading[0]

        user_xp = int(reading[2])
        accuracy = int(reading[3])
        correct = int(reading[4])

    profile_window = ctk.CTkToplevel(login_window)
    profile_window.geometry("1280x640")
    profile_window.configure (bg="#ffffff")
    profile_window.title("Maths Mania! | Gamemode Menu")

    # Import images
    img = tk.PhotoImage(file = "images/login_bg_test.png")
    quit = tk.PhotoImage(file = "images/quit.png")

    # Creates a background canvas and adds the background image to it, this image is expanded on the x and y axis so it fills the screen.
    mode_canvas = Canvas(profile_window, width = 1280, height = 640, bg="#ffffff")
    mode_canvas.pack(fill="both", expand=True)
    mode_canvas.create_image(0,0, image=img, anchor="nw")
    mode_canvas.image = img

    banner_frame = Frame(mode_canvas, width=500, height=150, bg="#590b93")
    win_banner_frame = mode_canvas.create_window((0,0), anchor= "nw", window=banner_frame)

    # Adds a banner at the top of the screen
    banner_label = Label(banner_frame, font = (CUSTOM_FONT_2, 35), text = ("Profile Menu"), fg="#f3e1ff", bg="#590b93")
    banner_label.pack(fill=("x"), expand=True, padx=500, pady=10)

    # ====================================================================================================================================================================================
    
    username_label = ctk.CTkLabel(mode_canvas, font=(CUSTOM_FONT_2, 35), text = (f"{user_detail.username}'s Statistics"), height=40, width=1228, corner_radius=20, fg_color="#ecc8ff", text_color="#650892")
    win_username_label = mode_canvas.create_window((29,94), anchor= "nw", window=username_label)

    # ====================================================================================================================================================================================

    questions_answered_frame = ctk.CTkFrame(mode_canvas, height=100, width=445, corner_radius=20, fg_color="#cb96fc")
    win_questions_answered = mode_canvas.create_window((29,152), anchor= "nw", window=questions_answered_frame)

    top_questions_answered_label = ctk.CTkLabel(mode_canvas, font=(CUSTOM_FONT_2, 27), text = (f"{reading[3]}"), fg_color="#cb96fc", text_color=COLOUR_1)
    win_questions_answered_label = mode_canvas.create_window((50,168), anchor= "nw", window=top_questions_answered_label)

    btm_questions_answered_label = ctk.CTkLabel(mode_canvas, font=(CUSTOM_FONT_2, 27), text = ("Questions Answered"), fg_color="#cb96fc", text_color="#530892")
    win_questions_answered_label = mode_canvas.create_window((50,168+30), anchor= "nw", window=btm_questions_answered_label)

    # ====================================================================================================================================================================================

    # best_score_label = Label(mode_canvas, bg = COLOUR_5, font = (CUSTOM_FONT, 20, "bold"), text = (f"BEST XP: {reading[0]}"), width = 75, height = 2)    
    # win_best_score_label = mode_canvas.create_window((0,50), anchor= "nw", window=best_score_label)

    # best_combo_label = Label(mode_canvas, bg = COLOUR_5, font = (CUSTOM_FONT, 20, "bold"), text = (f"BEST COMBO: {reading[1]}"), width = 75, height = 2)    
    # win_best_combo_label = mode_canvas.create_window((0,200), anchor= "nw", window=banner_label)

    # total_xp_label = Label(mode_canvas, bg = COLOUR_5, font = (CUSTOM_FONT, 20, "bold"), text = (f"TOTAL XP: {reading[2]}"), width = 75, height = 2)    
    # win_total_xp_label = mode_canvas.create_window((0,300), anchor= "nw", window=best_combo_label)

# total_questions_answered_label = Label(mode_canvas, bg = COLOUR_5, font = (CUSTOM_FONT, 20, "bold"), text = (f"QUESTIONS ANSWERED: {reading[3]}"), width = 75, height = 2)    
# win_total_total_questions_answered_label = mode_canvas.create_window((0,400), anchor= "nw", window=total_questions_answered_label)

    # total_correct_answers_label = Label(mode_canvas, bg = COLOUR_5, font = (CUSTOM_FONT, 20, "bold"), text = (f"CORRECT ANSWERS: {reading[4]}"), width = 75, height = 2)    
    # win_total_correct_answers_label = mode_canvas.create_window((0,500), anchor= "nw", window=total_correct_answers_label)

    # games_played_label = Label(mode_canvas, bg = COLOUR_5, font = (CUSTOM_FONT, 20, "bold"), text = (f"GAMES PLAYED: {reading[5]}"), width = 75, height = 2)    
    # win_games_played_label = mode_canvas.create_window((0,600), anchor= "nw", window=games_played_label)

    # accuracy_label = Label(mode_canvas, bg = COLOUR_5, font = (CUSTOM_FONT, 20, "bold"), text = (f"ACCURACY: {(correct/accuracy)*100}%"), width = 75, height = 2)    
    # win_accuracy_label = mode_canvas.create_window((0,700), anchor= "nw", window=accuracy_label)

    # user_level_label = Label(mode_canvas, bg = COLOUR_5, font = (CUSTOM_FONT, 20, "bold"), text = (f"LEVEL {(user_xp/XP_PER_LEVEL):.0f}"), width = 75, height = 2)    
    # win_user_level_label = mode_canvas.create_window((0,700), anchor= "nw", window=user_level_label)

    # # Creates a back_button, and calls for quit_program to destroy this window, then it calls the main_menu function to open the main menu.
    # quit_button = Button(mode_canvas, bg = COLOUR_1, command = lambda: [quit_program(profile_window), main_menu()], image = quit)    
    # win_quit_button = mode_canvas.create_window((1115,5), anchor= "nw", window=quit_button)
    # quit_button.image = quit

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

    setting_button = Button(main_canvas, bg = COLOUR_1, text="PLAY", font=(CUSTOM_FONT, 30, "bold"), fg = "white", image = settings, command= lambda: profile_menu(main_window))    
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

# Starts the program
main()