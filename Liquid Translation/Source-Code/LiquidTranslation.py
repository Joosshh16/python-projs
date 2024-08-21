#start of the code
from tkinter import *           #import tkinter libraries       
import tkinter.messagebox       #import tkinter messagebox

root = Tk()                     #open window
root.title("Liquid Translation")               #window title
root.resizable (width=False, height = False)    #fixed size of the window

#Window Size
root.geometry("700x355")

#Window Title
title = Label(root, text = "Liquid Translation", font="Arial 20 bold")
title.grid(row = 0, column = 3)
instruct= Label(root, text = "Choose and input you wanted to convert.", font="Arial 10 bold")
instruct.grid(row =  1, column = 3)

#For Column and Row Spacing
col= Label(root, text = "", width = 5, font="Arial 10 bold")
col.grid(row =  0, column = 0 )
row= Label(root, text = "", width = 5, font="Arial 10 bold")
row.grid(row =  2, column = 0 )
row2= Label(root, text = "", width = 5, font="Arial 10 bold")
row2.grid(row =  4, column = 0 )

#Field Input Entry
inputfield = Entry(root, width = 20)

#Displaying Field Input Entry
inputfield.grid(row = 5 , column = 2)

#Output Label
Display1=Label(root, height = 1, width = 20, bg = "sky blue", font = "Arial 10 bold")
Display1.grid(row = 5, column = 4)

#Translating Water Unit
def translate():
    try:
        option1 = selectUnit1.get()
        option2 = selectUnit2.get()
        data = float(inputfield.get())

#Water Unit Calculation
        if (option1 == Unit1[0] and option2 == Unit2[0]):
            tkinter.messagebox.showinfo("Select Error", "You must select different unit you wanted to convert")
        elif (option1 == Unit1[1] and option2 == Unit2[1]):
            tkinter.messagebox.showinfo("Select Unit2", "You must select different unit you wanted to convert")
        elif (option1 == Unit1[2] and option2 == Liters2[2]):
            tkinter.messagebox.showinfo("Select Error", "You must select different unit you wanted to convert")
        elif (option1 == Unit1[3] and option2 == Unit2[3]):
            tkinter.messagebox.showinfo("Select Error", "You must select different unit you wanted to convert")
        elif (option1 == Unit1[4] and option2 == Unit2[4]):
            tkinter.messagebox.showinfo("Select Error", "You must select different unit you wanted to convert")
        elif (option1 == Unit1[5] and option2 == Unit2[5]):
            tkinter.messagebox.showinfo("Select Error", "You must select different unit you wanted to convert")
        elif (option1 == Unit1[6] and option2 == Unit2[6]):
            tkinter.messagebox.showinfo("Select Error", "You must select different unit you wanted to convert")
        elif (option1 == Unit1[7] and option2 == Unit2[7]):
            tkinter.messagebox.showinfo("Select Error", "You must select different unit you wanted to convert")
        elif (option1 == Unit1[8] and option2 == Unit2[8]):
            tkinter.messagebox.showinfo("Select Error", "You must select different unit you wanted to convert")
#Litre Translation
        elif (option1 == Unit1[0] and option2 == Unit2[1]):
            output = data / 100
            Display1.configure(text = output)
        elif (option1 == Unit1[0] and option2 == Unit2[2]):
            output = data * 100
            Display1.configure(text = output)
        elif (option1 == Unit1[0] and option2 == Unit2[3]):
            output = data / 1000
            Display1.configure(text = output)
        elif (option1 == Unit1[0] and option2 == Unit2[4]):
            output = data * 10
            Display1.configure(text = output)
        elif (option1 == Unit1[0] and option2 == Unit2[5]):
            output = data * 1000
            Display1.configure(text = output)
        elif (option1 == Unit1[0] and option2 == Unit2[6]):
            output = data * 61.024
            Display1.configure(text = output)
        elif (option1 == Unit1[0] and option2 == Unit2[7]):
            output = data / 28.317
            Display1.configure(text = output)
        elif (option1 == Unit1[0] and option2 == Unit2[8]):
            output = data / 4.546
            Display1.configure(text = output)
#Hectolitre Translation
        elif (option1 == Unit1[1] and option2 == Unit2[0]):
            output = data * 100
            Display1.configure(text = output)
        elif (option1 == Unit1[1] and option2 == Unit2[2]):
            output = data * 10000
            Display1.configure(text = output)
        elif (option1 == Unit1[1] and option2 == Unit2[3]):
            output = data / 10
            Display1.configure(text = output)
        elif (option1 == Unit1[1] and option2 == Unit2[4]):
            output = data * 1000
            Display1.configure(text = output)
        elif (option1 == Unit1[1] and option2 == Unit2[5]):
            output = data * 100000
            Display1.configure(text = output)
        elif (option1 == Unit1[1] and option2 == Unit2[6]):
            output = data * 6102
            Display1.configure(text = output)
        elif (option1 == Unit1[1] and option2 == Unit2[7]):
            output = data * 3.531
            Display1.configure(text = output)
        elif (option1 == Unit1[1] and option2 == Unit2[8]):
            output = data * 21.997
            Display1.configure(text = output)
