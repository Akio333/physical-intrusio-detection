from tkinter import *
import tkinter.messagebox
import os
import sys
import datetime

root = Tk()
root.geometry('600x600')
root.resizable(False, False)

frame = Frame(root, relief=RIDGE, borderwidth=5)
frame.pack(fill=BOTH, expand=1)
root.title('PIDS')
frame.config(background='light blue')
label = Label(frame, text="PIDS", bg='light blue', font=('Arial bold', 50))
label.pack(side=TOP)

#filename = PhotoImage(file="demo.png")
background_label = Label(frame, background='black')
background_label.pack(side=TOP)


def Contri():
    tkinter.messagebox.showinfo(
        "Contributors", "\n1.Sumukh Maduskar(172270)\n2.Suyog Mule(172271) \n3.Pankaj Masaye(162070) \n")


def anotherWin():
    tkinter.messagebox.showinfo("About", '\n Made Using\n-Tkinter In Python 3')


menu = Menu(root)
root.config(menu=menu)


subm2 = Menu(menu)

subm2.add_command(label="PIDS", command=anotherWin)
subm2.add_command(label="Contributors", command=Contri)


def exit_button():
    exit()


def a():
    now = datetime.datetime.now()
    if (now.hour >= 8 and now.hour < 20):
        os.chdir('/home/akio/project/pids/pids_gui/Face/')
        os.system('python main.py')

    else:
        os.chdir('/home/akio/project/pids/pids_gui/Person/')
        os.system('python detect_video.py')


def b():
    os.chdir('/home/akio/project/pids/pids_gui/Person/')
    os.system('python detect_video.py')


def c():
    os.chdir('/home/akio/project/pids/pids_gui/Face/')
    os.system('python main.py')


def d():
    print(e1.get())
    if str(e1.get()) == "":
        tkinter.messagebox.showinfo("Error", "Please Enter Name")
    else:
        os.chdir('/home/akio/project/pids/pids_gui/Face/')
        os.system('python main.py --mode="input" --name={}'.format(e1.get()))


e1 = Entry(root, font=('helvetica 15 bold'))
e1.pack()
e1.place(x=200, y=430)
but2 = Button(frame, padx=5, pady=5, width=25, bg='white', fg='black',
              relief=GROOVE, command=d, text='Add a new face', font=('helvetica 15 bold'))
but2.place(x=150, y=460)


but3 = Button(frame, padx=5, pady=5, width=15, bg='white', fg='black',
              relief=GROOVE, command=c, text='Face Recognition', font=('helvetica 15 bold'))
but3.place(x=25, y=500)


but4 = Button(frame, padx=5, pady=5, width=15, bg='white', fg='black',
              relief=GROOVE, command=b, text='Person Detection', font=('helvetica 15 bold'))
but4.place(x=210, y=500)

but5 = Button(frame, padx=5, pady=5, width=10, bg='white', fg='black',
              relief=RAISED, text='Exit', command=exit_button, font=('helvetica 15 bold'))
but5.place(x=400, y=500)

a()
root.mainloop()
