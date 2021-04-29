from tkinter import Button, Frame, Label, Tk, Toplevel
import MySQLdb
from configure import user,password


class PastBookings:
    def __init__(self,user_id):
        top = Toplevel()
        # top = Tk()
        top.title("Past bookings - Udan Khatola")
        top.geometry("800x400")

        self.user_email = user_id

        self.widgets(top)
        top.mainloop()

    def widgets(self,top):
        frame = Frame(top,height = 80,width = 800,background = 'WHITE', borderwidth = 1, relief = 'sunken').pack()
        Label(top, text="Past Bookings",bg='WHITE', font=("Times New Roman", 30)).place(x=275, y=10)
        try:
            con = MySQLdb.connect(host='localhost', user=user,
                                  password=password, database="airline_reservation")
            cursor = con.cursor()
            cursor.execute("SELECT * FROM booking")
            data = cursor.fetchall()
            frame = Frame(top,height = 24,width = 800,bg='GRAY', borderwidth = 1, relief = 'sunken').place(y = 79)
            Label(top, text="Airline",bg='GRAY', font=("Times New Roman", 10)).place(x=30, y=80)
            Label(top, text="Departure",bg='GRAY', font=("Times New Roman", 10)).place(x=140, y=80)
            Label(top, text="Arrival",bg='GRAY', font=("Times New Roman", 10)).place(x=270, y=80)
            Label(top, text="Date",bg='GRAY', font=("Times New Roman", 10)).place(x=430, y=80)
            Label(top, text="Time",bg='GRAY', font=("Times New Roman", 10)).place(x=365, y=80)
            Label(top, text="PNR",bg='GRAY', font=("Times New Roman", 10)).place(x=510, y=80)
            Label(top, text="Seat No.",bg='GRAY', font=("Times New Roman", 10)).place(x=580, y=80)
            Label(top, text="Class",bg='GRAY', font=("Times New Roman", 10)).place(x=700, y=80)


            y_height = 100
            i=0
            for users in data:
                if users[3]==self.user_email:
                    if i%2==0:
                        frame = Frame(top,height = 30,width = 800, borderwidth = 1, relief = 'sunken').place(y = y_height)
                        rel = 'ridge'
                        i += 1
                    else:
                        frame = Frame(top,height = 30,width = 800, borderwidth = 1, relief = 'raised').place(y = y_height)
                        rel = 'raised'
                        i += 1
                    btn = Label(top, text=users[12],relief=rel,font=('Times New Roman',12),padx=2,pady=3,width=10)
                    btn.place(y=100)
                    btn = Label(top, text=users[8],relief=rel,font=('Times New Roman',12),padx=2,pady=3,width=15)
                    btn.place(x=97,y=100)
                    btn = Label(top, text=users[9],relief=rel,font=('Times New Roman',12),padx=2,pady=3,width=15)
                    btn.place(x=220,y=100)
                    btn = Label(top, text=users[11],relief=rel,font=('Times New Roman',12),padx=1,pady=3,width=6)
                    btn.place(x=351,y=100)
                    btn = Label(top, text=users[10],relief=rel,font=('Times New Roman',12),padx=1,pady=3,width=8)
                    btn.place(x=410,y=100)
                    btn = Label(top, text=users[7],relief=rel,font=('Times New Roman',12),padx=1,pady=3,width=8)
                    btn.place(x=486,y=100)
                    if users[14]==None:
                        btn = Label(top, text='-',relief=rel,font=('Times New Roman',12),padx=1,pady=3,width=8)
                        btn.place(x=563,y=100)
                    else:
                        btn = Label(top, text=users[10],relief=rel,font=('Times New Roman',12),padx=1,pady=3,width=8)
                        btn.place(x=563,y=100)
                    btn = Label(top, text=users[13],relief=rel,font=('Times New Roman',12),padx=1,pady=3,width=17)
                    btn.place(x=640,y=100)
                    
                    y_height += 30
                    return
                else:
                    pass
            Label(top, text="No Bookings Found!", font=("Times New Roman", 30)).place(x=230, y=150)

        except Exception as e:
             print(e)
