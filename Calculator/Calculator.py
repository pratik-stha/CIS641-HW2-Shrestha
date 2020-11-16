from tkinter import*
import Arithmetic
import UnitConversion
import Display
import Trigonometric

me=Tk()
me.geometry("500x530")
me.title("CALCULATOR APP")
melabel = Label(me,text="CALCULATOR",bg='dark gray',font=("Times",30,'bold'))
melabel.pack(side=TOP)
me.config(background='Dark gray')



Disp = Display.Display(me)
Arith = Arithmetic.Arithmetic(me,Disp)
Conv = UnitConversion.UnitConversion(me,Disp)
Trig = Trigonometric.Trigonometric(me)

me.mainloop()
