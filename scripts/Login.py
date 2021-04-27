import MySQLdb
from configure import user, password
import tkinter as tk
from tkinter import *
from PIL import ImageTk

con = MySQLdb.connect(host='localhost', user= user, password= password, database="airline_reservation")
cursor = con.cursor()
#str = 'create database airline_reservation'
#cursor.execute(str)

class Login:
    def __init__(self,root):
        self.root = root
        self.root.title("Login System - Airline Booking System")
        self.root.geometry("400x400")

        self.email = StringVar()
        self.passwor = StringVar()

        self.buttons(root)
        
    def isFormEmpty(self):
        if(self.email.get() == '' or self.passwor == ''):
            return True

    def buttons(self, root):
        label_0 = Label(root, text="Login", width=20, font=("bold", 20))
        label_0.place(x=50, y=50)

        label_3 = Label(root, text="Email", width=20, font=("bold", 10))
        label_3.place(x=25, y=150)
        entry_3 = Entry(root, width=30, textvar=self.email)
        entry_3.place(x=150, y=150)
        
        label_6 = Label(root, text="Password",
                        width=20, font=("bold", 10))
        label_6.place(x=25, y=250)
        entry_6 = Entry(root, width=30,textvar=self.passwor)
        entry_6.place(x=150, y=250)

        Button(root, text='Submit', width=20, height=2, bg='brown', fg='white', command=lambda: self.database(top)).place(x=180, y=530)

root = Tk()
obj = Login(root)
root.mainloop()
