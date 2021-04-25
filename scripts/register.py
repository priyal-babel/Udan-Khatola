import tkinter as tk
from tkinter import Tk, Label, messagebox, StringVar, IntVar, Entry, Radiobutton, Button, Listbox
from configure import user, password
import MySQLdb


top = Tk()
top.title("Airline Reservation System")
top.geometry("500x600")

first_name = StringVar()
last_name = StringVar()
email = StringVar()
number = StringVar()
Gender = IntVar()
age = StringVar()
passwor = StringVar()


def isFormEmpty():
    if(first_name.get() == '' or last_name.get() == '' or email.get() == '' or number.get() == '' or Gender.get() == 0 or age.get() == '' or passwor == ''):
        return True


def database():
    check = True
    firstName = first_name.get()
    lastName = last_name.get()
    emailid = email.get()
    num = number.get()
    g = Gender.get()
    Age = age.get()
    passw = passwor.get()

    if isFormEmpty() == True:
        messagebox.showerror("Form Empty", "Please enter all details!")
        return
    #con = sqlite3.connect('airline_reservation.db')
    try:
        con = MySQLdb.connect(host='localhost', user=user,
                              password=password, database="airline_reservation")
        cursor = con.cursor()
        command = 'SELECT emailid FROM registration'
        cursor.execute(command)
        registered_email = cursor.fetchall()
        for ids in registered_email:
            if(emailid == ids[0]):
                check = False
        if(check):
            if(len(passw) < 8):
                messagebox.showwarning(
                    "Change password", "Password too short!")
                return
            elif(len(passw) > 20):
                messagebox.showwarning("Change password", "Password too long!")
                return
            elif(len(passw) >= 8 and len(passw) <= 20):
                a = b = c = d = 0
                for p in passw:
                    if (p.islower()):
                        a = 1
                    if (p.isdigit()):
                        b = 1
                    if (p.isupper()):
                        c = 1
                    if (p == "$" or p == "#" or p == "@"):
                        d = 1
                if(a != 1):
                    messagebox.showwarning(
                        "Change password", "Password should contain lower characters!")
                    return
                if(c != 1):
                    messagebox.showwarning(
                        "Change password", "Password should contain upper characters!")
                    return
                if(b != 1):
                    messagebox.showwarning(
                        "Change password", "Password should contain a digit!")
                    return
                if(d != 1):
                    messagebox.showwarning(
                        "Change password", "Password should contain $ or # or @!")
                    return
            else:
                cursor.execute("INSERT INTO registration VALUES(%s,%s,%s,%s,%s,%s,%s)",
                               (firstName, lastName, num, emailid, passw, g, Age,))
                con.commit()
                messagebox.showinfo("Registration successful",
                                    "You have been registered successfully!")
                top.destroy()
        else:
            messagebox.showwarning("Oops", "Email id already registered!")
            top.destroy()
            import register
    except Exception as e:
        print(e)
        messagebox.showerror("Error", "Error\nUnable to register.")


class BLabel(object):
    b = "•"

    def __init__(self, master):
        import tkinter as tk
        self.l = tk.Label(master)

    def add_option(self, text):
        if self.l.cget("text") == "":
            self.l.config(text=self.b+" "+text)
        else:
            self.l.config(text=self.l.cget("text") + "\n" + self.b + " "+text)


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

Lb1 = BLabel(master=top)
Lb1.add_option("At least 1 letter between [a-z]")
Lb1.add_option("At least 1 number between [0-9]")
Lb1.add_option("At least 1 letter between [A-Z]")
Lb1.add_option("At least 1 character from [$#@]")
Lb1.add_option("Minimum length of password: 8")
Lb1.add_option("Maximum length of password: 15")
Lb1.l.place(x=155, y=430)

Button(top, text='Submit', width=20, height=2, bg='brown',
       fg='white', command=database).place(x=180, y=530)
# it is use for display the registration form on the window
top.mainloop()
