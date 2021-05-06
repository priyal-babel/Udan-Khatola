import tkinter as tk
from tkinter import Tk, Label, messagebox, StringVar, IntVar, Entry, Radiobutton, Button, Listbox, Toplevel, Checkbutton
from configure import user, password
import MySQLdb


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


class Register:
    def __init__(self):
        top = Toplevel()
        top.title("Registaration - Udan Khatola")
        top.geometry("500x650+400+25")

        self.first_name = StringVar()
        self.last_name = StringVar()
        self.email = StringVar()
        self.number = StringVar()
        self.Gender = IntVar()
        self.age = StringVar()
        self.passwor = StringVar()
        self.checkButton = IntVar()

        self.buttons(top)
        top.mainloop()

    def checkbox(self, root):
        self.check_value = self.checkButton.get()
        if self.check_value == 0:
            self.entry_6.configure(show="*")
        else:
            self.entry_6.configure(show="")

    def isFormEmpty(self):
        if(self.first_name.get() == '' or self.last_name.get() == '' or self.email.get() == '' or self.number.get() == '' or self.Gender.get() == 0 or self.age.get() == '' or self.passwor == ''):
            return True

    def database(self, top):
        check = True
        firstName = self.first_name.get()
        lastName = self.last_name.get()
        emailid = self.email.get()
        num = self.number.get()
        g = self.Gender.get()
        Age = self.age.get()
        passw = self.passwor.get()
        if self.isFormEmpty() == True:
            messagebox.showerror(master=top,title="Form Empty",message= "Please enter all details!")
            top.lift()
            return
        if '@' not in emailid:
            messagebox.showerror(master=top,title="Error",message= "Invalid Email")
            top.lift()
            return

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
                        master=top,title="Change password",message= "Password too short!")
                    top.lift()
                    return
                elif(len(passw) > 20):
                    messagebox.showwarning(
                        master=top,title="Change password",message= "Password too long!")
                    top.lift()
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
                            master=top,title="Change password",message= "Password should contain lower characters!")
                        top.lift()
                        return
                    if(c != 1):
                        messagebox.showwarning(
                            master=top,title="Change password",message= "Password should contain upper characters!")
                        top.lift()
                        return
                    if(b != 1):
                        messagebox.showwarning(
                            master=top,title="Change password",message= "Password should contain a digit!")
                        top.lift()
                        return
                    if(d != 1):
                        messagebox.showwarning(
                            master=top,title="Change password",message= "Password should contain $ or # or @!")
                        top.lift()
                        return

                    cursor.execute("INSERT INTO registration VALUES(%s,%s,%s,%s,%s,%s,%s)",
                                   (firstName, lastName, num, emailid, passw, g, Age,))
                    con.commit()
                    messagebox.showinfo(master=top,title="Registration successful",
                                        message="You have been registered successfully!")
                    top.destroy()
                    from login import Login
                    Login()
            else:
                messagebox.showwarning(
                    master=top,title="Oops",message= "Email id already registered!")
                top.destroy()
                Register()

        except Exception as e:
            print(e)
            messagebox.showerror(master=top,title="Error",message= "Error\nUnable to register.")
            top.lift()

    def buttons(self, top):
        label_0 = Label(top, text="Registration Form",
                        width=20, font=("bold", 20))
        label_0.place(x=100, y=23)

        label_1 = Label(top, text="First Name",
                        width=20, font=("bold", 10))
        label_1.place(x=75, y=100)
        entry_1 = Entry(top, width=30, textvar=self.first_name)
        entry_1.place(x=210, y=100)

        label_2 = Label(top, text="Last Name", width=20, font=("bold", 10))
        label_2.place(x=75, y=150)
        entry_2 = Entry(top, width=30, textvar=self.last_name)
        entry_2.place(x=210, y=150)

        label_3 = Label(top, text="Email", width=20, font=("bold", 10))
        label_3.place(x=75, y=200)
        entry_3 = Entry(top, width=30, textvar=self.email)
        entry_3.place(x=210, y=200)

        label_4 = Label(top, text="Phone Number",
                        width=20, font=("bold", 10))
        label_4.place(x=75, y=250)
        entry_4 = Entry(top, width=20, textvar=self.number)
        entry_4.place(x=210, y=250)

        label_5 = Label(top, text="Gender", width=20, font=("bold", 10))
        label_5.place(x=75, y=300)
        Radiobutton(top, text="Male", padx=5, variable=self.Gender,
                    value=1).place(x=205, y=300)
        Radiobutton(top, text="Female", padx=20,
                    variable=self.Gender, value=2).place(x=260, y=300)

        label = Label(top, text="Age", width=20, font=("bold", 10))
        label.place(x=75, y=350)
        entry = Entry(top, textvar=self.age)
        entry.place(x=210, y=350)

        label_6 = Label(top, text="Password",
                        width=20, font=("bold", 10))
        label_6.place(x=75, y=400)
        self.entry_6 =Entry(top, textvar=self.passwor, show="*")
        self.entry_6.place(x=210, y=400)
        Checkbutton(top, text = "Show password", 
                    variable = self.checkButton,
                    onvalue = 1,
                    offvalue = 0,
                    height = 2,
                    width = 10,
                    command = lambda: self.checkbox(top)).place(x=210,y=420)

        Lb1 = BLabel(master=top)
        Lb1.add_option("At least 1 letter between [a-z]")
        Lb1.add_option("At least 1 number between [0-9]")
        Lb1.add_option("At least 1 letter between [A-Z]")
        Lb1.add_option("At least 1 character from [$#@]")
        Lb1.add_option("Minimum length of password: 8")
        Lb1.add_option("Maximum length of password: 15")
        Lb1.l.place(x=155, y=460)
        

        Button(top, text='Submit', width=20, height=2, bg='brown',
               fg='white', command=lambda: self.database(top)).place(x=180, y=560)


# Register()
