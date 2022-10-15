#!/usr/bin/python3
'''
Author  : Sundararajan T
Version : v0.0.1
Name    : Password Hatch

'''

from tkinter import *
import secrets
import string
import pyperclip as pc

#functions
def generatePass():
    password_length = slide_val.get()
    numbers = chkvar1.get()
    strings = chkvar2.get()
    chars = chkvar3.get()
        
    if numbers:
        resultlbl.configure(text="")
        if numbers and strings and chars:
            #Numbers and String and Chars
            phrase = string.digits + string.ascii_letters + string.punctuation
            password = ''.join(secrets.choice(phrase) for i in range(int(password_length)))
            pwd.set(str(password))
        elif numbers and strings:
            #Numbers and Strings
            phrase = string.digits + string.ascii_letters
            password = ''.join(secrets.choice(phrase) for i in range(int(password_length)))
            pwd.set(str(password))
        elif numbers and chars:
            #Numbers and Chars
            phrase = string.digits + string.punctuation
            password = ''.join(secrets.choice(phrase) for i in range(int(password_length)))
            pwd.set(str(password))
        else:
            #Numbers only
            phrase = string.digits
            password = ''.join(secrets.choice(phrase) for i in range(int(password_length)))
            pwd.set(str(password))

    elif strings:
        resultlbl.configure(text="")
        if strings and chars:
            #Strings and Chars
            phrase = string.ascii_letters + string.punctuation
            password = ''.join(secrets.choice(phrase) for i in range(int(password_length)))
            pwd.set(str(password))
        else:
            #strings only
            phrase = string.ascii_letters
            password = ''.join(secrets.choice(phrase) for i in range(int(password_length)))
            pwd.set(str(password))
    
    elif chars:
        resultlbl.configure(text="")
        #"only Chars"
        phrase = string.punctuation
        password = ''.join(secrets.choice(phrase) for i in range(int(password_length)))
        pwd.set(str(password))
    else:
        resultlbl.configure(text="Choose atleast one option")

def copy_password():
    pc.copy(pwd.get())
    resultlbl.configure(text="Password Copied")


#Vars
app = Tk()
app.geometry("510x265+500+100")
app.title("Hatch Strong Passwords")

#variables
pwd = StringVar()
chkvar1 = BooleanVar()
chkvar2 = BooleanVar()
chkvar3 = BooleanVar()
slide_val = StringVar()

#Frames
topframe = Frame(app)
topframe.pack()
bottomframe = Frame(app, width=475)
bottomframe.pack()

#Widgets
pwdLbl = Label(topframe, text='Hatched Password')
pwdLbl.grid(row=0,column=0, padx=10, pady=10, sticky=W)
pwdEnt = Entry(topframe, text=pwd, width=28)
pwdEnt.grid(row=0,column=1)
copybtn = Button(topframe, text="Copy Password", command=copy_password)
copybtn.grid(row=0, column=2)


slide1 = Scale(bottomframe, from_=6, to=30, orient=HORIZONTAL, length=490, variable=slide_val)
slide1.grid(row=1, columnspan=3)

chk1 = Checkbutton(bottomframe, text="Include Numbers", variable=chkvar1, onvalue = True, offvalue=False, height=1)
chk2 = Checkbutton(bottomframe, text="Include Alphabets", variable=chkvar2, onvalue = True, offvalue=False, height=1)
chk3 = Checkbutton(bottomframe, text="Include Special Characters", variable=chkvar3, onvalue = True, offvalue=False, height=1)

chk1.grid(row=2, column=0, sticky=W)
chk2.grid(row=3, column=0, sticky=W)
chk3.grid(row=4, column=0, sticky=W)

generateBtn = Button(bottomframe, text="Hatch", width=58, command=generatePass)
generateBtn.grid(row=5, columnspan=3, padx=8, pady=8)

resultlbl = Label(bottomframe, text='')
resultlbl.grid(row=6, columnspan=3, padx=15, pady=15)

app.mainloop()