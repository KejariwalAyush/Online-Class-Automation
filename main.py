from tkinter import *
import pandas as pd
from Zoom import *

df = pd.read_csv('meetingschedule.csv')
df_new = pd.DataFrame(df)

# print(df_new.loc[])


def addMeeting():
    root1 = Tk()
    root1.title('Enter Meeting Details')
    # width x height
    root1.geometry('400x200')
    # root1.mainloop()

    # 1st box meeting id
    lbl = Label(root1, text='Meeting ID : ')
    lbl.grid(column=0, row=0)
    mid = Entry(root1, width=10)
    mid.grid(column=1, row=0)

    # 2nd box passkey
    lbl1 = Label(root1, text='PassCode : ')
    lbl1.grid(column=0, row=1)
    pk = Entry(root1, width=10)
    pk.grid(column=1, row=1)

    # 3rd box Time
    lbl2 = Label(root1, text='Time : ')
    lbl2.grid(column=0, row=2)
    tm = Entry(root1, width=10)
    tm.grid(column=1, row=2)
    lbl3 = Label(
        root1, text='Add time in format: hh:mm,\n Ex. - 13:00 for 1 PM', fg='green')
    lbl3.grid(column=0, row=3)

    def clicked():
        res1 = "Meeting ID : " + mid.get()
        res2 = "Passkey : " + pk.get()
        res3 = "Time : " + tm.get()
        print(res1)
        print(res2)
        print(res3)
        # btn.config(text=res1)
        root1.destroy()

    def cancel():
        root1.destroy()
    # button widget with red color text inside
    btn = Button(root1, text="Save",
                 fg="red", command=clicked)
    btn.grid(column=0, row=4)

    btn2 = Button(root1, text="Cancel",
                  fg="grey", command=cancel)
    btn2.grid(column=1, row=4)
    # btn = Button(root1, text="Click me",
    #              fg="red", command=clicked)
    # btn.grid(column=2, row=1)
    # exit()


def deleteMeeting():
    root2 = Tk()
    root2.title('Delete Meeting Details')
    # width x height
    root2.geometry('400x200')
    # root1.mainloop()
    w = Label(root2, text='GeeksForGeeks', font="50")
    w.pack()

    Checkbutton1 = IntVar()
    Checkbutton2 = IntVar()
    Checkbutton3 = IntVar()

    Button1 = Checkbutton(root2, text="Tutorial",
                          variable=Checkbutton1,
                          onvalue=1,
                          offvalue=0,
                          height=2,
                          width=10)

    Button2 = Checkbutton(root2, text="Student",
                          variable=Checkbutton2,
                          onvalue=1,
                          offvalue=0,
                          height=2,
                          width=10)

    Button3 = Checkbutton(root2, text="Courses",
                          variable=Checkbutton3,
                          onvalue=1,
                          offvalue=0,
                          height=2,
                          width=10)

    Button1.pack()
    Button2.pack()
    Button3.pack()

    def clicked():
        print(Checkbutton1)
        print(Checkbutton2)
        print(Checkbutton3)
        # btn.config(text=res1)
        root2.destroy()

    def cancel():
        root2.destroy()
    # button widget with red color text inside
    btn = Button(root2, text="Delete",
                 fg="red", command=clicked)
    # btn.grid(column=0, row=4)
    btn.pack()

    btn2 = Button(root2, text="Cancel",
                  fg="grey", command=cancel)
    # btn2.grid(column=1, row=4)
    btn2.pack()


root = Tk()
root.title('Online Classes Automation')
root.geometry('400x300')

menu = Menu(root)


file = Menu(menu)
file.add_command(label='New Meeting', command=addMeeting)
file.add_command(label='Delete Meeting', command=deleteMeeting)
menu.add_cascade(label='File', menu=file)

# item = Menu(menu)
# item.add_command(label='Exit', command=exit)
menu.add_cascade(label='Exit', command=exit)
root.config(menu=menu)

aut = 'As you start the automation \nEvery thing will go under a process.\nSo dont press any button just minimize it'
lb2 = Label(root, text=aut, fg='red')
lb2.grid(column=0, row=0)

lb = Label(root, text=df.head())
lb.grid(column=0, row=1)
# lb.pack()


def clicked():
    button.configure(text='Stop Automation', command=exit)
    x = automate()


button = Button(root, text='Run Automation',
                command=clicked, background='orange',)
button.grid(column=0, row=2)
# button.pack()
# button is clicked


# button1 = Button(root, text='Exit Automation',
#                  command=terminate, background='grey',)
# button1.grid(column=0, row=2)
# button1.pack()


root.mainloop()
