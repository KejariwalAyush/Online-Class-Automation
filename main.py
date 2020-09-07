from tkinter import *
import pandas as pd
from Zoom import *

df = pd.read_csv('meetingschedule.csv')
df_new = pd.DataFrame()

root = Tk()
root.title('Online Classes Automation')
root.geometry('400x300')

lb = Label(root, text=df)
lb.grid(column=0, row=0)
# lb.pack()

button = Button(root, text='Run Automation',
                command=automate, background='orange',)
button.grid(column=0, row=1)
# button.pack()


button1 = Button(root, text='Exit Automation',
                 command=terminate, background='grey',)
button1.grid(column=1, row=1)
# button1.pack()


root.mainloop()


# import tkinter as tk

# root = tk.Tk()

# canvas1 = tk.Canvas(root, width=300, height=300)
# canvas1.pack()


# def hello():
#     label1 = tk.Label(root, text='Hello World!', fg='green',
#                       font=('helvetica', 12, 'bold'))
#     canvas1.create_window(150, 200, window=label1)


# # menu = tk.Menu()
# # file = tk.Menu(menu)
# # file.add_command(label='Set Path of Zoom', command=exit())
# # menu.add_cascade(label='File', menu=file)
# button1 = tk.Button(text='Click Me', command=hello, bg='brown', fg='white')
# canvas1.create_window(150, 150, window=button1)

# root.mainloop()
