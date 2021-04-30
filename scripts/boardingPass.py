from tkinter import Frame, Label, PhotoImage, Tk, Toplevel, messagebox
from PIL import Image, ImageTk
import MySQLdb
from configure import user,password
from airlineTypes import airline_type

class BoardingPass:
    def __init__(self,pnr):
        window = Toplevel()
        # window = Tk()
        window.title("Invoice - Udan Khatola")
        window.geometry("600x300")

        self.pnr = pnr
        self.data = self.database(window)
        self.widgets(window)
        window.mainloop()

    def database(self,top):
        try:
            con = MySQLdb.connect(host='localhost', user=user,
                                  password=password, database="airline_reservation")
            cursor = con.cursor()
            cursor.execute("SELECT * FROM booking")
            pnr_data = cursor.fetchall()
            for data in pnr_data:
                if self.pnr == data[7]:
                    return data
        except Exception as e:
            print(e)
            messagebox.showerror(master=top,title="Error",message= "Error\nUnable to generate Boarding pass.")
            top.lift()

    def widgets(self,top):
        one = Frame(top, bg = '#ED1B24', width = 60, height = 450)
        one.pack(side = 'left')

        two = Frame(top, bg = '#1B1464', width = 700, height = 40)
        two.pack(side = 'top')

        load = Image.open(airline_type[self.data[-3]]["logo"])
        load = load.resize((80, 60), Image.ANTIALIAS)
        render = ImageTk.PhotoImage(load)
        img = Label(top, image=render)
        img.image = render
        img.place(x=60, y=40)

        lbl1 = Label(two, text='Boarding Pass', font=('Times New Roman', 20), fg='#fff', bg='#1B1464')
        lbl1.place(x=305, y=6, anchor='ne')

        lbl2 = Label(top, text='Passenger Name:', font=('Times New Roman', 10))
        lbl2.place(x=300, y=45, anchor='ne')
        lbl3 = Label(top, text=self.data[0]+" "+self.data[1], font=('Times New Roman', 15))
        lbl3.place(x=350, y=70, width = 200, anchor='ne')

        lbl4 = Label(top, text='From', font=('Times New Roman', 10))
        lbl4.place(x=120, y=110, anchor='ne')
        lbl5 = Label(top, text=self.data[8], font=('Times New Roman', 15))
        lbl5.place(x=205, y=130, width = 100, anchor='ne')

        lbl6 = Label(top, text='To', font=('Times New Roman', 10))
        lbl6.place(x=108, y=160, anchor='ne')
        lbl7 = Label(top, text=self.data[9], font=('Times New Roman', 15))
        lbl7.place(x=205, y=180, width = 100, anchor='ne')

        lbl8 = Label(top, text='Flight', font=('Times New Roman', 9))
        lbl8.place(x=290, y=110, anchor='ne')
        lbl9 = Label(top, text=self.data[-3], font=('Times New Roman', 13))
        lbl9.place(x=315, y=130, width = 80, anchor='ne')

        lbl10 = Label(top, text='Date', font=('Times New Roman', 9))
        lbl10.place(x=370, y=110, anchor='ne')
        lbl11 = Label(top, text=self.data[10], font=('Times New Roman', 15))
        lbl11.place(x=430, y=130, width = 100, anchor='ne')

        lbl12 = Label(top, text='Time', font=('Times New Roman', 9))
        lbl12.place(x=370, y=160, anchor='ne')
        lbl13 = Label(top, text=self.data[11], font=('Times New Roman', 15))
        lbl13.place(x=417, y=180, width = 100, anchor='ne')

        Label(top, text='Seat No:',bg='yellow', font=('Times New Roman', 20)).place(x=470, y=220, anchor='ne')
        Label(top, text=self.data[-1],bg='yellow', font=('Times New Roman', 20)).place(x=515, y=220, anchor='ne',width=50)


# BoardingPass('0EIqFy')