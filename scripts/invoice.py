from tkinter import Frame, Label, Tk, Toplevel, messagebox
import MySQLdb
from configure import user,password
import json
from PIL import ImageTk, Image
from airlineTypes import airline_type

class Invoice:
    def __init__(self,pnr):
        # window = Toplevel()
        window = Tk()
        window.title("Invoice - Udan Khatola")
        window.geometry("800x600")

        self.data = []
        self.pnr = pnr

        self.database(window)
        self.loadJson()
        self.widgets(window)
        window.mainloop()

    def database(self,top):
        try:
            con = MySQLdb.connect(host='localhost', user=user,
                                  password=password, database="airline_reservation")
            cursor = con.cursor()
            command = "SELECT * FROM booking"
            cursor.execute(command)
            data = cursor.fetchall()
            for current in data:
                if self.pnr==current[7]:
                    self.data = current
        except Exception as e:
            print(e)
            top.lift()
            messagebox.showerror("Error","Could not connect")
        return

    def loadJson(self):
        data = open('json_data/airports.json',)
        json_data = json.load(data)
        airport_data = json_data["airports"]
        for airports in airport_data:
            if airports["city_name"] == self.data[8]:
                self.source_airport = airports["airport_name"]
            if airports["city_name"] == self.data[9]:
                self.destination_airport = airports["airport_name"]
        data.close()
        
    def widgets(self,top):
        frame = Frame(top,height = 80,width = 800,background = 'WHITE', borderwidth = 1, relief = 'sunken').pack()
        Label(top, text="INVOICE",bg='WHITE', font=("Times New Roman", 30)).place(x=300, y=10)

        Label(top, text=self.data[8], font=("Times New Roman", 25)).place(x=100, y=100,width=200)
        Label(top, text="("+self.source_airport+")",fg='grey', font=("Times New Roman", 15)).place(x=50, y=150,width=300)

        load = Image.open("src/arrow.png")
        load = load.resize((70, 40), Image.ANTIALIAS)
        render = ImageTk.PhotoImage(load)
        img = Label(top, image=render)
        img.image = render
        img.place(x=360, y=105)

        Label(top, text=self.data[9], font=("Times New Roman", 25)).place(x=500, y=100,width=200)
        Label(top, text="("+self.destination_airport+")",fg='grey', font=("Times New Roman", 15)).place(x=450, y=150,width=300)

        logo = airline_type[self.data[12]]["logo"]
        load = Image.open(logo)
        load = load.resize((150, 100), Image.ANTIALIAS)
        render = ImageTk.PhotoImage(load)
        img = Label(top, image=render)
        img.image = render
        img.place(x=150, y=200)

        Label(top, text="Date of departure: ", font=("Times New Roman", 15)).place(x=350, y=200)
        Label(top, text="Time of departure: ", font=("Times New Roman", 15)).place(x=350, y=240)
        Label(top, text="Class: ", font=("Times New Roman", 15)).place(x=350, y=280)

        Label(top, text=self.data[10], font=("Times New Roman", 15)).place(x=510, y=200)
        Label(top, text=self.data[11], font=("Times New Roman", 15)).place(x=510, y=240)
        Label(top, text=self.data[-2], font=("Times New Roman", 15)).place(x=410, y=280)

        Label(top, text="Name: ", font=("Times New Roman", 15)).place(x=200, y=350)
        Label(top, text="Email ID: ", font=("Times New Roman", 15)).place(x=200, y=390)
        Label(top, text="PNR: ", font=("Times New Roman", 15)).place(x=200, y=430)

        Label(top, text=self.data[0] +" "+ self.data[1], font=("Times New Roman", 15)).place(x=300, y=350)
        Label(top, text=self.data[3], font=("Times New Roman", 15)).place(x=300, y=390)
        Label(top, text=self.data[7], font=("Times New Roman", 15)).place(x=300, y=430)

        rate = airline_type[self.data[-3]]["rate"]
        Label(top, text="Amount Paid: ", font=("Times New Roman", 15)).place(x=450, y=500)
        Label(top, text="₹ "+str(rate), font=("Times New Roman", 15)).place(x=575, y=500)

Invoice('Ohvgs9')