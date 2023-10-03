import time

import bcrypt
import os
import json
import tkinter as tk
from tkinter import ttk
from ctypes import windll
from PIL import ImageTk, Image
from tkinter.messagebox import showinfo, askyesno

def write_pass_file(pwd):
    path = 'assets/secret.json'
    if os.path.isfile(path):
        f = open(path)
        data = json.load(f)
        return data
    pwd = pwd.decode()
    #dict = {}
    dict['password'] = pwd
    js_object = json.dumps(dict, indent=4)
    with open('assets/secret.json', 'w') as f:
        f.write(js_object)


def encrypt(password):
    password = password.encode('utf-8')
    hashed = bcrypt.hashpw(password, bcrypt.gensalt(10))
    return hashed


def check(passen, stren):
    check = passen.encode('utf-8')
    if bcrypt.checkpw(check, stren):
        print('OK')
    else:
        print('FALSE')

'''pawss = input('pass: ')

stren = encrypt(pawss)
write_pass_file(stren)

check(input('check pass: '), stren)'''

# DB type window


def db_win(color):
    root = tk.Tk()
    root.title('Contractor - DataBase Type')
    root.geometry('450x350+350+150')
    root.resizable(False, False)
    img = Image.open('assets/DB_pic.png')
    img = img.resize((30, 30), Image.LANCZOS)
    img = ImageTk.PhotoImage(img)
    lb_db_pic = ttk.Label(image=img)
    lb_db_pic.place(x=100, y=50)
    db_var = tk.IntVar()
    lb_subject = ttk.Label(root, text='Choose Database type:', foreground=color, font=('Ariel', 12, 'bold'))
    lb_subject.place(x=10, y=10)
    rdb_dbExcel = tk.Radiobutton(root, text='Secure Excel file', variable=db_var, value=0, foreground=color, font=('Ariel', 11, 'bold'))
    rdb_dbExcel.place(x=30, y=50)
    rdb_dbSqlite = tk.Radiobutton(root, text='SQLite DB', variable=db_var, value=1, foreground=color, font=('Ariel', 11, 'bold'))
    rdb_dbSqlite.place(x=30, y=90)
    rdb_dbDynamo = tk.Radiobutton(root, text='Dynamo DB', variable=db_var, value=2, foreground=color, font=('Ariel', 11, 'bold'))
    rdb_dbDynamo.place(x=30, y=130)

    root.mainloop()

# Main Win


def main_win(color):
    root = tk.Tk()
    root.title('Contractor')
    root.geometry('1500x900+150+50')
    root.resizable(False, False)
    root.mainloop()


windll.shcore.SetProcessDpiAwareness(1)
text_color = 'DodgerBlue4'
main_win(text_color)
db_win(text_color)
