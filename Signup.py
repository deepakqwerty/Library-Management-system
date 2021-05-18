import sys
import os
from tkinter import *
from tkinter import ttk,messagebox
from PIL import ImageTk
import sqlite3

con = sqlite3.connect('library.db')
cur = con.cursor()

class Login:
    def __init__(self,root):
        self.root = root
        self.root.title("Library Login")
        self.root.geometry("1199x600+100+50")

        #-------Background Image----------

        self.bg=ImageTk.PhotoImage(file="icons/lib.jpg")
        self.bg_image = Label(self.root,image=self.bg).place(x=0,y=0,relwidth=1,relheight=1)

        #----Register Frame---

        frame1 = Frame(self.root,bg="white")
        frame1.place(x=480,y=100,width=700,height=500)

        title = Label(frame1,text="Register Here",font=("times new roman",20,"bold"),bg="white",fg="green").place(x=50,y=30)

        # ------------------------------------------Row1

        f_name = Label(frame1,text="First Name",font=("times new roman",15,"bold"),bg="white",fg="gray").place(x=50,y=100)
        self.txt_fname = Entry(frame1,font=("times new roman",15),bg="lightgray")
        self.txt_fname.place(x=50, y=130, width=250)

        l_name = Label(frame1, text="Last Name", font=("times new roman", 15, "bold"), bg="white", fg="gray").place(x=370, y=100)
        self.txt_lname = Entry(frame1, font=("times new roman", 15), bg="lightgray")
        self.txt_lname.place(x=370, y=130, width=250)


        # ------------------------------------------Row2

        contact = Label(frame1, text="Contact No.", font=("times new roman", 15, "bold"), bg="white", fg="gray").place(x=50, y=190)
        self.txt_contact = Entry(frame1, font=("times new roman", 15), bg="lightgray")
        self.txt_contact.place(x=50, y=220, width=250)

        email = Label(frame1, text="Email", font=("times new roman", 15, "bold"), bg="white", fg="gray").place(x=370, y=190)
        self.txt_email = Entry(frame1, font=("times new roman", 15), bg="lightgray")
        self.txt_email.place(x=370, y=220, width=250)

        # ------------------------------------------Row3

        password = Label(frame1, text="Password", font=("times new roman", 15, "bold"), bg="white", fg="gray").place(x=50, y=280)
        self.txt_password = Entry(frame1, font=("times new roman", 15), bg="lightgray",show="*")
        self.txt_password.place(x=50, y=310, width=250)

        cpassword = Label(frame1, text="Confirm Password", font=("times new roman", 15, "bold"), bg="white", fg="gray").place(x=370,y=280)
        self.txt_cpassword = Entry(frame1, font=("times new roman", 15), bg="lightgray",show="*")
        self.txt_cpassword.place(x=370, y=310, width=250)

        #--------Terms-----
        self.var_chk = IntVar()
        chk =Checkbutton(frame1,text="I Agree The Terms & Conditions",variable=self.var_chk,onvalue=1,offvalue=0,bg="white",font=("times new roman",12)).place(x=50,y=350)

        self.btn_image=ImageTk.PhotoImage(file='icons/register.jpg')
        btn_register = Button(frame1,image=self.btn_image,bd=0,cursor="hand2",command=self.register_data).place(x=50,y=400)

        self.btn_image2 = ImageTk.PhotoImage(file='icons/signin.jpg')
        btn_log = Button(frame1, image=self.btn_image2, bd=0, cursor="hand2",command=self.GOTO).place(x=400, y=400)



    def GOTO(self):
        root.destroy()
        os.system('python mainLogin.py')



    def register_data(self):

         if self.txt_fname.get()!="" or self.txt_email.get()!="" or self.txt_password.get()!="" or self.txt_cpassword.get()!="" or self.txt_contact.get()!="":
                 name1 = self.txt_fname.get()
                 email1 = self.txt_email.get()
                 password1 = self.txt_cpassword.get()


         if self.txt_password.get() != self.txt_cpassword.get():
             messagebox.showerror("Error ","Password and Confirm Password Are Not Same")

         elif self.var_chk.get()==0:
             messagebox.showerror("Error", "You Should To The Terms And Conditions", parent=self.root)

         elif(self.txt_password!=""):
                    try:
                        query = "INSERT INTO 'members' VALUES(?,?,?)"
                        cur.execute(query,(name1,email1,password1))
                        con.commit()
                        messagebox.showinfo("Success","Successfully added to database",icon='info',parent=self.root)
                    except:
                        messagebox.showerror("Error","Cant add to database",icon='warning')









root = Tk()
obj = Login(root)
root.mainloop()
