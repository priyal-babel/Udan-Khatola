import tkinter as tk
from tkinter import Toplevel, Label, messagebox, StringVar, IntVar, Entry, Radiobutton, Button, Listbox
from configure import user, password
from seatSelection import selectSeat
import MySQLdb

class WebCheckin:
    def __init__(self):
        top = Toplevel()
        top.title("Udan Khatola")
        top.geometry("500x300")

        self.pnr_value = StringVar()
        self.buttons(top)
        top.mainloop()

    def checkPNR(self,top):
        pnr = self.pnr_value.get()
        try:
            con = MySQLdb.connect(host='localhost', user=user,
                                  password=password, database="airline_reservation")
            cursor = con.cursor()
            cursor.execute("SELECT pnr FROM booking")
            pnr_data = cursor.fetchall()
            for data in pnr_data:
                if pnr == data[0]:
                    selectSeat()
                    return
            messagebox.showerror(
                master=top, title="Error", message="Invalid PNR")
            top.lift()
        except Exception as e:
            print(e)

    def buttons(self,top):
        label_1 = Label(top, text="Enter PNR number:", width=20, font=("bold", 10))
        label_1.place(x=50, y=100)
        entry_1 = Entry(top, width=30,textvar=self.pnr_value)
        entry_1.place(x=210, y=100)

        Button(top, text='Submit', width=20, bg='brown',
               fg='white', command=lambda:self.checkPNR(top)).place(x=180, y=150)
