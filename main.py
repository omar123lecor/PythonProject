from tkinter import *
from tkinter import messagebox
import numpy
import time
window = Tk()
icon1 = PhotoImage(file="C:\\Users\pc\Downloads\icons\lock.png")
window.iconphoto(True, icon1)
window.title('Login')
window.geometry('925x500')
window.resizable(False, False)
img = PhotoImage(file="C:\\Users\pc\Downloads\image2.png")
window.configure(bg='#fff')
Label(window, image=img, bg='white').place(x=50, y=65)
frame = Frame(window, width=350, height=350, bg='white')
frame.place(x=480, y=70)
heading = Label(frame, text='Sign in', fg='#07f572', bg='white', font=('Microsoft Yahei UI Light', 23, 'bold'))
heading.place(x=100, y=5)
imag2 = PhotoImage(file="C:\\Users\pc\Downloads\health.png")
def action():
    frame3.tkraise()

def myinfo():
    if weight.get()=="" or height.get()=="" or week1.get()=="" or week2.get()=="" or week3.get()=="" or week4.get()=="":
        messagebox.showinfo(message="Please complete all the form",title="Empty data")
    else:
        about_button = Button(frame2, text='MyInfo', font=('Arial', 17, 'bold'), border=0, bd=4, command=accct)
        about_button.place(x=110, y=26)

def accct():
    frame4.tkraise()
    frame4.place(x=0, y=110)

def account():
    global frame3
    global frame4
    global frame2
    global image2
    global image3
    global frame5
    global weight,height,week1,week2,week3,week4
    sub = Toplevel()
    image2 = PhotoImage(file="C:\\Users\pc\Downloads\\trees.png")
    image3 = PhotoImage(file="C:\\Users\pc\Downloads\health.png")
    sub.title('Welcome to fit tracker app')
    sub.geometry('700x500')
    sub.config(bg='white')
    sub.resizable(False, False)
    icon = PhotoImage(file="C:\\Users\pc\Downloads\icons\sport.png")
    window.iconphoto(True, icon)
    frame5 = Frame(sub, width=700,height=4,bg='green')
    frame2 = Frame(sub, width=350, height=102, bg='#c7e9f0')
    Label(sub, image=image2, bg='white').place(x=550, y=0)
    Label(sub, image=image3, bg='white').place(x=15, y=15)
    frame3 = Frame(sub, width=750, height=500, bg='#e6ccff')
    frame4 = Frame(sub, width=750, height=500, bg='blue')
    home_button = Button(frame2, text='Home', font=('Arial', 17, 'bold'), border=0, bd=4, command=action)
    frame2.place(x=170, y=0)
    frame5.place(x=0,y=104)
    home_button.place(x=10, y=26)
    frame3.place(x=0, y=110)
    Label(frame3,text="Welcome to Fit Tracker Up! Our aim is to help users stay informed about their body's health."
                      " To achieve this, we require some information from you?",font=('Arial', 12, 'bold'),bg='#e6ccff').place(x=0,y=0)
    Label(frame3, text=" To achieve this, we require some information from you?", font=('Arial', 12, 'bold'),
          bg='#e6ccff').place(x=0, y=20)
    Label(frame3,text="Your gender : ",fg='blue',bg='#e6ccff',font=('Arial',14,'bold')).place(x=10,y=55)
    x = StringVar()
    Radiobutton(frame3,text='Male',variable=x,value='male',bg='#e6ccff',font=('Arial',14,'bold')).place(x=200,y=55)
    Radiobutton(frame3,text='Female',variable=x,value='Female',bg='#e6ccff',font=('Arial',14,'bold')).place(x=280,y=55)
    Label(frame3,text="Your Weight en KG: ",fg='blue',bg='#e6ccff',font=('Arial',14,'bold')).place(x=10,y=95)
    weight = Entry(frame3,font=('Arial',14,'bold'),width=5)
    weight.place(x=260, y=95)
    Label(frame3, text="Your height en Cm: ", fg='blue', bg='#e6ccff', font=('Arial', 14, 'bold')).place(x=10, y=135)
    height = Entry(frame3,font=('Arial',14,'bold'),width=5)
    height.place(x=260,y=135)
    Label(frame3, text="Your weight during the last month :", fg='blue', bg='#e6ccff', font=('Arial', 13, 'bold')).place(x=90, y=170)
    Label(frame3,text="week1 : ",fg='black', bg='#e6ccff', font=('Arial', 13, 'bold')).place(x=120,y=200)
    week1=Entry(frame3,font=('Arial',13,'bold'),width=5)
    week1.place(x=190,y=200)
    Label(frame3, text="week2 : ", fg='black', bg='#e6ccff', font=('Arial', 13, 'bold')).place(x=120, y=240)
    week2 = Entry(frame3, font=('Arial', 13, 'bold'), width=5)
    week2.place(x=190, y=240)
    Label(frame3, text="week3 : ", fg='black', bg='#e6ccff', font=('Arial', 13, 'bold')).place(x=120, y=280)
    week3 = Entry(frame3, font=('Arial', 13, 'bold'), width=5)
    week3.place(x=190, y=280)
    Label(frame3, text="week4 : ", fg='black', bg='#e6ccff', font=('Arial', 13, 'bold')).place(x=120, y=320)
    week4 = Entry(frame3,font=('Arial', 13, 'bold'), width=5)
    week4.place(x=190, y=320)
    submit = Button(frame3,text='submit',bg='#e6ccff',bd='2',font=('Arial', 14, 'bold'),command=myinfo)
    submit.place(x=450,y=330)

def sign_in():
    if user.get() == 'omar' and code.get() == 'sabor':
        account()
    elif user.get() in ["Username", ''] or code.get() in ['Password', '']:
        messagebox.showinfo(title='erreu', message="Donner manquant")
    else:
        messagebox.showerror(title='incorrect info', message='mot de passe ou username incorrect')


def on_enter(a):
    user.delete(0, 'end')


def on_leave(a):
    name = user.get()
    if name == '':
        user.insert(0, 'Username')


def on_enterr(a):
    code.delete(0, 'end')
    code.config(show='*')


def on_leavee(a):
    name = code.get()
    if name == '':
        code.config(show='')
        code.insert(0, 'Password')


##################-----------------------------
user = Entry(frame, width=25, fg='black', border=0, bg='white', font=('Microsoft Yahei UI Light', 11))
user.place(x=30, y=80)
user.insert(0, "Username")
user.bind('<FocusIn>', on_enter)
user.bind('<FocusOut>', on_leave)
Frame(frame, width=295, height=2, bg='black').place(x=25, y=107)
##################-----------------------------
code = Entry(frame, width=25, fg='black', border=0, bg='white', font=('Microsoft Yahei UI Light', 11))
code.place(x=30, y=150)
code.insert(0, "Password")
code.bind('<FocusIn>', on_enterr)
code.bind('<FocusOut>', on_leavee)
Frame(frame, width=295, height=2, bg='black').place(x=25, y=180)
##################-----------------------------
Button(frame, width=39, pady=7, text='Sign in', bg='#07f572', fg='white', border=0, command=sign_in).place(x=35, y=204)
label = Label(frame, text="Don't have an account?", fg='black', bg='white', font=('Microsoft Yahei UI Light', 9))
label.place(x=75, y=270)
sign_up = Button(frame, width=6, text='Sign up', border=0, bg='white', cursor='hand2', fg='#57a1f8')
sign_up.place(x=215, y=270)
##################-----------------------------
window.mainloop()
