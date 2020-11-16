from tkinter import *

class Display:
    def __init__(self, master):
        self.operator=""
        self.textin = StringVar(master)
        self.textin.set("")
        self.metext=Entry(master,font=("Courier New",12,'bold'),textvariable=self.textin,width=25,bd=5,bg='powder blue')
        self.metext.pack()

        