import tkinter as tk 
from tkinter import *
from tkinter import ttk, messagebox
import random
import os
from PIL import Image, ImageTk
from collections import namedtuple

def start_menu():
    start_window = Tk()
    start_window.geometry("1280x640")
    start_window.configure (bg="#584353")
    start_window.title("Maths Mania! | Home Menu")
    
    icon = tk.PhotoImage(file = "main_bg.png")
    #image_label = Label(start_window, image=icon).pack(pady = 20)
    
    test_canvas = Canvas(start_window, width = 1280, height = 640, bg="purple")
    test_canvas.pack()
    test_canvas.create_image(0,0, image=icon, anchor="nw")

    back_button = Button(bg = "#114114", text="Quit", font=("arial", 27, "bold"), height = 2, width = 8, command = quit).pack(side=LEFT, padx=(20,0))

    start_window.mainloop()

start_menu()