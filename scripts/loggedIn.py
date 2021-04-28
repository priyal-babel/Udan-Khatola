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
            for users in data:
                if users[3]==self.user_email:
                    x = 10
                    return
                else:
                    pass
            Label(top, text="No Bookings Found!", font=("Times New Roman", 30)).place(x=230, y=150)

        except Exception as e:
             print(e)

PastBookings("priyalbabel@gmail.com")