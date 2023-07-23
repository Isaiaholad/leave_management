from  tkinter import *
from tkinter.ttk import Combobox
from LM_Images import mybg

class LeaveHistory(Frame):
    def __init__(self, master,data=[]):
        super(LeaveHistory, self).__init__(master)
        self.master.title("LEAVE MANAGEMENT APP")
        self.userdata = data
        self.grid()
        self.create_widgets()

    def create_widgets(self):
        mybg(self).place(x=0,y=0)
        self.lblHeader = Label(self.master, text="Hazzi Commz .inc Leave App", font=("Elephant", 20, "bold"), fg="#999").place(x=50, y=5)

        self.lblStatus = Label(self.master, text="Select Status :", font=("Cooper", 10), fg="blue").place(x=40, y=70)
        self.StatusCombo = Combobox(self.master, state="readonly",values=("All","Pending", "Approved", "Withdrawn","Canceled","Active"))
        self.StatusCombo.set("All")
        self.StatusCombo.place(x=130, y=70)
        self.btnView = Button(self.master, text="View", width="7", command=self.viewStaff, font=("Arial", 10),bg="blue", fg="pink").place(x=150, y=100)
        self.Status = ()
    def viewStaff(self):
        from LM_Database import getleavehistory
        if self.StatusCombo.get() == "Pending":
            self.Status = (self.userdata[0],"pending","","","","")
        elif self.StatusCombo.get() == "Approved":
            self.Status = (self.userdata[0],"approved", "","","","")
        elif self.StatusCombo.get() == "Withdrawn":
            self.Status = (self.userdata[0],"","withdrawn","","","")
        elif self.StatusCombo.get() == "Canceled":
            self.Status = (self.userdata[0],"canceled","","","","")
        elif self.StatusCombo.get() == "Active":
            self.Status = (self.userdata[0],"active","","","","")
        else:
            self.Status = (self.userdata[0],"pending", "approved","withdrawn","canceled","active")

        _,all_leave = getleavehistory(self.Status)
        from LM_Tables import MyTable
        stb = MyTable(self.master,"Leave ID","Leave Type","Date Applied", "Leave Start Date", "Leave End Date", "Leave Status")

        for c,leave in enumerate(all_leave):
            leave = list(leave)
            stb.addData(c,["LV"+str(leave[1])+str(leave[0]), leave[4],(leave[7])[:17], leave[2], leave[3], leave[6]])