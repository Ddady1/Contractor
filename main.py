import time

import bcrypt
import os
import json
import tkinter as tk
from tkinter import ttk
from ctypes import windll
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
    db_var = tk.IntVar
    lb_subject = ttk.Label(root, text='Choose Database type:', foreground=text_color, font=('Ariel', 12, 'bold'))
    lb_subject.place(x=10, y=10)
    rdb_dbExcel = tk.Radiobutton(text='Secure Excel file', foreground=text_color, font=('Ariel', 11, 'bold'), variable=db_var, value=1)
    rdb_dbExcel.place(x=30, y=50)
    rdb_dbSqlite =tk.Radiobutton(text='SQLite DB', foreground=text_color, font=('Ariel', 11, 'bold'), variable=db_var, value=2)
    rdb_dbSqlite.place(x=30, y=90)
    rdb_dbDynamo = tk.Radiobutton(text='Dynamo DB', foreground=text_color, font=('Ariel', 11, 'bold'), variable=db_var, value=3)
    rdb_dbDynamo.place(x=30, y=130)





    root.mainloop()

# Main Win


def main_win(color):
    root =tk.Tk()
    root.title('Contractor')
    root.geometry('1500x900+150+50')
    root.resizable(False, False)
    root.mainloop()


windll.shcore.SetProcessDpiAwareness(1)
text_color = 'DodgerBlue4'
db_win(text_color)
#main_win(text_color)