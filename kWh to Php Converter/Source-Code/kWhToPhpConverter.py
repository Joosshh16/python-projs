#start of the code
from tkinter import *           #import tkinter libraries
import tkinter.messagebox       #import tkinter messagebox

root = Tk()                     #open window
root.title("KP Converter")      #window title
root.resizable (width=False, height = False)    #fixed size of the window

#Window Size
widthwindow = 740
heightwindow = 350

screenwidth =root.winfo_screenwidth()
screenheight =root.winfo_screenheight()

xcoordinate = (screenwidth/2)-(widthwindow/2)
ycoordinate = (screenheight/2)-(heightwindow/2)

root.geometry("%dx%d+%d+%d" % (widthwindow, heightwindow, xcoordinate, ycoordinate))

#Window Title
title = Label(root, text = "KP Electric Company", font="Arial 20 bold")
title.grid(row=  0, column = 2)
title2 = Label(root, text = "kWh to Php Converter", font="Arial 18 bold")
title2.grid(row = 1, column = 2)

#Text Label
justdisplayrow = Label(root, text = "", width = 10)
info1 = Label(root, text ="Please enter your data and kWh you wanted to convert:", width = 45, font="Arial 9")
name = Label(root, text ="Name:", width = 7)
kwh = Label(root, text ="kWh:", width = 5)
contactnumber = Label(root, text ="Contact#:", width = 7)
address = Label(root, text ="Address:", width = 6)
info2 = Label(root, text ="Welcome this is", width = 35, font="Arial 10 bold")
info3 = Label(root, text ="Kilowatt-hour to Philippine Peso Converter", width = 35, font="Arial 10 bold")

#Displaying Text
justdisplayrow.grid(row = 2, column = 0 , sticky = W)
info1.grid(row = 3, column = 2)
name.grid(row = 4, column = 0, stick = E)
kwh.grid(row = 4, column = 3, stick = E)
contactnumber.grid(row = 5, column = 0, stick = E)
address.grid(row = 5, column = 3, stick = E)
info2.grid(row = 6, column = 2)
info3.grid(row = 7, column = 2)

#Field Entry
namefield = Entry(root)
kwhfield = Entry(root)
contactnumberfield = Entry(root)
addressfield = Entry(root)

#Displaying Field Entry
namefield.grid(row = 4, column = 1)
kwhfield.grid(row = 4, column = 4)
contactnumberfield.grid(row = 5, column = 1)
addressfield.grid(row = 5, column = 4)

#Convert Window, Second Window
def convert():
    try:
        #Calculation from kWh to Php
        k = float(kwhfield.get())
        result = k * 0.00480819
    
        root = Tk()                        #second window open
        root.title("KP Converter")         #second window title
        root.resizable (width=False, height = False)    #fixed size of the window
        
#Second Window Size  
        widthwindow = 480
        heightwindow = 450

        screenwidth =root.winfo_screenwidth()
        screenheight =root.winfo_screenheight()

        xcoordinate = (screenwidth/2)-(widthwindow/2)
        ycoordinate = (screenheight/2)-(heightwindow/2)

        root.geometry("%dx%d+%d+%d" % (widthwindow, heightwindow, xcoordinate, ycoordinate))
        
#Second Window Title   
        title = Label(root, text = "KP Electric Company", font="Arial 20 bold")
        title.grid(row = 0, column = 1)
    
        title2 = Label(root, text = "Your kWh to Php Converter", font="Arial 18 bold")
        title2.grid(row = 1, column = 1)
        
#Displaying for Column Spacing      
        justdisplaycolumn = Label(root, text = "", width = 10)
        justdisplaycolumn.grid(row = 0,column = 0, sticky = W)
        
#Displaying for Row Spacing       
        justdisplayrow = Label(root, text = "", width = 10)
        justdisplayrow.grid(row = 2, column = 0, sticky = W)
        
#Description Text      
        info = Label(root, text ="Your electrical bill data is provided by KP Electric Company.", width = 45, font="Arial 9")
        info.grid(row = 3, column = 1)
    
