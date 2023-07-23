from tkinter import *
from LM_Window import Leavemanagement
from tkinter import messagebox

class AdminMenuBar(Frame):
    def __init__(self, master,userdata):
        super(AdminMenuBar, self).__init__(master)
        self.userdata=userdata
        self.create_widgets()

    def create_widgets(self):
        menubar=Menu(self)
        fileMenu=Menu(menubar)
        actionMenu = Menu(menubar)
        viewMenu = Menu(menubar)

        menubar.add_cascade(label="File",menu=fileMenu)
        fileMenu.add_command(label="Home", command=self.home)
        fileMenu.add_command(label="Open staff list",command=self.openstafflist)
        fileMenu.add_command(label="Close",command=self.landingpage)
        fileMenu.add_command(label="Exit",command=self.master.quit)

        menubar.add_cascade(label="Action",menu=actionMenu)
        actionMenu.add_command(label="Register New Staff", command=self.registerstaff)
        actionMenu.add_command(label="Check Leave Request", command=self.checkleaverequest)
        actionMenu.add_command(label="Update Staff Details", command=self.updatedetails)
        actionMenu.add_command(label="Remove Staff", command=self.removestaff)

        menubar.add_cascade(label="View", menu=viewMenu)
        viewMenu.add_command(label="View All Leave Records", command=self.allrecord)

        self.master.config(menu=menubar)

    def home(self):
        from LM_MainMenu import MainMenu
        self.master.destroy()
        self.window = Leavemanagement()
        AdminMenuBar(self.window,self.userdata)
        MainMenu(self.window,self.userdata[1]+self.userdata[2])

    def openstafflist(self):
        from LM_Staff_List import StaffList
        self.master.destroy()
        self.window = Leavemanagement()
        AdminMenuBar(self.window,self.userdata)
        StaffList(self.window)
    def landingpage(self):
        from LM_Login import LoginUser
        self.master.destroy()
        self.window = Leavemanagement()
        LoginUser(self.window)

    def registerstaff(self):
        from LM_Register import RegisterUser
        self.master.destroy()
        self.window = Leavemanagement()
        AdminMenuBar(self.window,self.userdata)
        RegisterUser(self.window)

    def checkleaverequest(self):
        from LM_Leave_Requests import LeaveRequests
        self.master.destroy()
        self.window = Leavemanagement()
        AdminMenuBar(self.window,self.userdata)
        LeaveRequests(self.window)

    def updatedetails(self):
        from LM_Update_Staff import UpdateStaff
        self.master.destroy()
        self.window = Leavemanagement()
        AdminMenuBar(self.window, self.userdata)
        UpdateStaff(self.window, self.userdata)

    def removestaff(self):
        from LM_Database import remove_staff
        remove_staff( self.userdata[4])
        messagebox.showinfo("Successful", f"user {self.userdata[1]}  has been deleted!!!")

    def allrecord(self):
        from LM_All_Leave_History import AllRequestList
        self.master.destroy()
        self.window = Leavemanagement()
        AdminMenuBar(self.window, self.userdata)
        AllRequestList(self.window)


class RegularUserMenuBar(Frame):
    def __init__(self, master,userdata=[]):
        super(RegularUserMenuBar, self).__init__(master)
        self.userdata=userdata
        self.grid()
        self.create_widgets()

    def create_widgets(self):
        menubar=Menu(self)
        fileMenu=Menu(menubar)
        actionMenu = Menu(menubar)
        viewMenu = Menu(menubar)
        helpMenu = Menu(menubar)
        menubar.add_cascade(label="File",menu=fileMenu)
        fileMenu.add_command(label="Home", command=self.home)
        fileMenu.add_command(label="Close",command=self.landingpage)
        fileMenu.add_command(label="Exit",command=self.master.quit)

        menubar.add_cascade(label="Action",menu=actionMenu)
        actionMenu.add_command(label="Apply for Leave", command=self.applyforleave)
        actionMenu.add_command(label="Check Leave Balance", command=self.checkleavebalance)
        actionMenu.add_command(label="Withdraw Last Leave Request", command=self.withdrawleave)
        actionMenu.add_command(label="Cancel Active Leave", command=self.cancelleave)
        actionMenu.add_command(label="Update My Details", command=self.updatedetails)

        menubar.add_cascade(label="View", menu=viewMenu)
        viewMenu.add_command(label="My Details", command=self.mydetails)
        viewMenu.add_command(label="Leave History", command=self.leavehistory)

        menubar.add_cascade(label="Help", menu=helpMenu)
        helpMenu.add_command(label="About", command=self.about)
        helpMenu.add_command(label="How to use LM App", command=self.howto)
        helpMenu.add_command(label="Check for updates", command=self.checkupdate)

        self.master.config(menu=menubar)

    def home(self):
        from LM_MainMenu import MainMenu
        self.master.destroy()
        self.window = Leavemanagement()
        RegularUserMenuBar(self.window,self.userdata)
        MainMenu(self.window,self.userdata[1]+self.userdata[2])

    def landingpage(self):
        from LM_Login import LoginUser
        self.master.destroy()
        self.window = Leavemanagement()
        LoginUser(self.window)
    def applyforleave(self):
        from LM_Apply import ApplyLeave
        self.master.destroy()
        self.window = Leavemanagement()
        RegularUserMenuBar(self.window,self.userdata)
        ApplyLeave(self.window,self.userdata)
    def checkleavebalance(self):
        messagebox.showinfo(f"{self.userdata[1]}", f"You are eligible to apply for 30 leave")
    def withdrawleave(self):
        from LM_Database import leaveexist,withdraw_leave
        if leaveexist(self.userdata[0]):
            withdraw_leave(self.userdata[0])
            messagebox.showinfo("Successful", "Last Leave Applied withdrawn")
        else:
            messagebox.showinfo("No Result","You have not apply for any leave")
    def cancelleave(self):
        from LM_Database import leaveexist,withdraw_leave
        if leaveexist(self.userdata[0]):
            withdraw_leave(self.userdata[0])
            messagebox.showinfo("Successful", "Active Leave has been Canceled")
        else:
            messagebox.showinfo("No Result","You do not have any active leave")
    def updatedetails(self):
        from LM_Update_Staff import UpdateStaff
        self.master.destroy()
        self.window = Leavemanagement()
        RegularUserMenuBar(self.window, self.userdata)
        UpdateStaff(self.window, self.userdata)

    def mydetails(self):
        messagebox.showinfo(f"user {self.userdata[1]}",f"Full Name --> {self.userdata[1]} \n Email --> {self.userdata[4]}\nPhone number --> {self.userdata[3]}\nRole --> {self.userdata[5]}")

    def leavehistory(self):
        from LM_Leave_History import LeaveHistory
        self.master.destroy()
        self.window = Leavemanagement()
        RegularUserMenuBar(self.window,self.userdata)
        LeaveHistory(self.window,self.userdata)
    def about(self):
        pass
    def howto(self):
        pass
    def checkupdate(self):
        pass