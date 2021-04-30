from tkinter import Button, Canvas, Frame, Label, Tk, Toplevel, messagebox
from configure import user,password
import MySQLdb

class SelectSeat:
    def __init__(self,pnr):
        # top = Toplevel()
        top = Tk()
        top.title("Book a Ticket - Udan Khatola")
        top.geometry("400x600")

        self.pnr = pnr
        self.prev = None
        self.widgets(top)
        top.mainloop()

    def color_change(self,i,top):
        if self.prev!=None:
            self.prev["bg"]='grey'
        i["bg"] = "blue"
        button_value = str(i)
        index = button_value[8:]
        if index=='':
            seat_num = self.seat_number(0)
        else:
            index = int(index)
            seat_num = self.seat_number(index-1)
        self.button.config(text=seat_num)
        self.prev = i
        Button(top, text='Submit', width=10, bg='brown',
               fg='white', command=lambda:self.database(seat_num,top)).place(x=270, y=550)

    def database(self,seat_num,top):
        try:
            con = MySQLdb.connect(host='localhost', user=user,
                                  password=password, database="airline_reservation")
            cursor = con.cursor()
            cursor.execute("UPDATE booking SET seat=(%s) WHERE pnr=(%s)",(seat_num,self.pnr,))
            con.commit()
            messagebox.showinfo(master=top, title="Success",
                                message="Your seat has been selected successfully!")
            top.destroy()
            # BoardingPass()
        except Exception as e:
            print(e)
            messagebox.showerror(master=top,title="Error",message="Could not select seat!")

    def seat_number(self,index):
        lst = []
        for i in range(1,16):
            for j in ['A','B','C','D','E','F']:
                lst.append(str(i)+j)
        return lst[index]

    def widgets(self,top):
        frame = Frame(top, height=510, width=250, background='WHITE',
                      borderwidth=1, relief='sunken').place(x=75)
        Label(top, text="A",bg="WHITE", font=(
            "Times New Roman", 15)).place(x=95, y=10)
        Label(top, text="B",bg="WHITE", font=(
            "Times New Roman", 15)).place(x=125, y=10)
        Label(top, text="C",bg="WHITE", font=(
            "Times New Roman", 15)).place(x=155, y=10)
        Label(top, text="D",bg="WHITE", font=(
            "Times New Roman", 15)).place(x=225, y=10)
        Label(top, text="E",bg="WHITE", font=(
            "Times New Roman", 15)).place(x=255, y=10)
        Label(top, text="F",bg="WHITE", font=(
            "Times New Roman", 15)).place(x=285, y=10)

        y_height = 0
        for i in range (1,10):
            Label(top, text=i,bg="WHITE", font=(
            "Times New Roman", 12)).place(x=195, y=35+y_height)
            y_height += 30
        for i in range (10,16):
            Label(top, text=i,bg="WHITE", font=(
            "Times New Roman", 12)).place(x=190, y=50+y_height)
            y_height += 30

        h=0
        for i in range(1,16):
            w = 0
            if i<10:
                for j in range(6):
                    if(j<3):
                        btn = Button(top, width=2,bg='grey')
                        btn.place(x=92+w,y=35+h)
                        btn["command"]=lambda btn = btn: self.color_change(btn,top)
                        w += 32
                    else:
                        btn = Button(top, width=2,bg='grey')
                        btn.place(x=125+w,y=35+h)
                        btn["command"] = lambda btn = btn:self.color_change(btn,top)
                        w += 32
            else:
                for j in range(6):
                    if(j<3):
                        btn = Button(top, width=2,bg='grey')
                        btn.place(x=92+w,y=50+h)
                        btn["command"] = lambda btn = btn:self.color_change(btn,top)
                        w += 32
                    else:
                        btn = Button(top, width=2,bg='grey')
                        btn.place(x=125+w,y=50+h)
                        btn["command"] = lambda btn = btn:self.color_change(btn,top)
                        w += 32
            h += 30

        self.button = Label(top, text="", width=5,height=1,bg="white", font=("Times New Roman",20,"bold"))
        self.button.place(x=100,y=530)

# SelectSeat()