from tkinter import *
from tkinter import ttk
from tkinter import messagebox

frame = Tk()
frame.geometry('400x100+100+100')
frame.title("Condom Calculator")

# function
def calculator():
    # declare varible for storage from user
    message = ""
    girth = int(GIRTH.get())
    
    if girth == 0:
        message = "Error!! Enter more than 1"
    elif girth <= 110:
        message = "Oops!!! You have a small cock 5555555."
    elif girth <= 120:
        message = "49 mm."
    elif girth <= 130:
        message = "52 mm."
    elif girth <= 140:
        message = "54 mm."
    elif girth <= 150:
        message = "56 mm."
    elif girth >= 151:
        message = "Oh !!! You have a big cock."
    
    messagebox.showinfo("", message)
       
    

# label, input girth from user
lb_Grith = Label(frame, text="ป้อนเส้นรอบวงของคุณ (มิลลิเมตร): ").pack()
# StringVar
GIRTH = StringVar()
ent_Girth = Entry(frame, textvariable = GIRTH, width = 30).pack()
# click to calculator
btn_Cal = ttk.Button(frame, text="Calculator", command=calculator).pack()

# Show screen
frame.mainloop()
