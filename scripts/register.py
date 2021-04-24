import tkinter as tk
from tkinter import *
from configure import user, password
import MySQLdb


top = Tk()
top.title("Airline Reservation System")
top.geometry("500x500")

first_name = StringVar()
last_name = StringVar()
email = StringVar()
number = StringVar()
Gender = IntVar()
age = StringVar()
passwor = StringVar()


def database():
    firstName = first_name.get()
    lastName = last_name.get()
    emailid = email.get()
    num = number.get()
    g = Gender.get()
    Age = age.get()
    passw = passwor.get()
    #con = sqlite3.connect('airline_reservation.db')
    con = MySQLdb.connect(host='localhost', user=user,
                      password=password, database = "airline_reservation")
    cursor = con.cursor()
    cursor.execute("INSERT INTO registration VALUES(%s,%s,%s,%s,%s,%s,%s)",
               (firstName, lastName, num, emailid, passw, g, Age,))
    con.commit()


label_0 = Label(top, text="Registration Form", width=20, font=("bold", 20))
label_0.place(x=100, y=23)

label_1 = Label(top, text="First Name", width=20, font=("bold", 10))
label_1.place(x=75, y=100)
entry_1 = Entry(top, width=30, textvar=first_name)
entry_1.place(x=210, y=100)

label_2 = Label(top, text="Last Name", width=20, font=("bold", 10))
label_2.place(x=75, y=150)
entry_2 = Entry(top, width=30, textvar=last_name)
entry_2.place(x=210, y=150)

label_3 = Label(top, text="Email", width=20, font=("bold", 10))
label_3.place(x=75, y=200)
entry_3 = Entry(top, width=30, textvar=email)
entry_3.place(x=210, y=200)

label_4 = Label(top, text="Phone Number", width=20, font=("bold", 10))
label_4.place(x=75, y=250)
entry_4 = Entry(top, width=20, textvar=number)
entry_4.place(x=210, y=250)

label_5 = Label(top, text="Gender", width=20, font=("bold", 10))
label_5.place(x=75, y=300)
Radiobutton(top, text="Male", padx=5, variable=Gender,
            value=1).place(x=205, y=300)
Radiobutton(top, text="Female", padx=20,
            variable=Gender, value=2).place(x=260, y=300)

label = Label(top, text="Age", width=20, font=("bold", 10))
label.place(x=75, y=350)
entry = Entry(top, textvar=age)
entry.place(x=210, y=350)

label_6 = Label(top, text="Password",
                width=20, font=("bold", 10))
label_6.place(x=75, y=400)
entry_6 = Entry(top, textvar=passwor)
entry_6.place(x=210, y=400)

Button(top, text='Submit', width=20, bg='brown',
       fg='white', command=database).place(x=180, y=450)
# it is use for display the registration form on the window
top.mainloop()
