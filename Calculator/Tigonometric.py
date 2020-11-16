from tkinter import *

class Trigonometric:
    def __init__(self,master,disp):
        labelframe = LabelFrame(master, text="Trigonometric",padx=50,pady=50)
        labelframe.pack(padx=50, pady=50)
        self.butconvert=Button(master,padx=14,pady=14,bd=4,bg='green',text="Convert",fg='yellow',command=self.convert,font=("Courier New",16,'bold'))
        self.butconvert.place(x=300,y=50)
