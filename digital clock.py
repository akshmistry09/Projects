from tkinter import *
from tkinter.ttk import *

from time import strftime

root =Tk()
root.title("Digital Clock")


def time():
    string = strftime('%H:%M:%S %p')
    label.config(text=string) 
    label.after(1000, time)

label = Label(root, font=("ds-digital", 100), background= "black", foreground= "white")
label.pack(anchor='center')
time()

mainloop()
# python Aks.py
# dir -> show all directories
# cd -> change directory
# folder means directory

#for CMD Prompt
# iomprt os
#clear = lambda: os.system('clear')
# clear()