from tkinter import *
import shutil         
import os
from unittest.mock import patch
from tkinter import filedialog
from tkinter import messagebox as mb

import os
import pyautogui as pag
from tkinter import *
from time import *

App = Tk()

Cpath = ''

text = Text(App)
text.pack(fill=BOTH)

def getTextInput():
    retrieve = App.text.get(1.0, END+"-1c")
    print(retrieve)

def Open():
    path = filedialog.askopenfilename()
    with open(path, 'r') as file:
        code = file.read()
        text.delete('1.0', END)
        text.insert('1.0', code)
        global Cpath
        Cpath = path

text.selection_get

def saveAs():
    global Cpath
    if Cpath == '':
        path = filedialog.asksaveasfilename(filetypes=[('Text files','*.txt')])
    else:
        path = Cpath
    with open(path, 'w') as file:
        code = text.get('1.0', END)
        file.write(code)

def New():
    text.delete('1.0', END)

App.title("Pocket Note")
App.iconbitmap("C://Users//Andrew//Desktop//Main//Codage//Python//Saison 1//Projet//book.ico")
App.configure(bg='#F9F9F9')
App.geometry('1000x500')

menubar = Menu(App)
file = Menu(menubar, tearoff=0)
menubar.add_cascade(label='File', menu=file)
file.add_command(label="New", command=New)
file.add_command(label="Open", command=Open)
file.add_command(label="Save As", command=saveAs)


edit = Menu(menubar, tearoff=0)
menubar.add_cascade(label="Edit", menu = edit)
edit.add_command(label="Cut")
edit.add_command(label="Copy")
edit.add_command(label="Past")
edit.add_command(label="Select All")

help = Menu(menubar, tearoff=0)
menubar.add_cascade(label="Help", menu = help)
help.add_command(label="About...")

menubar.add_cascade(label="Quit", command=App.quit)

App.config(menu = menubar)


App.mainloop()


