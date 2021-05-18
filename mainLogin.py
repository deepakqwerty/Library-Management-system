import sys
import os
from tkinter import *
from PIL import ImageTk
from tkinter import ttk,messagebox
import sqlite3

con = sqlite3.connect('library.db')
cur = con.cursor()


class LoginSystem:
    def __init__(self,root):
        self.root = root
        self.root.title("Library Login System")
        self.root.geometry("1350x700+0+0")

        #--------Images-----------------
        self.bg_icon = ImageTk.PhotoImage(file="icons/bg.jpg")
        self.user_icon = ImageTk.PhotoImage(file="icons/userlogo.JPG")
        self.pass_icon = ImageTk.PhotoImage(file="icons/passlogo.JPG")
        self.logo_icon = ImageTk.PhotoImage(file="icons/mainlogo.JPG")

        #--------variables(Username and saved passwords)--------





        bg_lbl = Label(self.root, image=self.bg_icon).pack()
        title = Label(self.root,text="Library Login",font=("times new roman",40,"bold"),bg="Orange",fg="red",relief=GROOVE)
        title.place(x=0,y=0,relwidth=1)

        Login_Frame = Frame(self.root,bg="white")
        Login_Frame.place(x=400,y=150)

        logolbl = Label(Login_Frame,image=self.logo_icon,bd=0).grid(row=0,columnspan=2,pady=20)

        lbluser = Label(Login_Frame,text="Username",image=self.user_icon,compound=LEFT,font=("times new roman",20,"bold")).grid(row=1,column=0,padx=20,pady=10)
        self.txtuser = Entry(Login_Frame,bd = 5,relief=GROOVE,font=("",15))
        self.txtuser.grid(row=1,column=1,padx=20)

        lblpass = Label(Login_Frame,text="Password",image=self.pass_icon,compound=LEFT,font=("times new roman",20,"bold")).grid(row=2,column=0,padx=20,pady=10)
        self.txtpass = Entry(Login_Frame,bd = 5,show="*",relief=GROOVE,font=("",15))
        self.txtpass.grid(row=2,column=1,padx=20)

        btn_log = Button(Login_Frame,text="Login",width=15,font=("times new roman",14,"bold"),bg="orange",fg="red",command=self.log_in).grid(row=3,column=1,pady=10)


    def log_in(self):
        name1 = self.txtuser.get()
        pass1 = self.txtpass.get()
        if self.txtuser.get()=="" or self.txtpass.get()=="":
            messagebox.showerror("Error","All Fields Are Required",parent = self.root)


        #----------- Check Entry From Database-------------------

        search = cur.execute("SELECT * FROM members WHERE name LIKE ? AND password LIKE ?",(name1,pass1)).fetchall()
        print(search)
        if search:
                   try:
                       root.destroy()
                       os.system('python main.py')
                   except:
                       messagebox.showerror("Error","Unable to login",icon='warning')
        else:
            messagebox.showerror("Error","No such member exists",icon='warning')

            con.close()


root = Tk()
obj = LoginSystem(root)
root.mainloop()
