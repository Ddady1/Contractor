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
# Text according to DB type

def db_explain_text(num):
    excel_text = 'An Excel secured file.'
    sqlite_text = 'SQLite database server.'
    dynamo_text = 'A free cloud database.'

    if num == 1:
        return excel_text
    elif num ==2:
        return sqlite_text
    else:
        return dynamo_text

# DB type window


def select_db_win(color):
    root = tk.Tk()
    root.title('Contractor - DataBase Type')
    root.geometry('450x350+350+150')
    root.resizable(False, False)
    img = Image.open('assets/DB_pic.png')
    img = img.resize((150, 150), Image.LANCZOS)
    img = ImageTk.PhotoImage(img)
    lb_db_pic = ttk.Label(root, image=img)
    lb_db_pic.place(x=250, y=20)
    db_var = tk.IntVar()
    lb_subject = ttk.Label(root, text='Choose Database type:', foreground=color, font=('Ariel', 12, 'bold'))
    lb_subject.place(x=10, y=10)
    rdb_dbExcel = tk.Radiobutton(root, text='Secure Excel file', variable=db_var, value=0, foreground=color, font=('Ariel', 11, 'bold'))
    rdb_dbExcel.place(x=30, y=50)
    lb_excel = tk.Label(root, text=db_explain_text(1), foreground=color, font=('Ariel', 11))
    lb_excel.place(x=53, y=73)
    rdb_dbSqlite = tk.Radiobutton(root, text='SQLite DB', variable=db_var, value=1, foreground=color, font=('Ariel', 11, 'bold'))
    rdb_dbSqlite.place(x=30, y=130)
    lb_sqlite = tk.Label(root, text=db_explain_text(2), foreground=color, font=('Ariel', 11))
    lb_sqlite.place(x=53, y=153)
    rdb_dbDynamo = tk.Radiobutton(root, text='Dynamo DB', variable=db_var, value=2, foreground=color, font=('Ariel', 11, 'bold'))
    rdb_dbDynamo.place(x=30, y=210)
    lb_dynamo = tk.Label(root, text=db_explain_text(3), foreground=color, font=('Ariel', 11))
    lb_dynamo.place(x=53, y=233)
    bt_cancel = tk.Button(root, text='Cancel', height=1, width=8, foreground=color, font=('Ariel', 11), command=root.quit)
    bt_cancel.place(x=250, y=290)
    bt_next = tk.Button(root, text='Next', height=1, width=8, foreground=color, font=('Ariel', 11), command=lambda: [root.quit, input_db_win(text_color)])
    bt_next.place(x=350, y=290)

    root.mainloop()


def input_db_win(color):
    root = tk.Tk()
    root.title('Contractor - Database Setup')
    root.geometry('450x350+350+150')
    root.resizable(False, False)

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
#main_win(text_color)
select_db_win(text_color)
