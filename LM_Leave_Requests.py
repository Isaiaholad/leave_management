from  tkinter import *
from  tkinter import messagebox
from LM_Images import mybg
from LM_Database import getAllRequest,getuserbyid,acceptLeave,active_leave

class LeaveRequests(Frame):
    def __init__(self, master):
        super(LeaveRequests, self).__init__(master)
        self.master.title("LEAVE MANAGEMENT APP")
        self.userdata = []
        self.grid()
        self.create_widgets()

    def create_widgets(self):
        mybg(self).place(x=0, y=0)

        self.lblHeader = Label(self.master, text="Hazzi Commz .inc Leave App", font=("Elephant", 20, "bold"), fg="#999").place(x=50, y=5)

        from LM_Tables import MyTable

        _,leaveRequests = getAllRequest(("pending","","","",""))

        self.LRT = MyTable(self.master,"Staff Name", "Type of leave", "Start Date","End Date","Date Applied","Reason")
        self.requestTable = self.LRT.gettable()

        self.ws = False
        self.tplvl = False
        self.btcnt = 0

        for col in ("Staff Name", "Type of leave", "Start Date", "End Date","Date Applied","Reason"):
            self.requestTable.column(col, anchor=CENTER, width=90, minwidth=90)
            self.requestTable.bind("<Button-1>",self.disableresize)

        for c, request in enumerate(leaveRequests):
            self.request = list(request)
            username = list(getuserbyid(self.request[1]))[1] + list(getuserbyid(self.request[1]))[2]
            self.LRT.addData(c, [username , self.request[4],self.request[2], self.request[3], (self.request[7])[:16], self.request[5]])

    def disableresize(self, ev):
        if ev.y < 20:
            if not self.ws:
                self.requestTable.column(self.requestTable.identify_column(ev.x), width=170)
                self.ws = True
            elif self.ws:
                self.requestTable.column(self.requestTable.identify_column(ev.x), width=100)
                self.ws = False

            if self.requestTable.identify_region(ev.x, ev.y) == "separator":
                return "break"
        elif ev.y >20:
            self.btcnt +=1
            if self.btcnt>=2:
                self.request_selected()

    def request_selected(self):
        sel = self.requestTable.focus()
        sel = self.requestTable.item(sel)["values"]
        sel = list(sel)
        print(sel)
        if not self.tplvl:
            self.decisionwindow = Toplevel(self.master,width=320,height=150)
            self.decisionwindow.title(sel[0]+"  LEAVE REQUEST ")
            Label(self.decisionwindow, text=f"{sel[1]} leave between {sel[2]} and {sel[3]}").place(x=70, y=15)
            Label(self.decisionwindow,text ="Would you like to accept or reject this request").place(x=50,y=30)
            self.btnapprove = Button(self.decisionwindow, text="approve", command=self.approve, font=("Arial", 10),bg="blue", fg="pink").place(x=70, y=70)
            self.decline = Button(self.decisionwindow, text="decline", command=self.decline, font=("Arial", 10),bg="blue", fg="pink").place(x=170, y=70)
            self.tplvl = True

    def approve(self):
        active_leave(self.request[1])
        messagebox.showinfo("REQUEST ACCEPTED",f"{self.request[0]} {self.request[1]} leave request has been accepted and active")
        #acceptLeave(self.request[1],self.request[])
    def decline(self):
        messagebox.showinfo("REQUEST DECLINED",f"{self.request[0]} {self.request[1]} leave request has been declined")
