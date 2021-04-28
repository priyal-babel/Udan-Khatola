from tkinter import Frame, Label, Tk, Toplevel
import MySQLdb
from configure import user,password


class PastBookings:
    def __init__(self,user_id):
        # top = Toplevel()
        top = Tk()
        top.title("Past bookings - Airline Reservation System")
        top.geometry("800x400")

        self.user_email = user_id

        self.widgets(top)
        top.mainloop()

    def widgets(self,top):
        frame = Frame(top,height = 80,width = 800,background = 'WHITE', borderwidth = 1, relief = 'sunken').pack()
        Label(frame, text="Past Bookings",bg='WHITE', font=("Times New Roman", 30)).place(x=275, y=10)
        try:
            con = MySQLdb.connect(host='localhost', user=user,
                                  password=password, database="airline_reservation")
            cursor = con.cursor()
            cursor.execute("SELECT * FROM booking")
            data = cursor.fetchall()
            Label(top, text="Airline", font=("Times New Roman", 10)).place(x=20, y=80)
            Label(top, text="Departure", font=("Times New Roman", 10)).place(x=120, y=80)
            Label(top, text="Arrival", font=("Times New Roman", 10)).place(x=240, y=80)
            Label(top, text="Date", font=("Times New Roman", 10)).place(x=320, y=80)
            Label(top, text="Time of departure", font=("Times New Roman", 10)).place(x=400, y=80)
            Label(top, text="PNR", font=("Times New Roman", 10)).place(x=540, y=80)
            Label(top, text="Seat No.", font=("Times New Roman", 10)).place(x=620, y=80)

            y_height = 100
            for users in data:
                if users[3]==self.user_email:
                    frame = Frame(top,height = 50,width = 800, borderwidth = 1, relief = 'sunken').place(y = y_height)
                    y_height += 50
                    return
                else:
                    pass
            Label(top, text="No Bookings Found!", font=("Times New Roman", 30)).place(x=230, y=150)

        except Exception as e:
             print(e)

PastBookings("priyalbabel@gmail.com")