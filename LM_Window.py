from tkinter import *
from LM_Images import mybg, centerimg

class StartApp(Frame):
    def __init__(self, master):
        super(StartApp, self).__init__(master)
        self.grid()
        self.create_widgets()

    def create_widgets(self):
        mybg(self).place(x=0,y=0)
        centerimg(self).place(x=120, y=100)
        self.lblHeader = Label(self.master, text="Hazzi Commz .inc Leave App", font=("Elephant", 20, "bold"), fg="#999").place(x=50, y=5)
        self.btnContinue = Button(self.master, text="Continue", command=self.continuefcn,width="20", font=("Arial", 12)).place(x=170, y=500)
        self.mainloop()

    def continuefcn(self):
        from LM_Login import LoginUser
        self.master.destroy()
        self.window = Leavemanagement()
        LoginUser(self.window)

class Leavemanagement(Tk):
    def __init__(self):
        super(Leavemanagement, self).__init__()
        self.grid()
        self.title("LEAVE MANAGEMENT APP")
        self.geometry("560x600+350+50")
        self.resizable(False,False)