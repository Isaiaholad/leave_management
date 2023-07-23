from  tkinter import *
from LM_MenuBar import Leavemanagement,AdminMenuBar,RegularUserMenuBar
from LM_Images import mybg

class UpdateStaff(Frame):
    def __init__(self, master,userdata):
        super(UpdateStaff, self).__init__(master)
        self.master.title("LEAVE MANAGEMENT APP")
        self.userdata=userdata
        self.grid()
        self.create_widgets()

    def create_widgets(self):
        self.usremail = StringVar()
        mybg(self).place(x=0,y=0)

        self.lblHeader = Label(self.master, text="Hazzi Commz .inc Leave App", font=("Elephant", 20, "bold"), fg="#999").place(x=50, y=5)
        self.lblemail = Label(self.master, text="Enter User Email", font=("Cooper", 14),fg="blue").place(x=40, y=80)
        self.entryemail = Entry(self.master, width="20", textvariable=self.usremail,font=("Castellar", 13, "bold"), bg="#ddd",fg="#55a").place(x=200,y=80)
        self.btnedit = Button(self.master, text="E D I T", width="20", command=self.editfcn,bg="blue",fg="pink").place(x=130,y=150)

    def editfcn(self):
        from LM_Database import getuserbymail
        exist, userupdate = getuserbymail(self.usremail.get())
        if not exist:
            from tkinter import messagebox
            messagebox.showwarning("Incorrect details!",f"User with {self.usremail.get()} does not exist \n Please try again")
        elif exist:
            from LM_Register import RegisterUser
            self.master.destroy()
            self.window = Leavemanagement()
            if self.userdata[7]=="Admin":
                AdminMenuBar(self.window, self.userdata)
            elif self.userdata[7]=="Regular":
                RegularUserMenuBar(self.window, self.userdata)
            RegisterUser(self.window,userupdate,id=list(userupdate)[0])
