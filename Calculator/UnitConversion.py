from tkinter import *
from tkinter import ttk 
import Arithmetic
import Display

class UnitConversion:
    def __init__(self,master,disp):
        self.operator = disp.operator
        self.textin= disp.textin
        self.butconvert=Button(master,padx=14,pady=14,bd=4,bg='green',text="Convert",fg='yellow',command=lambda:self.convert(self.textin.get()),font=("Courier New",16,'bold'))
        self.butconvert.place(x=10,y=450)

        self.variable = StringVar(master)
        self.variable.set("Feet to Meter")
        self.w = OptionMenu(master,self.variable, "Feet to Meter","Meter to Feet")
        self.w.configure(width=15, height=3)
        self.w.place(x=200,y=450)
        
      

    def convert(self,num):
        choice=self.variable.get()
        if(choice == "Feet to Meter"):
            self.FeetToMeter(num)
        else:
            self.MeterToFeet(num)


    def FeetToMeter(self,num):
        try:
            #val = 0.3048*float(self.textin.get())
            #self.textin.set("")
            #self.textin.set(str(val)+" m")
            self.operator=""
            self.textin.set("")
            #val=self.textin.get()
            print(num)
           
        except:
            self.textin.set("Enter valid value")

    def MeterToFeet(self,num):
        try:
            val = 3.2804*float(self.textin.get())
            #val=self.textin.get()
            self.textin.set(str(val)+" f")
            print(val)
            
        except:
            self.textin.set("Enter valid value")
            