from  tkinter import *
from LM_MenuBar import Leavemanagement,AdminMenuBar
from LM_Images import mybg

class UpdateStaff(Frame):
    def __init__(self, master,userdata):
        super(UpdateStaff, self).__init__(master)
        self.master.title("LEAVE MANAGEMENT APP")
        self.userdata = userdata
        self.grid()
        self.create_widgets()

    def create_widgets(self):
        self.usremail = StringVar()
        mybg(self).place(x=0,y=0)

        self.lblHeader = Label(self.master, text="Hazzi Commz .inc Leave App", font=("Elephant", 20, "bold"), fg="#999").place(x=50, y=5)
        self.lblEmail = Label(self.master, text="Enter User Email", font=("Cooper", 14),fg="blue").place(x=40, y=80)
        self.entryEmail = Entry(self.master, width="20", textvariable=self.usremail,font=("Castellar", 13, "bold"), bg="#ddd",fg="#55a").place(x=200,y=80)
        self.btnRemove = Button(self.master, text="R E M O V E", width="20", command=self.removefcn,bg="blue",fg="pink").place(x=130,y=150)

    def removefcn(self):
        from LM_Database import remove_staff
        from tkinter import messagebox
        remove_staff(self.usremail.get())
        messagebox.showinfo("User Deletion Successful","f{self.usremail.get()} has been Successfullly removed")