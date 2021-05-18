from tkinter import *
from tkinter import ttk
import sqlite3
from tkinter import messagebox

con = sqlite3.connect('library.db')
cur = con.cursor()

class GiveBook(Toplevel):
   def __init__(self):
       Toplevel.__init__(self)
       self.geometry("800x800+400+600")
       self.title("Lend Book")
       self.resizable(False,False)
       global given_id
       self.book_id = int(given_id)
       query = "SELECT * FROM books WHERE book_status=0"
       books = cur.execute(query).fetchall()
       book_list=[]
       for book in books:
           book_list.append(str(book[0])+"-"+book[1])


       # Top Frame
       self.topFrame = Frame(self, height=150, bg='yellow')
       self.topFrame.pack(fill=X)

       # Bottom Frame
       self.bottomFrame = Frame(self, height=600, bg='#fcc324')
       self.bottomFrame.pack(fill=X)

       # name
       self.book_name = StringVar()
       self.lbl_name = Label(self.bottomFrame, text='Name :', font='arial 15 bold', fg='white', bg='#fcc324')
       self.lbl_name.place(x=40, y=40)
       self.combo_name = ttk.Combobox(self.bottomFrame,textvariable=self.book_name)
       self.combo_name.place(x=150,y=45)

       # Button
       button = Button(self.bottomFrame, text=' Lend Book',command=self.lendBook)
       button.place(x=220, y=120)

   def lendBook(self):
       book_name=self.book_name.get()
       self.book_id = book_name.split('-')[0]

       if(book_name !=""):
           try:
               query="INSERT INTO 'borrows' (bbook_id) VALUES(?)"
               cur.execute(query,(self.book_id))
               con.commit()
               messagebox.showinfo("Success","Successfully added to database:",icon='info')
               cur.execute("UPDATE books SET book_status = ? WHERE book_id= ?",(1,self.book_id))
               con.commit()
           except:
               messagebox.showerror("Error", "Cant add to database", icon='warning')

       else:
           messagebox.showerror("Error","Fields cant be empty",icon='warning')

