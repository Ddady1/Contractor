from tkinter import ttk
from PIL import ImageTk, Image
import tkinter as tk

root = tk.Tk()
root.title('Contractor - DataBase Type')
root.geometry('450x350+350+150')
root.resizable(False, False)
img = Image.open('assets/DB_pic.png')
img = img.resize((30, 30), Image.LANCZOS)
img = ImageTk.PhotoImage(img)
lb_db_pic = ttk.Label(root, image=img)
lb_db_pic.place(x=300, y=50)

root.mainloop()

