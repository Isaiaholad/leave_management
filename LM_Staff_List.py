from  tkinter import *
from tkinter.ttk import Treeview,Style,Combobox,Scrollbar
from LM_Images import mybg
from LM_Database import getAlluser
import LM_Images
class StaffList(Frame):
    def __init__(self, master):
        super(StaffList, self).__init__(master)
        self.master.title("LEAVE MANAGEMENT APP")
        self.create_widgets()

    def create_widgets(self):
        self.roleSelected=StringVar

        mybg(self).place(x=0,y=0)

        self.lblHeader = Label(self.master, text="Hazzi Commz .inc Leave App", font=("Elephant", 20, "bold"),fg="#999").place(x=50, y=5)
        self.lblRole = Label(self.master, text="Select Role :", font=("Cooper", 10), fg="blue").place(x=40, y=70)
        self.roleCombo = Combobox(self.master, textvariable=self.roleSelected, state="readonly",values=("All","Admin", "Regular"))
        self.roleCombo.set("All")
        self.roleCombo.place(x=130, y=70)
        self.btnView = Button(self.master, text="View", width="7", command=self.viewStaff, font=("Arial", 10),bg="blue", fg="pink").place(x=150, y=100)
        self.role = ()

    def viewStaff(self):
        if self.roleCombo.get() == "Regular":
            self.role = ("Regular","")
        elif self.roleCombo.get() == "Admin":
            self.role = ("Admin","")
        else:
            self.role = ("Regular","Admin")
        allstaff = getAlluser(self.role)

        from LM_Tables import MyTable
        stb=MyTable(self.master,"Staff Id", "Fullname", "Email", "Phone", "Gender")
        for c,staff in enumerate (allstaff):
            staff = list(staff)
            stb.addData(c,[staff[0],staff[1]+" "+staff[2],staff[4],staff[3],staff[8]])