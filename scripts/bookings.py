import fullScreen as fs
import tkinter
from tkinter import *

top = Tk()
top.title("Airline Reservation System")
app = fs.FullScreenApp(top)
label = Label(top, text="Flight Booking",padx = "3",pady = "3", font=("Times New Roman", 25)).pack()
user_name = Label(top, text = "Source Location", font=("Times New Roman", 25)).place(x = 100, y = 60)    
variable = StringVar(top)
variable.set("-Select a Source Airport-")
w = OptionMenu(top, variable, "Chhatrapati Shivaji International Airport (BOM), Mumbai", "Pune International Airport (PNQ), Pune", "Dr Babasaheb Ambedkar International Airport (NAG), Nagpur", "Shri Guru Gobind Singh Ji Airport (NDC), Nanded", "Akola Airport (AKD)", "Aurangabad Airport (IXU)", "Shirdi Airport (SAG)", "Kolhapur Airport (KLH), Kolhapur", "").place(x = 325, y = 60) 
user_password = Label(top, text = "Destination", font=("Times New Roman", 25)).place(x = 100, y = 100) 
top.mainloop()