#Centilitre Translation
        elif (option1 == Unit1[2] and option2 == Unit2[0]):
            output = data / 100
            Display1.configure(text = output)
        elif (option1 == Unit1[2] and option2 == Unit2[1]):
            output = data / 10000
            Display1.configure(text = output)
        elif (option1 == Unit1[2] and option2 == Unit2[3]):
            output = data / 100000
            Display1.configure(text = output)
        elif (option1 == Unit1[2] and option2 == Unit2[4]):
            output = data / 10
            Display1.configure(text = output)
        elif (option1 == Unit1[2] and option2 == Unit2[5]):
            output = data * 10
            Display1.configure(text = output)
        elif (option1 == Unit1[2] and option2 == Unit2[6]):
            output = data / 1.639
            Display1.configure(text = output)
        elif (option1 == Unit1[2] and option2 == Unit2[7]):
            output = data / 2832
            Display1.configure(text = output)
        elif (option1 == Unit1[2] and option2 == Unit2[8]):
            output = data / 455
            Display1.configure(text = output)
#Kilolitre Translation            
        elif (option1 == Unit1[3] and option2 == Unit2[0]):
            output = data * 1000
            Display1.configure(text = output)
        elif (option1 == Unit1[3] and option2 == Unit2[1]):
            output = data * 10
            Display1.configure(text = output)
        elif (option1 == Unit1[3] and option2 == Unit2[2]):
            output = data * 100000
            Display1.configure(text = output)
        elif (option1 == Unit1[3] and option2 == Unit2[4]):
            output = data * 100
            Display1.configure(text = output)
        elif (option1 == Unit1[3] and option2 == Unit2[5]):
            output = data * 1000000
            Display1.configure(text = output)
        elif (option1 == Unit1[3] and option2 == Unit2[6]):
            output = data * 61024
            Display1.configure(text = output)
        elif (option1 == Unit1[3] and option2 == Unit2[7]):
            output = data * 35.315
            Display1.configure(text = output)
        elif (option1 == Unit1[3] and option2 == Unit2[8]):
            output = data * 220
            Display1.configure(text = output)
#Decilitre Translation  
        elif (option1 == Unit1[4] and option2 == Unit2[0]):
            output = data / 10
            Display1.configure(text = output)
        elif (option1 == Unit1[4] and option2 == Unit2[1]): 
            output = data / 1000
            Display1.configure(text = output)
        elif (option1 == Unit1[4] and option2 == Unit2[2]): 
            output = data * 10
            Display1.configure(text = output)
        elif (option1 == Unit1[4] and option2 == Unit2[3]): 
            output = data / 10000
            Display1.configure(text = output)
        elif (option1 == Unit1[4] and option2 == Unit2[5]): 
            output = data * 100
            Display1.configure(text = output)
        elif (option1 == Unit1[4] and option2 == Unit2[6]): 
            output = data * 6.102
            Display1.configure(text = output)
        elif (option1 == Unit1[4] and option2 == Unit2[7]): 
            output = data / 283
            Display1.configure(text = output)
        elif (option1 == Unit1[4] and option2 == Unit2[8]): 
            output = data / 45.461
            Display1.configure(text = output)
#Millilitre Translation  
        elif (option1 == Unit1[5] and option2 == Unit2[0]):
            output = data / 1000
            Display1.configure(text = output)
        elif (option1 == Unit1[5] and option2 == Unit2[1]):
            output = data / 100000
            Display1.configure(text = output)
        elif (option1 == Unit1[5] and option2 == Unit2[2]):
            output = data / 10
            Display1.configure(text = output)
        elif (option1 == Unit1[5] and option2 == Unit2[3]):
            output = data * 0.000001
            Display1.configure(text = output)
        elif (option1 == Unit1[5] and option2 == Unit2[4]):
            output = data / 100
            Display1.configure(text = output)
        elif (option1 == Unit1[5] and option2 == Unit2[6]):
            output = data / 16.387
            Display1.configure(text = output)
        elif (option1 == Unit1[5] and option2 == Unit2[7]):
            output = data / 28317
            Display1.configure(text = output)
        elif (option1 == Unit1[5] and option2 == Unit2[8]):
            output = data / 4546
            Display1.configure(text = output)
