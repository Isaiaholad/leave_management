from  tkinter import PhotoImage,Label

def mybg(self):
    self.phimg = PhotoImage(file="pcs.png")
    self.lblimg = Label(self.master, image=self.phimg)
    return self.lblimg

def centerimg(self):
    self.phimg2 = PhotoImage(file="lm.png")
    self.lblimg2 = Label(self.master, image=self.phimg2)
    return self.lblimg2

def userimg(self):
    self.phimg3 = PhotoImage(file="uname2.png")
    self.lblimg3 = Label(self.master, image=self.phimg3)
    return self.lblimg3

def passwordimg(self):
    self.phimg4 = PhotoImage(file="passd.png")
    self.lblimg4 = Label(self.master, image=self.phimg4)
    return self.lblimg4

def centerimg2(self):
    self.phimg5 = PhotoImage(file="logn.png")
    self.lblimg5 = Label(self.master, image=self.phimg5)
    return self.lblimg5