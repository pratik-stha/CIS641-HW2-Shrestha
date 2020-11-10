from tkinter import *
import Arithmetic
import Display

class UnitConversion:
    def __init__(self,master,disp):
        self.operator = disp.operator
        self.textin= disp.textin
        self.butconvert=Button(master,padx=14,pady=14,bd=4,bg='white',text="FeetToMeter",fg='green',command=self.FeetToMeter,font=("Courier New",16,'bold'))
        self.butconvert.place(x=10,y=450)
    
    def FeetToMeter(self):
        try:
            val = 0.3048*float(self.textin.get())
            #val=self.textin.get()
            self.textin.set(val)
            print(val)
           
            
            
        except:
            self.textin.set("Enter valid value")
        