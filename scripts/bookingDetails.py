from tkinter import Button, Canvas, Entry, Frame, IntVar, Label, Radiobutton, StringVar, Text, Tk, Toplevel, messagebox
# from PIL.Image import Image
from PIL import ImageTk, Image
import json
from configure import user, password
import MySQLdb
import string
import random
from invoice import Invoice


class Details:
    def __init__(self, details, travel_details):
        window = Toplevel()
        # window = Tk()
        window.title("Confirm booking - Udan Khatola")
        window.geometry("800x600")

        self.airline_details = details
        self.travel_details = travel_details
        self.source_city = ''
        self.destination_city = ''
        self.first_name = StringVar()
        self.last_name = StringVar()
        self.email = StringVar()
        self.address = StringVar()
        self.phone = StringVar()
        self.Gender = IntVar()
        self.age = StringVar()

        self.loadJson()
        self.widgets(window)
        self.inputDetails(window)
        window.mainloop()

    def loadJson(self):
        data = open('json_data/airports.json',)
        json_data = json.load(data)
        airport_data = json_data["airports"]
        for airports in airport_data:
            if airports["airport_name"] == self.travel_details["source"]:
                self.source_city = airports["city_name"]
            if airports["airport_name"] == self.travel_details["destination"]:
                self.destination_city = airports["city_name"]
        data.close()

    def isFormEmpty(self):
        if(self.first_name.get() == '' or self.last_name.get() == '' or self.email.get() == '' or self.phone.get() == '' or self.Gender.get() == 0 or self.age.get() == ''):
            return True

    def generatePNR(self):
        lower = list(string.ascii_lowercase)
        upper = list(string.ascii_uppercase)
        number = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
        final_list = lower+upper+number
        pnr = ''
        for _ in range(6):
            pnr += random.choice(final_list)
        return pnr

    def onSubmit(self, top):
        check = True
        firstName = self.first_name.get()
        lastName = self.last_name.get()
        emailid = self.email.get()
        num = self.phone.get()
        gender = self.Gender.get()
        age = self.age.get()
        address = self.address.get()
        pnr = self.generatePNR()

        if self.isFormEmpty() == True:
            messagebox.showerror(master=top, title="Form Empty",
                                 message="Please enter all details!")
            top.lift()
            return
        if '@' not in emailid:
            messagebox.showerror(master=top, title="Error",
                                 message="Invalid Email")
            top.lift()
            return
        try:
            con = MySQLdb.connect(host='localhost', user=user,
                                  password=password, database="airline_reservation")
            cursor = con.cursor()
            cursor.execute("INSERT INTO booking(firstname,lastname,phonenumber, emailid, address,gender, age,pnr,source,destination,date,time,airline_name,class) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",
                           (firstName, lastName, num, emailid, address, gender, age, pnr, self.source_city, self.destination_city, self.travel_details["date"], self.travel_details["time"], self.airline_details["name"], self.travel_details["travel_class"]))
            con.commit()
            messagebox.showinfo(master=top, title="Booking successful",
                                message="Your ticket has been booked successfully!")
            Invoice(pnr)
            top.destroy()

        except Exception as e:
            print(e)
            messagebox.showerror(master=top, title="Error",
                                 message="Error\nUnable to book.")
            top.lift()

    def widgets(self, window):
        Label(window, text="Confirm Booking", font=(
            "Times New Roman", 30)).place(x=250, y=10)
        frame = Frame(window, height=120, width=700, background='WHITE',
                      borderwidth=1, relief='sunken').place(x=50, y=70)

        load = Image.open(self.airline_details['logo'])
        load = load.resize((120, 80), Image.ANTIALIAS)
        render = ImageTk.PhotoImage(load)
        img = Label(window, image=render)
        img.image = render
        img.place(x=70, y=90)

        Label(window, text="DEPARTURE", font=(
            "Times New Roman", 10)).place(x=270, y=90)
        Label(window, text=self.source_city, bg='WHITE', font=(
            "Times New Roman", 25)).place(x=230, y=110, width=150)
        Label(window, text=self.travel_details["source"], bg='WHITE', fg='GRAY', font=(
            "Times New Roman", 10)).place(x=210, y=150, width=220)

        load = Image.open("src/arrow.png")
        load = load.resize((50, 40), Image.ANTIALIAS)
        render = ImageTk.PhotoImage(load)
        img = Label(window, image=render, bg='WHITE')
        img.image = render
        img.place(x=385, y=110)

        Label(window, text="Time: "+self.travel_details["time"], bg="WHITE", font=(
            "Times New Roman", 8)).place(x=385, y=168)

        Label(window, text="ARRIVAL", font=(
            "Times New Roman", 10)).place(x=500, y=90)
        Label(window, text=self.destination_city, bg='WHITE', font=(
            "Times New Roman", 25)).place(x=460, y=110, width=150)
        Label(window, text=self.travel_details["destination"], bg='WHITE', fg='GRAY', font=(
            "Times New Roman", 10)).place(x=440, y=150, width=220)

        Label(window, text="RATE", font=(
            "Times New Roman", 10)).place(x=660, y=90)
        Label(window, text="₹"+str(self.airline_details["rate"]), bg='WHITE', font=(
            "Times New Roman", 15)).place(x=625, y=115, width=100)
        Label(window, text="DATE", font=(
            "Times New Roman", 10)).place(x=660, y=140)
        Label(window, text=str(self.travel_details["date"]), bg='WHITE', font=(
            "Times New Roman", 10)).place(x=625, y=165, width=100)

    def inputDetails(self, window):
        Label(window, text="First Name:", font=(
            "Times New Roman", 15)).place(x=60, y=220)
        Entry(window, width=30, textvar=self.first_name).place(x=200, y=225)

        Label(window, text="Last Name:", font=(
            "Times New Roman", 15)).place(x=410, y=220)
        Entry(window, width=30, textvar=self.last_name).place(x=550, y=225)

        Label(window, text="Billing Address:", font=(
            "Times New Roman", 15)).place(x=60, y=280)
        Entry(window, width=90, textvar=self.address).place(x=200, y=285)

        Label(window, text="Email Address:", font=(
            "Times New Roman", 15)).place(x=60, y=340)
        Entry(window, width=30, textvar=self.email).place(x=200, y=345)

        Label(window, text="Phone Number:", font=(
            "Times New Roman", 15)).place(x=410, y=340)
        Entry(window, width=30, textvar=self.phone).place(x=550, y=345)

        Label(window, text="Gender:", font=(
            "Times New Roman", 15)).place(x=60, y=400)
        Radiobutton(window, text="Male", padx=5, variable=self.Gender,
                    value=1).place(x=205, y=405)
        Radiobutton(window, text="Female", padx=5,
                    variable=self.Gender, value=2).place(x=305, y=405)
        Radiobutton(window, text="Other", padx=5,
                    variable=self.Gender, value=3).place(x=400, y=405)

        Label(window, text="Age:", font=(
            "Times New Roman", 15)).place(x=60, y=460)
        Entry(window, width=10, textvar=self.age).place(x=200, y=465)

        Button(window, text='Submit', width=15, height=2, bg='brown',
               fg='white', command=lambda: self.onSubmit(window)).place(x=345, y=510)
