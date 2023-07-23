from  tkinter import *
from tkinter.ttk import Combobox
from LM_Images import mybg

class AllRequestList(Frame):
    def __init__(self, master):
        super(AllRequestList, self).__init__(master)
        self.userdata = []
        self.grid()
        self.create_widgets()

    def create_widgets(self):
        mybg(self).place(x=0, y=0)
        self.lblHeader = Label(self.master, text="Hazzi Commz .inc Leave App", font=("Elephant", 20, "bold"),fg="#999").place(x=50, y=5)

        self.lblStatus = Label(self.master, text="Select Status :", font=("Cooper", 10), fg="blue").place(x=40, y=70)
        self.StatusCombo = Combobox(self.master, state="readonly",values=("All", "Pending", "Approved", "Withdrawn", "Canceled", "Active"))
        self.StatusCombo.set("All")
        self.StatusCombo.place(x=130, y=70)
        self.btnView = Button(self.master, text="View", width="7", command=self.viewStaff, font=("Arial", 10),bg="blue", fg="pink").place(x=150, y=100)
        self.Status = ()

    def viewStaff(self):
        from LM_Database import getAllRequest, getuserbyid
        from LM_Tables import MyTable
        if self.StatusCombo.get() == "Pending":
            self.Status = ("pending","","","","")
        elif self.StatusCombo.get() == "Approved":
            self.Status = ("approved", "","","","")
        elif self.StatusCombo.get() == "Withdrawn":
            self.Status = ("","withdrawn","","","")
        elif self.StatusCombo.get() == "Canceled":
            self.Status = ("canceled","","","","")
        elif self.StatusCombo.get() == "Active":
            self.Status = ("active","","","","")
        else:
            self.Status = ("pending", "approved","withdrawn","canceled","active")

        _, all_leave = getAllRequest(self.Status)
        stb = MyTable(self.master,"Leave ID","Staff Name","Leave Type","Date Applied", "Leave Start Date", "Leave End Date", "Leave Status")

        for c,leave in enumerate(all_leave):
            leave = list(leave)
            staffname = list(getuserbyid(leave[1]))[1] + list(getuserbyid(leave[1]))[2]
            stb.addData(c,["LV"+str(leave[1])+str(leave[0]),staffname, leave[4],(leave[7])[:17], leave[2], leave[3], leave[6]])