#start of the code
from tkinter import *           #import tkinter libraries       
import tkinter.messagebox       #import tkinter messagebox

root = Tk()                     #open window
root.title("BMI")               #window title
root.resizable (width=False, height = False)    #fixed size of the window

#Window Size
widthwindow = 620
heightwindow = 220

screenwidth =root.winfo_screenwidth()
screenheight =root.winfo_screenheight()

xcoordinate = (screenwidth/2)-(widthwindow/2)
ycoordinate = (screenheight/2)-(heightwindow/2)

root.geometry("%dx%d+%d+%d" % (widthwindow, heightwindow, xcoordinate, ycoordinate))

#Window Title
title = Label(root, text = "Body Mass Index", font="Arial 20 bold")
title.grid(row=0, column = 2)

#Text Label
weight = Label(root, text ="Weight/kg: ", width = 10)
height = Label(root, text ="Height/m: ", width = 10)
result = Label(root, text ="Click for the result: ", width = 15, font="Arial 10 bold")

#Displaying Text
weight.grid(row = 1, column=0, stick = E)
height.grid(row = 1, column=2, stick = E)
result.grid(row = 2, column=1)

#Field Entry
weightfield = Entry(root)
heightfield = Entry(root)

#Displaying Field Entry
weightfield.grid(row =1, column = 1)
heightfield.grid(row =1, column = 3)

#BMI Result Label
result = Label(root, text = "BMI Result: ", width = 10, font="Arial 10 bold")
result.grid(row=3,column=2, sticky = E)
#Displaying Result
Display1=Label(root, height = 1, width = 20, bg = "yellow", font = "Arial 10 bold")
Display1.grid(row = 3, column=3)

#BMI Status Label
result = Label(root, text = "BMI Status: ", width = 10, font="Arial 10 bold")
result.grid(row=4,column=2, sticky = E)
#Displaying BMI Status
Display2=Label(root, height = 1, width = 20, bg = "yellow", font = "Arial 10 bold")
Display2.grid(row = 4, column=3)

#BMI Calculation
def bmi():
    try:
        w = float(weightfield.get())
        h = float(heightfield.get())
        bmi = w/(h*h)
        Display1.configure(text=bmi)
#BMI Classification
        if (bmi<18.5):
            Display2.configure(text="Under Weight" )
        elif(bmi>=18.5 and bmi<=24.9):
            Display2.configure(text="Normal Weight" )
        elif(bmi>=25.0 and bmi<=29.9):
            Display2.configure(text="Over Weight")
        elif(bmi>=30.0 and bmi<=34.9):
            Display2.configure(text="Class I Obesity")
        elif(bmi>=35.0 and bmi<=39.9):
            Display2.configure(text="Class II Obesity")
        elif(bmi>=40.0):
            Display2.configure(text="Class III Obesity")
        
    except:
#When the user not input integers
        tkinter.messagebox.showinfo("Input Invalid", "You must input integers") 
    
#Clearing Data
def reset():
    weightfield.delete(0, 'end')
    heightfield.delete(0, 'end')

#Button Reset
btnreset = Button(root, text ="Reset", height = 1, width = 10, command = reset)
btnreset.grid(row = 4, column = 1)

#Button Result
btnresult = Button(root, text ="BMI", height = 4, width = 10, command = bmi)
btnresult.grid(row = 3, column = 1)

#Button Exit
btnexit = Button(root, text ="Exit", height = 1, width = 7, command = root.destroy)
btnexit.grid(row = 5, column = 0)

root.mainloop()      #make window constantly open
#end of the code