from tkinter import ttk

import tkinter as tk
my_w = tk.Tk()
my_w.geometry("500x120")  # Size of the window

r1_v = tk.IntVar()

r1 = tk.Radiobutton(my_w, text='Passed', variable=r1_v, value=0, foreground='Blue', font=('Ariel', 11, 'bold'))
r1.grid(row=1,column=1,padx=30,pady=30)

r2 = tk.Radiobutton(my_w, text='Failed', variable=r1_v, value=1, foreground='Blue', font=('Ariel', 11, 'bold'))
r2.grid(row=1,column=2)

r3 = tk.Radiobutton(my_w, text='Appearing', variable=r1_v, value=2, foreground='Blue', font=('Ariel', 11, 'bold'))
r3.grid(row=1,column=3)

my_w.mainloop()  # Keep the window open

