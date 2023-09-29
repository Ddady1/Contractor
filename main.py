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
windll.shcore.SetProcessDpiAwareness(1)
text_color = 'DodgerBlue4'
# DB type window

root = tk.Tk()
root.title('Contractor - DataBase Type')
root.geometry('450x350+350+150')
root.resizable(False, False)
#.iconbitmap('assets/reminder.ico')

# DB type text

main_label = ttk.Label(root, text='Choose your Database type', foreground=text_color, font=('Ariel', 14, 'bold'))
main_label.place(x=100, y=10)






root.mainloop()