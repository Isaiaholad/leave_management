from  tkinter import *
from tkinter.ttk import Treeview,Style,Scrollbar
from LM_Images import mybg

class MyTable(Frame):
    def __init__(self, master,*ags):
        self.columnlist=[]
        for ag in ags:
            self.ag = ag
            self.columnlist.append(self.ag)

        super(MyTable, self).__init__(master)
        self.create_widgets()

    def create_widgets(self):
        self.ws = False
        mystyl = Style()
        mystyl.configure("mystyle.Treeview", font=("Segoe", 8))
        mystyl.configure("mystyle.Treeview.Heading", background="blue", font=("Segoe", 10, "bold"))
        mystyl.layout("mystyle.Treeview", [("mystyle.Treeview.treearea", {"sticky": "nsew"})])

        self.stafftable = Treeview(self.master, height=20, style="mystyle.Treeview")
        self.stafftable.place(x=40, y=130)
        self.mycolumn = tuple(self.columnlist)
        self.stafftable["columns"] = self.mycolumn

        self.stafftable.column("#0", width=0,stretch=NO)
        self.stafftable.heading("#0", text="", anchor=CENTER)

        self.horizontalscrollbar = Scrollbar(self.master,orient="horizontal",command=self.stafftable.xview)
        self.verticalscrollbar = Scrollbar(self.master, orient="vertical", command=self.stafftable.yview)
        self.horizontalscrollbar.place(x=40,y=538,width=500)
        self.verticalscrollbar.place(x=540, y=130, height=410)
        self.stafftable.configure(xscrollcommand=self.horizontalscrollbar.set,yscrollcommand=self.verticalscrollbar.set)

        for column in (self.mycolumn):
            self.stafftable.column(column, anchor=CENTER, width=80,minwidth=80)
        for column in (self.mycolumn):
            self.stafftable.heading(column, text=column.upper(), anchor=CENTER)

        self.stafftable.bind("<Button-1>", self.disableresize)
        #self.stafftable.bind("<Motion>", self.disableresize)

    def disableresize(self, ev):
        if ev.y <20:
            if not self.ws:
                self.stafftable.column(self.stafftable.identify_column(ev.x),width=170)
                self.ws=True
            elif self.ws:
                self.stafftable.column(self.stafftable.identify_column(ev.x), width=100)
                self.ws = False

            if self.stafftable.identify_region(ev.x, ev.y) == "separator":
                return "break"

    def addData(self,ind=0,data=[]):
        datas=tuple(data)
        self.stafftable.insert("",index=ind,iid=ind,text="",values=datas)
    def gettable(self):
        return self.stafftable


