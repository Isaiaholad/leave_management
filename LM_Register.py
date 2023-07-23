from tkinter import *
from tkinter import messagebox
import LM_Database
import os

class RegisterUser(Frame):
    def __init__(self, master,data=[],id=0):
        super(RegisterUser, self).__init__(master)
        self.grid()
        self.id = id
        if os.path.isfile('LM_DB.db') is False:
            LM_Database.create_database()
        self.create_widgets()
        if data:
            self.fstname.set(data[1])
            self.lstname.set(data[2])
            self.phone.set(data[3])
            self.email.set(data[4])
            self.desig.set(data[5])
            self.usrgender.set(data[8])
            self.passw.set(data[6])
            self.passwc.set(data[6])
            self.role.set(data[7])
            self.btnRegister = Button(self.master, text="Update", width="20", command=self.updatefcn, font=("Arial", 12),bg="blue",fg="pink").place(x=200, y=550)
        else:
            self.btnRegister = Button(self.master, text="Register", width="20", command=self.registerfcn,font=("Arial", 12), bg="blue", fg="pink").place(x=200, y=550)
    def create_widgets(self):
        self.fstname = StringVar()
        self.lstname = StringVar()
        self.phone = StringVar()
        self.email = StringVar()
        self.desig = StringVar()
        self.usrgender = StringVar()
        self.passw = StringVar()
        self.passwc = StringVar()
        self.role = StringVar()

        from LM_Images import mybg
        mybg(self).place(x=0,y=0)
        self.lblHeader = Label(self.master, text="Hazzi Commz .inc Leave App", font=("Elephant", 20, "bold"), fg="#999").place(x=50, y=5)
        self.lblInstr = Label(self.master, text="Please enter New details of Staff", font=("Ebrima", 10,),fg="#444").place(x=15, y=50)

        self.logindetailframe = LabelFrame(self.master, text="Login Details",width=450,height=220).place(x=40, y=80)

        self.lblEmail = Label(self.logindetailframe, text="Email", font=("Elephant", 10), fg="#555").place(x=70, y=120)
        self.entryEmail = Entry(self.logindetailframe, width="20", textvariable=self.email, font=("Ebrima", 9))
        self.entryEmail.place(x=70, y=150)

        self.lblRole = Label(self.master, text="Role", font=("Elephant", 10), fg="#555").place(x=300, y=120)
        self.radiobtnAdmin = Radiobutton(self.master, text="Admin", variable=self.role, font=("Elephant", 10),value="Admin", fg="#555").place(x=270, y=150)
        self.radiobtnStaff = Radiobutton(self.master, text="Staff", variable=self.role, font=("Elephant", 10),value="Regular", fg="#555")
        self.radiobtnStaff.place(x=350, y=150)
        self.radiobtnStaff.select()

        self.lblPassword = Label(self.logindetailframe, text="Password", font=("Elephant", 10), fg="#555").place(x=70,y=220)
        self.entryPassword = Entry(self.logindetailframe, width="20", textvariable=self.passw, show="*",font=("Ebrima", 9)).place(x=70, y=250)

        self.lblCpassword = Label(self.logindetailframe, text="Verify Password", font=("Elephant", 10),fg="#555").place(x=300,y=220)
        self.entryCpassword = Entry(self.logindetailframe, width="20", textvariable=self.passwc, show="*",font=("Ebrima", 9)).place(x=280, y=250)

        self.personaldetailframe = LabelFrame(self.master, container=True, text="Personal Details",width=450,height=230).place(x=40, y=300)

        self.lblFstname = Label(self.personaldetailframe, text="First Name", font=("Elephant", 10),fg="#555").place(x=70, y=320)
        self.entryFstname = Entry(self.personaldetailframe, width="25", textvariable=self.fstname,font=("Ebrima", 9)).place(x=70, y=350)

        self.lblLstname = Label(self.personaldetailframe, text="Last Name", font=("Elephant", 10),fg="#555").place(x=330, y=320)
        self.entryLstname = Entry(self.personaldetailframe, width="25", textvariable=self.lstname,font=("Ebrima", 9)).place(x=320, y=350)

        self.lblPhone = Label(self.personaldetailframe, text="Phone", font=("Elephant", 10),fg="#555").place(x=70, y=380)
        self.entryPhone = Entry(self.personaldetailframe, width="20",textvariable=self.phone, font=("Ebrima", 9)).place(x=70, y=400)

        self.lblGender = Label(self.personaldetailframe, text="Gender", font=("Elephant", 10),fg="#555").place(x=330, y=380)
        self.radiobtnMale = Radiobutton(self.personaldetailframe, text="Male",variable=self.usrgender,font=("Elephant", 10),fg="#555", value="Male")
        self.radiobtnMale.place(x=300, y=400)
        self.radiobtnFemale = Radiobutton(self.personaldetailframe, text="Female",variable=self.usrgender,font=("Elephant", 10),fg="#555", value="Female").place(x=380, y=400)
        self.radiobtnMale.select()

        self.lblDesignation = Label(self.personaldetailframe, text="Designation", font=("Elephant", 10),fg="#555").place(x=70, y=430)
        self.cmboxDesignation = Spinbox(self.personaldetailframe, width=18,textvariable=self.desig, values=["Security", "Receiptionist", "Clerk", "Manager"]).place(x=70, y=450)


    def registerfcn(self):
        fn = self.fstname.get()
        ln = self.lstname.get()
        ph = self.phone.get()
        em = self.email.get()
        dn = self.desig.get()
        gn = self.usrgender.get()
        pw = self.passw.get()
        pwc = self.passwc.get()
        rl = self.role.get()
        if pw==pwc:
            response=LM_Database.add_new(fn, ln, ph, em, dn, pw, rl, gn)
            if response is True:
                messagebox.showinfo("Registration Successful",f"{fn} is successfully registered")
            elif response is False:
                messagebox.showwarning("registration failed!","Error adding details to database \n Invalid details or user details alredy exist \n")
        else:
            messagebox.showwarning("Incorrect details!","Password is different from confirm password \n Please try again")
    def updatefcn(self):
        fn = self.fstname.get()
        ln = self.lstname.get()
        ph = self.phone.get()
        em = self.email.get()
        dn = self.desig.get()
        gn = self.usrgender.get()
        pw = self.passw.get()
        pwc = self.passwc.get()
        rl = self.role.get()

        if pw==pwc:
            response=LM_Database.update_staff(fn, ln, ph, em, dn, pw, rl, gn, self.id)
            if response is True:
                messagebox.showinfo("Update Successful",f"{fn} is successfully updated")
            elif response is False:
                messagebox.showwarning("Update failed!","Error adding details to database \n Invalid details or user details alredy exist \n")
        else:
            messagebox.showwarning("Incorrect details!","Password is different from confirm password \n Please try again")

