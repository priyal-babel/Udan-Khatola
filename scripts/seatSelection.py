from tkinter import Canvas, Frame, Label, Tk, Toplevel

class selectSeat:
    def __init__(self):
        # top = Toplevel()
        top = Tk()
        top.title("Book a Ticket - Udan Khatola")
        top.geometry("400x600")

        self.widgets(top)
        top.mainloop()

    def widgets(self,top):
        frame = Frame(top, height=500, width=250, background='WHITE',
                      borderwidth=1, relief='sunken').place(x=75)
        Label(top, text="A",bg="WHITE", font=(
            "Times New Roman", 15)).place(x=95, y=20)
        Label(top, text="B",bg="WHITE", font=(
            "Times New Roman", 15)).place(x=125, y=20)
        Label(top, text="C",bg="WHITE", font=(
            "Times New Roman", 15)).place(x=155, y=20)
        Label(top, text="D",bg="WHITE", font=(
            "Times New Roman", 15)).place(x=225, y=20)
        Label(top, text="E",bg="WHITE", font=(
            "Times New Roman", 15)).place(x=255, y=20)
        Label(top, text="F",bg="WHITE", font=(
            "Times New Roman", 15)).place(x=285, y=20)

        y_height = 0
        for i in range (1,10):
            Label(top, text=i,bg="WHITE", font=(
            "Times New Roman", 12)).place(x=195, y=50+y_height)
            y_height += 30
        for i in range (10,16):
            Label(top, text=i,bg="WHITE", font=(
            "Times New Roman", 12)).place(x=190, y=50+y_height)
            y_height += 30
        
selectSeat()