from Zoom import *
from tkinter import *
import pandas as pd

# for importing data from csv file
df = pd.read_csv('meetingschedule.csv')
df_new = pd.DataFrame(df)

# for extracting the path
pt = open('path.txt', 'r+')
pth = pt.readline()
pth = pth.replace('/', '\\\\')

root = Tk()
root.title('Online Classes Automation')
root.geometry('500x500')

menu = Menu(root)


def end():
    root.destroy()


menu.add_cascade(label='Exit', command=end)
root.config(menu=menu)

aut = 'As you start the automation \nEvery thing will go under a process.\nSo dont press any button just minimize it'
lb2 = Label(root, text=aut, fg='red')
lb2.grid(column=0, row=0)

lb0 = Label(root, text='Your Currnt Path for ZOOM app is :\n'+pth)
lb0.grid(column=0, row=2)

lb = Label(root, text=df.head())
lb.grid(column=0, row=1)

l = Label(
    root, text='', font='50')
l.grid(column=0, row=5)

lb3 = Label(
    root, text='Add Zoom App Path in "path.txt" file. \n\n'
    'To get path right click on ZOOM\nclick on "Open File Location"\n'
    'Copy Path from above and past it in "path.txt file"\n', fg='blue', font='40')
lb3.grid(column=0, row=6)

lb3 = Label(
    root, text='Add Meeting Details in "meetingsschedule.csv" file.', font='50')
lb3.grid(column=0, row=7)

lb3 = Label(
    root, text='Add time in format: hh:mm,\n Ex. - 13:00 for 1 PM', font='40')
lb3.grid(column=0, row=8)


def clicked():
    button.configure(text='Stop Automation', command=end)
    automate()


button = Button(root, text='Run Automation',
                command=clicked, background='orange',)
button.grid(column=0, row=2)


root.mainloop()