#Name Text
        namedisplay = Label(root, text = "Your Name: ", width = 10, font="Arial 10 bold", height = 2)
        namedisplay.grid(row = 4, column = 1, sticky = W)
    
#Displaying Name Result
        nameresult=Label(root, height = 1, width = 20, bg = "sky blue", font = "Arial 10 bold", text = namefield.get())
        nameresult.grid(row = 5, column = 1)
    
#kWh Text
        namedisplay = Label(root, text = "Your kWh: ", width = 10, font="Arial 10 bold")
        namedisplay.grid(row = 6,column = 1, sticky = W)
    
#Displaying kWh Result
        nameresult=Label(root, height = 1, width = 20, bg = "sky blue", font = "Arial 10 bold", text = k)
        nameresult.grid(row = 7, column = 1)
    
#Bill Result Text
        namedisplay = Label(root, text = "Your Electric Bill Php: ", width = 20, font="Arial 10 bold")
        namedisplay.grid(row = 8 ,column = 1, sticky = W)
    
#Displaying Bill Result
        nameresult=Label(root, height = 1, width = 20, bg = "sky blue", font = "Arial 10 bold", text = result)
        nameresult.grid(row = 9, column = 1)
                
#Displaying for Row Spacing    
        justdisplayrow2 = Label(root, text = "", width = 10)
        justdisplayrow2.grid(row = 10, column = 0, sticky = W)

#Button Thank you Text
        thankyou = Label(root, text = "Thank you for using KP Converter", width = 45, font="Arial 10 bold")
        thankyou.grid(row = 11 ,column = 1, sticky = W)
        
#Displaying for Row Spacing           
        justdisplayrow3 = Label(root, text = "", width = 10)
        justdisplayrow3.grid(row = 12,column = 0, sticky = W)
    
#Button Convert Again
        btnexit = Button(root, text ="Convert Again", height = 2, width = 10, command = root.destroy)
        btnexit.grid(row = 13, column = 1)
              
#Displaying for Row Spacing           
        justdisplayrow4 = Label(root, text = "", width = 10)
        justdisplayrow4.grid(row = 14, column = 0, sticky = W)
        
#Bottom Text        
        line = Label(root, text = "-------------------------------------------------", width = 40)
        line.grid(row = 15, column = 1,)        
        info = Label(root, text ="KP Electric Company since 2000", width = 30, font="Calibri 8")
        info.grid(row = 16, column = 1,)        
        info2 = Label(root, text ="Created by: ACE 2020", width = 30, font="Calibri 8")
        info2.grid(row = 17, column = 1,)
        
    except:
#When the user not input integers into kWh field
        tkinter.messagebox.showinfo("Input Invalid", "Please enter your correct kWh value")
        
#Clearing Data
def reset():
    namefield.delete(0, 'end')
    kwhfield.delete(0, 'end')
    addressfield.delete(0, 'end')
    contactnumberfield.delete(0, 'end')
    
#Displaying for Row Spacing  
justdisplayrow2 = Label(root, text = "", width = 10, font="Arial 10 bold")
justdisplayrow2.grid(row = 8, column = 0, sticky = W)

#Button Submit
btnconvert = Button(root, text ="Convert", height = 2, width = 10, command = convert)
btnconvert.grid(row = 9, column = 2)

#Button Reset
btnreset = Button(root, text ="Reset", height = 2, width = 10, command = reset)
btnreset.grid(row = 9, column = 4)

#Button Exit
btnexit = Button(root, text ="Exit", height = 2, width = 10, command = root.destroy)
btnexit.grid(row = 9, column = 1)

#Displaying for Row Spacing 
justdisplayrow3 = Label(root, text = "", width = 10)
justdisplayrow3.grid(row = 10, column = 0, sticky = W)

#Bottom Text  
line = Label(root, text = "-------------------------------------------------", width = 40)
line.grid(row = 11, column = 2)
info4 = Label(root, text ="KP Electric Company since 2000", width = 30, font="Calibri 8")
info4.grid(row = 12, column = 2)
info5 = Label(root, text ="Created by: ACE 2020", width = 30, font="Calibri 8")
info5.grid(row = 13, column = 2)

root.mainloop()      #make window constantly open
#end of the code