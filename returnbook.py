from tkinter import *
from tkinter import ttk
import sqlite3
from tkinter import messagebox

con = sqlite3.connect('library.db')
cur = con.cursor()

class ReturnBook(Toplevel):
   def __init__(self):
       Toplevel.__init__(self)
       self.geometry("800x800+400+600")
       self.title("Return Book")
       self.resizable(False,False)


       # Top Frame
       self.topFrame = Frame(self, height=150, bg='yellow')
       self.topFrame.pack(fill=X)

       # Bottom Frame
       self.bottomFrame = Frame(self, height=600, bg='#fcc324')
       self.bottomFrame.pack(fill=X)

       # id
       self.lbl_page = Label(self.bottomFrame, text=' ID : ', font='arial 15 bold', fg='white', bg='#fcc324')
       self.lbl_page.place(x=400, y=800)
       self.ent_page = Entry(self.bottomFrame, width=30, bd=4)
       self.ent_page.insert(0, 'Please enter book id')
       self.ent_page.place(x=150, y=125)

       # Button
       button = Button(self.bottomFrame, text=' Return Book ',command=self.returnBook)
       button.place(x=220, y=120)

   def returnBook(self):
       book_id = self.ent_page.get()

       if (book_id != ""):
           try:
               query = "DELETE FROM 'borrows' WHERE bbook_id = (?)"
               cur.execute(query, (book_id))
               con.commit()
               messagebox.showinfo("Success", "Book is returned to Library", icon='info')
               cur.execute("UPDATE books SET book_status = ? WHERE book_id =?", (0, book_id))
               con.commit()
           except:
               messagebox.showerror("Error", "Cant return book", icon='warning')
       else:

           messagebox.showerror("Error", "Fields cant be empty", icon='warning')

