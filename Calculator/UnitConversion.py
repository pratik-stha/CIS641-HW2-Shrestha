from tkinter import *
import Arithmetic
import Display

class UnitConversion:
    def __init__(self,master,disp):
        self.operator = disp.operator
        self.textin= disp.textin
        self.butconvert=Button(master,padx=14,pady=14,bd=4,bg='white',text="Convert",fg='green',command=self.convert,font=("Courier New",16,'bold'))
        self.butconvert.place(x=10,y=450)

        self.variable = StringVar(master)
        self.variable.set("Feet To Meter")
        self.w = OptionMenu(master,self.variable, "Feet to Meter","Meter to Feet")
        self.w.configure(width=15, height=3)
        self.w.place(x=200,y=450)
    
    def convert(self):
        choice=self.variable.get()
        if(choice == "Feet to Meter"):
            self.FeetToMeter()
        else:
            self.MeterToFeet()


    def FeetToMeter(self):
        try:
            val = 0.3048*float(self.textin.get())
            #val=self.textin.get()
            self.textin.set(str(val)+" m")
            print(val)
           
        except:
            self.textin.set("Enter valid value")

    def MeterToFeet(self):
        try:
            val = 3.2804*float(self.textin.get())
            #val=self.textin.get()
            self.textin.set(str(val)+" f")
            print(val)
            
        except:
            self.textin.set("Enter valid value")
            