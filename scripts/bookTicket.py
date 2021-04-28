import json
from tkinter import Button, Entry, Label, Listbox, Scrollbar, StringVar, Toplevel, messagebox, ttk
from tkcalendar import Calendar, DateEntry
import datetime
from selectAirline import Airline
from tkinter.messagebox import askokcancel


class Booking:
    def __init__(self):
        top = Toplevel()
        top.title("Book a Ticket - Airline Reservation System")
        top.geometry("800x350")

        self.airport_names = []
        self.airport_code = []
        self.source = StringVar()
        self.destination = StringVar()
        self.calendar = StringVar()
        self.time = StringVar()
        self.travel_class = StringVar()

        self.loadJson()
        self.buttons(top)

        top.mainloop()

    def loadJson(self):
        data = open('json_data/airports.json',)
        json_data = json.load(data)
        airport_data = json_data["airports"]
        for airports in airport_data:
            self.airport_names.append(airports["airport_name"])
        data.close()

    def isEmpty(self, booking_dict, top):
        if booking_dict["source"] == '':
            messagebox.showerror(master=top, title="Form Empty",
                                 message="Please Enter Source Location!")
            top.lift()
            return True

        elif booking_dict["destination"] == '':
            messagebox.showerror(
                master=top, title="Form Empty", message="Please Enter Destination Location!")
            top.lift()
            return True
        elif booking_dict["time"] == '':
            messagebox.showerror(master=top, title="Form Empty",
                                 message="Please Enter Time of Travel!")
            top.lift()
            return True
        elif booking_dict["travel_class"] == '':
            messagebox.showerror(master=top, title="Form Empty",
                                 message="Please Enter Class of Travel!")
            top.lift()
            return True

        elif booking_dict["source"] == booking_dict["destination"]:
            messagebox.showerror(
                master=top, title="Form Empty", message="Source and destination cannot be same!")
            top.lift()
            return True
        return False

    def onSubmit(self, top):
        booking_dict = {
            "source": self.source.get(),
            "destination": self.destination.get(),
            "date": self.calendar.get(),
            "time": self.time.get(),
            "travel_class": self.travel_class.get()
        }
        if(self.isEmpty(booking_dict, top) == True):
            return
        else:
            top.destroy()
            Airline(booking_dict)

    def buttons(self, top):
        label = Label(top, text="Flight Booking", padx="3",
                      pady="3", font=("Times New Roman", 25)).pack()

        Label(top, text="Source Location: ", font=(
            "Times New Roman", 15)).place(x=180, y=60)
        source_chosen = ttk.Combobox(top, width=38, textvariable=self.source)
        source_chosen['values'] = self.airport_names
        source_chosen.place(x=375, y=65)
        source_chosen.current()

        Label(top, text="Destination Location: ", font=(
            "Times New Roman", 15)).place(x=180, y=100)
        destination_chosen = ttk.Combobox(
            top, width=38, textvariable=self.destination)
        destination_chosen['values'] = self.airport_names
        destination_chosen.place(x=375, y=105)
        destination_chosen.current()

        today = datetime.date.today()
        Label(top, text="Date of Journey: ", font=(
            "Times New Roman", 15)).place(x=180, y=140)
        cal = DateEntry(top, selectmode="day", width=15, year=today.year, month=today.month, day=today.day,
                        background='darkblue', foreground='white', borderwidth=2, textvariable=self.calendar)
        cal.place(x=375, y=145)

        Label(top, text="Time of Journey: ", font=(
            "Times New Roman", 15)).place(x=180, y=180)
        time_chosen = ttk.Combobox(top, width=10, textvariable=self.time)
        time_chosen['values'] = ['7:30', '9:30', '11:30',
                                 '13:30', '15:30', '17:30', '19:30', '21:30', '23:30']
        time_chosen.place(x=375, y=185)
        time_chosen.current()

        Label(top, text="Class of Travel: ", font=(
            "Times New Roman", 15)).place(x=180, y=220)
        class_chosen = ttk.Combobox(
            top, width=20, textvariable=self.travel_class)
        class_chosen['values'] = ['First Class',
                                  'Business Class', 'Economy Class']
        class_chosen.place(x=375, y=225)
        class_chosen.current()

        Button(top, text='Submit', width=20, bg='brown',
               fg='white', command=lambda: self.onSubmit(top)).place(x=300, y=280)
