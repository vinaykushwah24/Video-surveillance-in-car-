import Tkinter
import subprocess
from Tkinter import *
import os

GUI = Tk()
GUI.geometry("250x200")
GUI.title("Screen Control")

def PHOTO():
    os.system("p1.py") 

def VIDEO():
    os.system("p2.py") 

def QUIT():
    GUI.destroy()

def SMS():
    os.system("sms.py")

def NUMBER_PLATE():
    subprocess.call(['./number.sh'])

def MAP():
    os.system("map.py")   

B1 = Button(text = "Share Photo", command = PHOTO ) 
B1.grid(row=10, column=11)


B2 = Button(text = "Share Video", command = VIDEO)
B2.grid(row=11, column=10,)


B3 = Button(text = "GUI Close", command = QUIT)
B3.grid(row=11, column=11,)


B4 = Button(text = "SMS Send", command = SMS)
B4.grid(row=11, column=12,)

B5 = Button(text = "Number plate", command = NUMBER_PLATE)
B5.grid(row=12, column=11,)

B6 = Button(text = "   MAP  ", command = MAP)
B6.grid(row=13, column=11,)

mainloop()