#Cubic Inch Translation             
        elif (option1 == Unit1[6] and option2 == Unit2[0]):
            output = data / 61.024
            Display1.configure(text = output)
        elif (option1 == Unit1[6] and option2 == Unit2[1]):
            output = data / 6102
            Display1.configure(text = output)
        elif (option1 == Unit1[6] and option2 == Unit2[2]):
            output = data * 1.639
            Display1.configure(text = output)
        elif (option1 == Unit1[6] and option2 == Unit2[3]):
            output = data / 61024
            Display1.configure(text = output)
        elif (option1 == Unit1[6] and option2 == Unit2[4]):
            output = data / 6.102
            Display1.configure(text = output)
        elif (option1 == Unit1[6] and option2 == Unit2[5]):
            output = data * 16.387
            Display1.configure(text = output)
        elif (option1 == Unit1[6] and option2 == Unit2[7]):
            output = data / 1728
            Display1.configure(text = output)
        elif (option1 == Unit1[6] and option2 == Unit2[8]):
            output = data / 277
            Display1.configure(text = output)
#Cubic Foot Translation
        elif (option1 == Unit1[7] and option2 == Unit2[0]):
            output = data * 28.317
            Display1.configure(text = output)
        elif (option1 == Unit1[7] and option2 == Unit2[1]):
            output = data / 3.531
            Display1.configure(text = output)
        elif (option1 == Unit1[7] and option2 == Unit2[2]):
            output = data * 2832
            Display1.configure(text = output)
        elif (option1 == Unit1[7] and option2 == Unit2[3]):
            output = data / 35.315
            Display1.configure(text = output)
        elif (option1 == Unit1[7] and option2 == Unit2[4]):
            output = data * 283
            Display1.configure(text = output)
        elif (option1 == Unit1[7] and option2 == Unit2[5]):
            output = data * 28317
            Display1.configure(text = output)
        elif (option1 == Unit1[7] and option2 == Unit2[6]):
            output = data * 1728
            Display1.configure(text = output)
        elif (option1 == Unit1[7] and option2 == Unit2[8]):
            output = data * 6.229
            Display1.configure(text = output)
#Gallon Translation
        elif (option1 == Unit1[8] and option2 == Unit2[0]):
            output = data * 4.546
            Display1.configure(text = output)
        elif (option1 == Unit1[8] and option2 == Unit2[1]):
            output = data / 21.997
            Display1.configure(text = output)
        elif (option1 == Unit1[8] and option2 == Unit2[2]):
            output = data * 455
            Display1.configure(text = output)
        elif (option1 == Unit1[8] and option2 == Unit2[3]):
            output = data / 220
            Display1.configure(text = output)
        elif (option1 == Unit1[8] and option2 == Unit2[4]):
            output = data * 45.461
            Display1.configure(text = output)
        elif (option1 == Unit1[8] and option2 == Unit2[5]):
            output = data * 4546
            Display1.configure(text = output)
        elif (option1 == Unit1[8] and option2 == Unit2[6]):
            output = data * 277
            Display1.configure(text = output)
        elif (option1 == Unit1[8] and option2 == Unit2[7]):
            output = data / 6.229
            Display1.configure(text = output)
    except:
#When the user not input integers
        tkinter.messagebox.showinfo("Input Invalid", "You must input correct value")
        
#Dropdown 1 for Liquid Unit
Unit1 = [
    "Litre",    
    "Hectolitre", 
    "Centilitre", 
    "Kilolitre", 
    "Decilitre", 
    "Millilitre", 
    "Cubic Inch",   
    "Cubic Foot", 
    "Gallon" 
]

selectUnit1 = StringVar()
selectUnit1.set(Unit1[0])

drop = OptionMenu(root, selectUnit1, *Unit1)
drop.grid(row = 3, column = 2 )

#Dropdown 2 for Liquid Unit
Unit2 = [
    "Litre",
    "Hectolitre",
    "Centilitre",
    "Kilolitre",
    "Decilitre",
    "Millilitre",
    "Cubic Inch",
    "Cubic Foot",
    "Gallon"
]

selectUnit2 = StringVar()
selectUnit2.set(Unit2[0])

drop = OptionMenu(root, selectUnit2, *Unit2)
drop.grid(row = 3, column = 4 )

#Clearing Data
def reset():
    inputfield.delete(0, 'end')   

#Button Convert
buttonconvert = Button(root, text = "Translate",height = 4, width = 10, command = translate)
buttonconvert.grid(row = 6, column = 3)

#Button Reset
btnreset = Button(root, text ="Reset", height = 2, width = 10, command = reset)
btnreset.grid(row = 7, column = 3)

#Button Exit
btnexit = Button(root, text ="Exit", height = 2, width = 7, command = root.destroy)
btnexit.grid(row = 8, column = 1)

#Bottom Text
line = Label(root, text = "-------------------------------------", width = 30)
line.grid(row =  9, column = 3)
info = Label(root, text = "Liquid Translation 2020", width = 20, font = "Calibre 8")
info.grid(row =  10, column = 3)


root.mainloop()      #make window constantly open
#end of the code