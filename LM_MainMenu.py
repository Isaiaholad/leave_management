from  tkinter import *
from LM_Images import mybg
class MainMenu(Frame):
    def __init__(self, master,uname):
        super(MainMenu, self).__init__(master)
        self.uname=uname
        self.master.title("LEAVE MANAGEMENT APP")
        self.grid()
        self.create_widgets()

    def create_widgets(self):
        mybg(self).place(x=0,y=0)

        self.lblHeader = Label(self.master, text="Hazzi Commz .inc Leave App", font=("Elephant", 20, "bold"), fg="#999").place(x=50, y=5)

        Label(self.master, text="Welcome to HAZZI COMMZ Leave Management", font=("Castellar", 10),fg="#222").place(x=30, y=100)
        Label(self.master, text="What would you like to do today ?  @"+self.uname, font=("Courier", 10), fg="#222").place(x=30, y=150)
        Label(self.master, text="Select an option from the menu bar at the top\nto get started !", font=("Courier", 10), fg="#222").place(x=100, y=350)