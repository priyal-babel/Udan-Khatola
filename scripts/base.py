import tkinter as tk
from tkinter import *
from fullScreen import FullScreenApp
from registration import register


top = Tk()
top.title("Airline Reservation System")
app = FullScreenApp(top)
background_image = PhotoImage(file="src/bkg.png")

def userRegister():
    register()

background_label = Label(top, image=background_image)
background_label.place(x=0, y=0, relwidth=1, relheight=1)

 
but1 = Button(
    top,
    bd=0,
    relief="groove",
    compound=tk.CENTER,
    bg="white",
    fg="black",
    activeforeground="pink",
    activebackground="white",
    font="arial 12",
    text="Login/Register",
    pady=10,
    borderwidth = 10,
    height = 1,
    width=30,
    command = userRegister
    )
 
but1.place(x=100,y=100)
but2 = Button(
    top,
    bd=0,
    relief="groove",
    compound=tk.CENTER,
    bg="white",
    fg="black",
    activeforeground="pink",
    activebackground="white",
    font="arial 12",
    text="Book a ticket",
    pady=10,
    borderwidth = 10,
    height = 1,
    width=30
    )
 
but2.place(x=100,y=200)

but3 = Button(
    top,
    bd=0,
    relief="groove",
    compound=tk.CENTER,
    bg="white",
    fg="black",
    activeforeground="pink",
    activebackground="white",
    font="arial 12",
    text="Web Checkin",
    pady=10,
    borderwidth = 10,
    height = 1,
    width=30
    )
 
but3.place(x=100,y=300)
top.mainloop()
