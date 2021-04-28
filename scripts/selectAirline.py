from tkinter import Button, Canvas, Frame, Label, PhotoImage, Tk, Toplevel
from airlineTypes import airline_type
import json
from PIL import Image, ImageTk
from bookingDetails import Details


class Airline:
    def __init__(self,booking_ticket):
        window = Toplevel()
        # window = Tk()
        window.title("Book a Ticket")
        window.geometry("800x600")

        self.booking_ticket = booking_ticket
        self.source_city = ''
        self.destination_city = ''

        self.loadJson()
        self.button(window)
        window.mainloop()

    def loadJson(self):
        data = open('json_data/airports.json',)
        json_data = json.load(data)
        airport_data = json_data["airports"]
        for airports in airport_data:
            if airports["airport_name"]==self.booking_ticket["source"]:
                self.source_city = airports["city_name"]
            if airports["airport_name"]==self.booking_ticket["destination"]:
                self.destination_city = airports["city_name"]
        data.close()

    def back(self,top):
        top.destroy()
        from bookTicket import Booking
        Booking()

    def confirmBooking(self,details,top):
        top.destroy()
        Details(details,self.booking_ticket)
        
    def button(self,window):
        heading = "Flights from "+self.source_city+" to "+self.destination_city
        label = Label(window, text=heading, padx="3",
                      pady="3", font=("Times New Roman", 25)).pack()

        y_height=50
        for a in airline_type:
            frame = Frame(window,height = 120,width = 800,background = 'WHITE', borderwidth = 1, relief = 'sunken').place(y=y_height)

            load = Image.open(airline_type[a]['logo'])
            load = load.resize((120, 80), Image.ANTIALIAS)
            render = ImageTk.PhotoImage(load)
            img = Label(window,image=render)
            img.image = render
            img.place(x=40, y=20+y_height) 
            
            Label(window, text="Departure:", font=("Times New Roman", 15)).place(x=300, y=15+y_height)
            Label(window, text=self.booking_ticket["time"],bg='WHITE', font=("Times New Roman", 15,'bold')).place(x=320, y=55+y_height)
            text = self.booking_ticket["source"] + " (" + self.source_city+")"
            Label(window, text=text,bg='WHITE',fg='GRAY', font=("Times New Roman", 10)).place(x=280, y=85+y_height)

            Label(window, text="Price:", font=("Times New Roman", 15)).place(x=500, y=15+y_height)
            Label(window, text='₹'+str(airline_type[a]['rate']),bg='WHITE', font=("Times New Roman", 15,'bold')).place(x=500, y=55+y_height)

            y_height += 120

        Button(window, text='Book', width=10, height=2, bg='brown',
               fg='white',command=lambda:self.confirmBooking(airline_type["Vistara"],window)).place(x=650, y=90)
        Button(window, text='Book', width=10, height=2, bg='brown',
               fg='white',command=lambda:self.confirmBooking(airline_type["AirAsia"],window)).place(x=650, y=210)
        Button(window, text='Book', width=10, height=2, bg='brown',
               fg='white',command=lambda:self.confirmBooking(airline_type["Indigo"],window)).place(x=650, y=330)
        Button(window, text='Book', width=10, height=2, bg='brown',
               fg='white',command=lambda:self.confirmBooking(airline_type["Air India"],window)).place(x=650, y=450)

        Button(window, text='Change details', width=15, height=2, bg='brown',
               fg='white',command=lambda:self.back(window)).place(x=345, y=545)

# Airline({'source': 'Amausi Airport', 'destination': 'Bhavnagar Airport', 'calendar': '4/30/21', 'time': '19:30', 'travel_class': 'Economy Class'})