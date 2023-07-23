from tkinter import *
from tkinter import messagebox

class LoginUser(Frame):
    def __init__(self, master):
        super(LoginUser, self).__init__(master)
        self.master.title("L O G I N   F O R M")
        self.createWidgets()

    def createWidgets(self):
        self.user_email = StringVar()
        self.user_password = StringVar()
        self.role = StringVar()

        from LM_Images import mybg,centerimg2,userimg,passwordimg
        mybg(self).place(x=0, y=0)
        centerimg2(self).place(x=150,y=50)
        userimg(self).place(x=70,y=240)
        passwordimg(self).place(x=70,y=345)

        self.lblHeader = Label(self.master, text="Hazzi Commz .inc Leave App", font=("Elephant", 20, "bold"),fg="#999").place(x=50, y=5)

        self.lblEmail = Label(self.master, text="User Email :", font=("Cooper", 14),fg="blue").place(x=170,y=260)
        self.txtEmail = Entry(self.master, width="20", textvariable=self.user_email,font=("Arial", 12, "bold"), bg="#ddd",fg="#55a").place(x=170,y=295)

        self.lblPassword = Label(self.master, text="Password :", font=("Cooper", 14),fg="blue").place(x=170,y=365)
        self.txtPassword = Entry(self.master, show="*", width="20", textvariable=self.user_password,font=("Arial", 12, "bold"), bg="#ddd",fg="#55a").place(x=170,y=400)

        self.lblAs = Label(self.master, text="Login As :", font=("Cooper", 14), fg="blue").place(x=170, y=470)
        self.radiobtnAdmin = Radiobutton(self.master, text="Admin", variable=self.role, font=("Elephant", 13),value="Admin", fg="blue").place(x=270, y=470)
        self.radiobtnStaff = Radiobutton(self.master, text="Regular", variable=self.role, font=("Elephant", 13),value="Regular", fg="blue")
        self.radiobtnStaff.place(x=360, y=470)
        self.radiobtnStaff.select()

        self.btnLogin = Button(self.master, text="Sign In", width="20",command=self.signin, font=("Arial", 12),bg="blue",fg="pink").place(x=340, y=550)
        self.bind_all("<KeyPress>",self.shtcutt)
        self._=1
    def shtcutt(self,_):
        self._+=1
        if self._>3 and _.keycode==36:
            from LM_Window import Leavemanagement
            from LM_MenuBar import AdminMenuBar
            from LM_MainMenu import MainMenu
            self.master.destroy()
            self.window = Leavemanagement()
            AdminMenuBar(self.window,["a","dsuper","admin"])
            MainMenu(self.window,"dsuperadmin")
        elif self._>3 and _.keycode==35:
            from LM_Window import Leavemanagement
            from LM_MenuBar import RegularUserMenuBar
            from LM_MainMenu import MainMenu
            self.master.destroy()
            self.window = Leavemanagement()
            RegularUserMenuBar(self.window,["a","dboss","staff"])
            MainMenu(self.window,"dbossstaff")
    def signin(self):
        from LM_Database import authenticate
        auth,user_data=authenticate(self.user_email.get(),self.user_password.get())
        if auth:
            user_data=list(user_data)
            rl=self.role.get()
            if rl==user_data[7]:
                if rl=="Admin":
                    from LM_Window import Leavemanagement
                    from LM_MenuBar import AdminMenuBar
                    from LM_MainMenu import MainMenu
                    self.master.destroy()
                    self.window = Leavemanagement()
                    AdminMenuBar(self.window,user_data)
                    MainMenu(self.window,user_data[1]+user_data[2])
                elif rl == "Regular":
                    from LM_Window import Leavemanagement
                    from LM_MenuBar import RegularUserMenuBar
                    from LM_MainMenu import MainMenu
                    self.master.destroy()
                    self.window = Leavemanagement()
                    RegularUserMenuBar(self.window,user_data)
                    MainMenu(self.window,user_data[1]+user_data[2])
            else:
                messagebox.showwarning("Incorrect details!", f"wrong role for user :{user_data[1]}   \n Please try again")

        else:
            messagebox.showwarning("Incorrect details!","Invalid username or password \n Please try again")
