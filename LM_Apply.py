from tkinter import *
from tkinter.ttk import Combobox
from tkinter import messagebox
from tkcalendar.dateentry import DateEntry
import LM_Database

class ApplyLeave(Frame):
    def __init__(self, master,data=[]):
        super(ApplyLeave, self).__init__(master)
        self.grid()
        self.userdata = data
        self.create_widgets()
    def create_widgets(self):
        from LM_Images import mybg
        mybg(self).place(x=0,y=0)
        self.lblHeader = Label(self.master, text="Hazzi Commz .inc Leave App", font=("Elephant", 20, "bold"), fg="#999").place(x=50, y=5)
        self.lblInstr = Label(self.master, text="Please fill all details", font=("Ebrima", 10,),fg="#444").place(x=15, y=50)

        self.leaveapplyframe = LabelFrame(self.master, text="New Leave Application",width=550,height=510).place(x=30, y=80)

        self.lblStartdate = Label(self.leaveapplyframe, text="Start Date", font=("Elephant", 10),fg="#555").place(x=70,y=120)
        self.lblEnddate = Label(self.leaveapplyframe, text="End Date", font=("Elephant", 10), fg="#555").place(x=350,y=120)

        self.entryStartdate = DateEntry(self.leaveapplyframe, width="12", year=2021, month=10, day=1,font=("Ebrima", 9))
        self.entryStartdate.place(x=70, y=160)
        self.entryEnddate = DateEntry(self.leaveapplyframe, width="12", year=2021, month=10, day=1,font=("Ebrima", 9))
        self.entryEnddate.place(x=350, y=160)
        self.lblReson = Label(self.leaveapplyframe, text="Reason for Application", font=("Elephant", 10), fg="#555").place(x=70, y=230)
        self.txtReason = Text(self.leaveapplyframe, height=4, width=30, font=("Ebrima", 9), relief=RAISED)
        self.txtReason.place(x=70, y=280)

        self.lblLeaveType = Label(self.leaveapplyframe, text="Leave Type", font=("Elephant", 10), fg="#555").place(x=70,y=380)
        self.comboleaveType = Combobox(self.leaveapplyframe, width=18,values=["Annual", "Medical", "Paternity", "Maternity", "Others"])
        self.comboleaveType.set("Others")
        self.comboleaveType.place(x=100, y=420)
        self.lblOthertype = Label(self.leaveapplyframe, text="If others Please Specify Below", font=("Elephant", 10),fg="#555").place(x=350,y=380)
        self.txtOthertype = Text(self.leaveapplyframe,height=3, width=25,font=("Ebrima", 9),relief=RAISED)
        self.txtOthertype.place(x=360, y=420)

        self.btnApply = Button(self.leaveapplyframe, text="Apply", width="20", command=self.applyfcn, font=("Arial", 12),bg="blue", fg="pink").place(x=200, y=550)

    def applyfcn(self):
        from LM_Database import getLeaveEntitled
        if (self.comboleaveType.get() == "Others") and len(self.txtOthertype.get(1.0,END))<5:
            messagebox.showwarning("Incomplete Details!"," Please Specify type of leave")
        else:
            leavedays = ((self.entryEnddate.get_date()-self.entryStartdate.get_date()).days)
            leaveType =   self.comboleaveType.get() if (self.comboleaveType.get() != "Others") else self.txtOthertype.get(1.0,END)
            if leavedays>0 and leavedays <getLeaveEntitled(self.userdata[0]):
                response=LM_Database.applyleave(self.userdata[0], self.entryStartdate.get(), self.entryEnddate.get(), leaveType, self.txtReason.get("1.0", END))
                if response is True:
                    messagebox.showinfo("Application Successful",f"Dear {self.userdata[1]} your {leaveType} leave will be reviewed shortly")
                elif response is False:
                    messagebox.showwarning("Application failed!","\n\n incorectLeave details or an application is currently pending \n Please try again")
            else:
                messagebox.showwarning("Application failed!","check leave start date and end date \n Please try again")