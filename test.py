from tkinter import ttk

import tkinter as tk

root = tk.Tk()
root.title('Contractor - DataBase Type')
root.geometry('450x350+350+150')
root.resizable(False, False)
db_var = tk.IntVar()
lb_subject = ttk.Label(root, text='Choose Database type:')
lb_subject.place(x=10, y=10)
rdb_dbExcel = tk.Radiobutton(root, text='Secure Excel file', variable=db_var, value=0, foreground='Blue',
                             font=('Ariel', 11, 'bold'))
rdb_dbExcel.place(x=30, y=50)
rdb_dbSqlite = tk.Radiobutton(root, text='SQLite DB', variable=db_var, value=1, foreground='Blue',
                              font=('Ariel', 11, 'bold'))
rdb_dbSqlite.place(x=30, y=90)
rdb_dbDynamo = tk.Radiobutton(root, text='Dynamo DB', variable=db_var, value=2, foreground='Blue',
                              font=('Ariel', 11, 'bold'))
rdb_dbDynamo.place(x=30, y=130)

root.mainloop()

