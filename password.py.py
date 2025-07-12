import tkinter as tk
from tkinter import *
import random
import string
import pyperclip

# Initialize window
root = Tk()
root.configure(bg='turquoise')  # Set background color
root.geometry("400x400")
root.resizable(30, 30)
root.title("Generate Password - BargainBeaute")  # Title of the window

# Variables
pass_str = StringVar()
pass_len = IntVar(value=12)  # default value

# Function to generate password
def generator():
    password = ''
    if pass_len.get() < 4:
        pass_str.set("Too short!")
        return
    # First 4 chars from different categories
    password += random.choice(string.ascii_uppercase)
    password += random.choice(string.ascii_lowercase)
    password += random.choice(string.digits)
    password += random.choice(string.punctuation)
    # Rest of the password
    for _ in range(pass_len.get() - 4):
        password += random.choice(string.ascii_letters + string.digits + string.punctuation)
    pass_str.set(password)

# Function to copy password to clipboard
def copy_password():
    pyperclip.copy(pass_str.get())

# Widgets
Label(root, text='BargainBeaute', font='calibri 15 bold', bg='green').place(relx=0.5, rely=0.9, anchor=CENTER)

Label(root, text='PASSWORD LENGTH', font='calibri 10 bold', bg='yellow').place(relx=0.5, rely=0.1, anchor=CENTER)
Spinbox(root, from_=8, to=32, textvariable=pass_len, width=15).place(relx=0.5, rely=0.15, anchor=CENTER)

Button(root, text="GENERATE PASSWORD", command=generator).place(relx=0.5, rely=0.3, anchor=CENTER)

Entry(root, textvariable=pass_str, width=30, justify='center').place(relx=0.5, rely=0.4, anchor=CENTER)

Button(root, text='RESET', command=lambda: pass_str.set('')).place(relx=0.5, rely=0.5, anchor=CENTER)

Button(root, text='COPY TO CLIPBOARD', bg='blue', fg='white', command=copy_password).place(relx=0.5, rely=0.6, anchor=CENTER)

# Run the main loop
root.mainloop()
