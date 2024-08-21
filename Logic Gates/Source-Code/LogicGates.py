#start of the code
from tkinter import *           #import tkinter libraries       
import tkinter.messagebox       #import tkinter messagebox

window1 = Tk()                     #open window
window1.title("Logic Gates")               #window title
window1.resizable (width=False, height = False)    #fixed size of the window

#Window Size
window1.geometry("680x500")

#Window Title
title = Label(window1, text = "Logic Gates", width = 15, font="Arial 30 bold")
title.grid(row = 0, column = 3)

instruct= Label(window1, text = "Choose Logic Gates you wanted to simulate.", font="Arial 10 bold")
instruct.grid(row =  1, column = 3)

#Row and Column Spacing For Window1
column = Label(window1, width = 5)
column.grid(row = 0, column = 0)
row = Label(window1, width = 5)
row.grid(row = 2, column = 2)
row2 = Label(window1, width = 5)
row2.grid(row = 11, column = 2)

#Logic Gates List      
Gate1 = [
    "NOT",    
    "AND", 
    "OR", 
    "NAND", 
    "NOR", 
    "EXOR", 
    "EXNOR" 
]
    
selectUnit1 = StringVar()
selectUnit1.set(Gate1[0])

#Image Path
notimage = PhotoImage(file = "NOTGate.png")
andimage = PhotoImage(file = "ANDGate.png")
orimage = PhotoImage(file = "ORGate.png")
nandimage = PhotoImage(file = "NANDGate.png")
norimage = PhotoImage(file = "NORGate.png")
exorimage = PhotoImage(file = "EXORGate.png")
exnorimage = PhotoImage(file = "EXNORGate.png")

#Selection of Image
def logicgates(event):
    option1 = selectUnit1.get()
    if (option1 == Gate1[0]):
        labelimagegate = Label(window1, image = notimage)
        labelimagegate.grid (row = 7 , column = 3)
    elif (option1 == Gate1[1]):
        labelimagegate = Label(window1, image = andimage)
        labelimagegate.grid (row = 7 , column = 3)
    elif (option1 == Gate1[2]):
        labelimagegate = Label(window1, image = orimage)
        labelimagegate.grid (row = 7 , column = 3)
    elif (option1 == Gate1[3]):
        labelimagegate = Label(window1, image = nandimage)
        labelimagegate.grid (row = 7 , column = 3)
    elif (option1 == Gate1[4]):
        labelimagegate = Label(window1, image = norimage)
        labelimagegate.grid (row = 7 , column = 3)
    elif (option1 == Gate1[5]):
        labelimagegate = Label(window1, image = exorimage)
        labelimagegate.grid (row = 7 , column = 3)
    elif (option1 == Gate1[6]):
        labelimagegate = Label(window1, image = exnorimage)
        labelimagegate.grid (row = 7 , column = 3)

#Dropdown for Logic Gates List
dropgate = OptionMenu(window1, selectUnit1, *Gate1, command = logicgates)
dropgate.grid(row = 3, column = 1 )

#Variables for Radio Button (Input A and Input B)
inpa = IntVar()
inpb = IntVar()

#Input A
inp1= Label(window1, text = "Input A", font="Arial 15 bold")
inp1.grid(row =  4, column = 1)

oneA = Radiobutton(window1, text = "OFF / 0", variable = inpa, value = 0)
oneA.grid(row = 5, column = 1)
twoA = Radiobutton(window1, text = "ON / 1", variable = inpa, value = 1)
twoA.grid(row = 6, column = 1)

#Input B
inp2= Label(window1, text = "Input B", font="Arial 15 bold")
inp2.grid(row =  8, column = 1)

oneB = Radiobutton(window1, text = "OFF / 0", variable = inpb, value = 0)
oneB.grid(row = 9, column = 1)
twoB = Radiobutton(window1, text = "ON / 1", variable = inpb, value = 1)
twoB.grid(row = 10, column = 1)

#Answer Output for Inputs in Logic Gates
def output():
    option1 = selectUnit1.get()
    inA = inpa.get()
    inB = inpb.get()
    if (option1 == Gate1[0]):
        if (inA == 0):
            outputanswer.configure(text = "ON / 1")
        elif (inA == 1):
            outputanswer.configure(text = "OFF / 0")
    elif (option1 == Gate1[1]):
        if (inA == 0 and inB == 0):
            outputanswer.configure(text = "OFF / 0")
        elif (inA == 0 and inB == 1):
            outputanswer.configure(text = "OFF / 0")
        elif (inA == 1 and inB == 0):
            outputanswer.configure(text = "OFF / 0")
        elif (inA == 1 and inB == 1):
            outputanswer.configure(text = "ON / 1")
    elif (option1 == Gate1[2]):
        if (inA == 0 and inB == 0):
            outputanswer.configure(text = "OFF / 0")
        elif (inA == 0 and inB == 1):
            outputanswer.configure(text = "ON / 1")
        elif (inA == 1 and inB == 0):
            outputanswer.configure(text = "ON / 1")
        elif (inA == 1 and inB == 1):
            outputanswer.configure(text = "ON / 1")
    elif (option1 == Gate1[3]):
        if (inA == 0 and inB == 0):
            outputanswer.configure(text = "ON / 1")
        elif (inA == 0 and inB == 1):
            outputanswer.configure(text = "ON / 1")
        elif (inA == 1 and inB == 0):
            outputanswer.configure(text = "ON / 1")
        elif (inA == 1 and inB == 1):
            outputanswer.configure(text = "OFF / 0")
    elif (option1 == Gate1[4]):
        if (inA == 0 and inB == 0):
            outputanswer.configure(text = "ON / 1")
        elif (inA == 0 and inB == 1):
            outputanswer.configure(text = "OFF / 0")
        elif (inA == 1 and inB == 0):
            outputanswer.configure(text = "OFF / 0")
        elif (inA == 1 and inB == 1):
            outputanswer.configure(text = "OFF / 0")
    elif (option1 == Gate1[5]):
        if (inA == 0 and inB == 0):
            outputanswer.configure(text = "OFF / 0")
        elif (inA == 0 and inB == 1):
            outputanswer.configure(text = "ON / 1")
        elif (inA == 1 and inB == 0):
            outputanswer.configure(text = "ON / 1")
        elif (inA == 1 and inB == 1):
            outputanswer.configure(text = "OFF / 0")
    elif (option1 == Gate1[6]):
        if (inA == 0 and inB == 0):
            outputanswer.configure(text = "ON / 1")
        elif (inA == 0 and inB == 1):
            outputanswer.configure(text = "OFF / 0")
        elif (inA == 1 and inB == 0):
            outputanswer.configure(text = "OFF / 0")
        elif (inA == 1 and inB == 1):
            outputanswer.configure(text = "ON / 1")
        
#Text Output and Output
textoutput= Label(window1, text = "Output A/B", bg = "skyblue", font= "Arial 15 bold")
textoutput.grid(row =  3, column = 4)

outputanswer= Label(window1, font="Arial 15 bold", bg = "skyblue", width = 7, height = 3)
outputanswer.grid(row =  7, column = 4)

#Button Convert
buttongate = Button(window1, text = "Logic Gates \nOutput",height = 3, width = 10, font= "Arial 12 bold", command = output)
buttongate.grid(row = 3, column = 3)

#Button Exit
buttonexit = Button(window1, text = "Exit",height = 2, width = 10, font= "Arial 12", command = window1.destroy)
buttonexit.grid(row = 12, column = 3)

window1.mainloop()  
#end of the code