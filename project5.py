import os
from tkinter import messagebox, Label, Button, FALSE, Tk, Entry

username = ("Tom")
password = ("")


def try_unlock():
   
    x = password_guess.get()
    if x == ("password"):
        os.startfile("txtfilelock.docx")
    else:
        wrong_text = Label(window, text="Wrong Password")
        wrong_text.pack()


#Gui Things
window = Tk()
window.resizable(width=FALSE, height=FALSE)
window.title("File Lock")
window.geometry("300x105")

#Creating the username & password entry boxes
username_text = Label(window, text="")

password_text = Label(window, text="Password:")
password_guess = Entry(window, show="*")
wrong_text = Label()
#attempt to login button
unlock = Button(text="Unlock", command=try_unlock)
 
username_text.pack()

password_text.pack()
password_guess.pack()
unlock.pack()

#Main Starter
window.mainloop()

  

