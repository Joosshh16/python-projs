#start of the code
from tkinter import *           #import tkinter libraries
import tkinter.messagebox       #import tkinter messagebox

root = Tk()                     #open window
root.title("Distance")      #window title

#Window Size
widthwindow = 590
heightwindow = 450

screenwidth =root.winfo_screenwidth()
screenheight =root.winfo_screenheight()

xcoordinate = (screenwidth/2)-(widthwindow/2)
ycoordinate = (screenheight/2)-(heightwindow/2)

root.geometry("%dx%d+%d+%d" % (widthwindow, heightwindow, xcoordinate, ycoordinate))

#Window Title
title = Label(root, text = "Distance Translation", font="Arial 20 bold")
title.grid(row =  0, column = 2)
instruct= Label(root, text = "Choose you wanted to convert.", font="Arial 10 bold")
instruct.grid(row =  1, column = 2)

#Meter Translation
def meterconvert():
    
    root = Tk()                        #second window open
    root.title("Distance Translation")         #second window title
    
#Window Size   
    widthwindow = 420
    heightwindow = 690

    screenwidth =root.winfo_screenwidth()
    screenheight =root.winfo_screenheight()

    xcoordinate = (screenwidth/2)-(widthwindow/2)
    ycoordinate = (screenheight/2)-(heightwindow/2)

    root.geometry("%dx%d+%d+%d" % (widthwindow, heightwindow, xcoordinate, ycoordinate))
    
#Window Title  
    title = Label(root, text = "Distance Translation", font="Arial 20 bold")
    title.grid(row =  0, column = 1)
    
#Displaying for Row Spacing    
    displayrow = Label(root, text = "", width = 10)
    displayrow.grid(row = 1, column = 0)
    displayrow = Label(root, text = "", width = 10)
    displayrow.grid(row = 4, column = 0)  
    displayrow = Label(root, text = "", width = 10)
    displayrow.grid(row = 7, column = 0)
    displayrow = Label(root, text = "", width = 10)
    displayrow.grid(row = 24, column = 0)
    displayrow = Label(root, text = "", width = 10)
    displayrow.grid(row = 26, column = 0)
    
#Meter User Input    
    metertext = Label(root, text ="Meter/m:", width = 20)
    metertext.grid(row = 2, column = 1, stick = W)
    meterfield = Entry(root)
    meterfield.grid(row = 3, column = 1)
    
#Text Translate     
    hectometertext = Label(root, text ="Hectometer/hm:", width = 15, font = "Arial 10 bold")
    hectometertext.grid(row = 8, column = 1, stick = W)
    centimetertext = Label(root, text ="Centimeter/cm:", width = 15, font = "Arial 10 bold")
    centimetertext.grid(row = 10, column = 1, stick = W)
    kilometertext = Label(root, text ="Kilometer/km:", width = 15, font = "Arial 10 bold")
    kilometertext.grid(row = 12, column = 1, stick = W)
    decimetertext = Label(root, text ="Decimeter/dm:", width = 15, font = "Arial 10 bold")
    decimetertext.grid(row = 14, column = 1, stick = W)
    millimetertext = Label(root, text ="Millimeter/mm:", width = 15, font = "Arial 10 bold")
    millimetertext.grid(row = 16, column = 1, stick = W)
    inchestext = Label(root, text ="Inches/in:", width = 15, font = "Arial 10 bold")
    inchestext.grid(row = 18, column = 1, stick = W)
    foottext = Label(root, text ="Foot/ft:", width = 15, font = "Arial 10 bold")
    foottext.grid(row = 20, column = 1, stick = W)
    yardtext = Label(root, text ="Yard/yd:", width = 15, font = "Arial 10 bold")
    yardtext.grid(row = 22, column = 1, stick = W)

#Text Translate Result
    hectometertranslate=Label(root, height = 1, width = 25, bg = "sky blue", font = "Arial 10 bold")
    hectometertranslate.grid(row = 9, column = 1)
    centimetertranslate=Label(root, height = 1, width = 25, bg = "sky blue", font = "Arial 10 bold")
    centimetertranslate.grid(row = 11, column = 1) 
    kilometertranslate=Label(root, height = 1, width = 25, bg = "sky blue", font = "Arial 10 bold")
    kilometertranslate.grid(row = 13, column = 1)
    decimetertranslate=Label(root, height = 1, width = 25, bg = "sky blue", font = "Arial 10 bold")
    decimetertranslate.grid(row = 15, column = 1)
    millimetertranslate=Label(root, height = 1, width = 25, bg = "sky blue", font = "Arial 10 bold")
    millimetertranslate.grid(row = 17, column = 1)
    inchestranslate=Label(root, height = 1, width = 25, bg = "sky blue", font = "Arial 10 bold")
    inchestranslate.grid(row = 19, column = 1)
    foottranslate=Label(root, height = 1, width = 25, bg = "sky blue", font = "Arial 10 bold")
    foottranslate.grid(row = 21, column = 1)
    yardtranslate=Label(root, height = 1, width = 25, bg = "sky blue", font = "Arial 10 bold")
    yardtranslate.grid(row = 23, column = 1)
      
#Button Exit
    btnexit = Button(root, text ="Translate Again", height = 2, width = 15, command = root.destroy, font = "Arial 10 bold")
    btnexit.grid(row = 25, column = 1)
    
#Translate Calculation      
    def metertranslate():
        try:
            meter = float(meterfield.get())
            hectometer = meter * 0.01
            centimeter = meter * 100
            kilometer = meter * 0.001
            decimeter = meter * 10
            millimeter = meter * 1000
            inches = meter * 39.3701
            foot = meter * 3.28084
            yard = meter * 1.09361
 
#Displaying Translate Calculation 
            hectometertranslate.configure(text = hectometer)
            centimetertranslate.configure(text = centimeter)
            kilometertranslate.configure(text = kilometer)
            decimetertranslate.configure(text = decimeter)
            millimetertranslate.configure(text = millimeter)
            inchestranslate.configure(text = inches)
            foottranslate.configure(text = foot)
            yardtranslate.configure(text = yard)
            
#When user not input integers            
        except:
            hectometertranslate.configure(text = "Check your meter value")
            centimetertranslate.configure(text = "Check your meter value")
            kilometertranslate.configure(text = "Check your meter value")
            decimetertranslate.configure(text = "Check your meter value")
            millimetertranslate.configure(text = "Check your meter value")
            inchestranslate.configure(text = "Check your meter value")
            foottranslate.configure(text = "Check your meter value")
            yardtranslate.configure(text = "Check your meter value")
        
#Button Translate        
    btntranslate = Button(root, text ="Translate", height = 3, width = 10, command = metertranslate)
    btntranslate.grid(row = 5, column = 1)
    
#Bottom Text      
    line = Label(root, text = "-------------------------------------", width = 30)
    line.grid(row = 27, column = 1)
    info = Label(root, text = "Distance Translation 2020", width = 20, font = "Calibre 8")
    info.grid(row = 28, column = 1)

#Hectometer Translation
def hectometerconvert():
    
    root = Tk()                        #second window open
    root.title("Distance Translation")         #second window title
    
#Window Size   
    widthwindow = 420
    heightwindow = 690

    screenwidth =root.winfo_screenwidth()
    screenheight =root.winfo_screenheight()

    xcoordinate = (screenwidth/2)-(widthwindow/2)
    ycoordinate = (screenheight/2)-(heightwindow/2)

    root.geometry("%dx%d+%d+%d" % (widthwindow, heightwindow, xcoordinate, ycoordinate))
    
#Window Title  
    title = Label(root, text = "Distance Translation", font="Arial 20 bold")
    title.grid(row =  0, column = 1)
    
#Displaying for Row Spacing    
    displayrow = Label(root, text = "", width = 10)
    displayrow.grid(row = 1, column = 0)
    displayrow = Label(root, text = "", width = 10)
    displayrow.grid(row = 4, column = 0)  
    displayrow = Label(root, text = "", width = 10)
    displayrow.grid(row = 7, column = 0)
    displayrow = Label(root, text = "", width = 10)
    displayrow.grid(row = 24, column = 0)
    displayrow = Label(root, text = "", width = 10)
    displayrow.grid(row = 26, column = 0)
    
#Hectometer User Input    
    hectometertext = Label(root, text ="Hectometer/hm:", width = 20)
    hectometertext.grid(row = 2, column = 1, stick = W)
    hectometerfield = Entry(root)
    hectometerfield.grid(row = 3, column = 1)
    
#Text Translate     
    metertext = Label(root, text ="Meter/m:", width = 15, font = "Arial 10 bold")
    metertext.grid(row = 8, column = 1, stick = W)
    centimetertext = Label(root, text ="Centimeter/cm:", width = 15, font = "Arial 10 bold")
    centimetertext.grid(row = 10, column = 1, stick = W)
    kilometertext = Label(root, text ="Kilometer/km:", width = 15, font = "Arial 10 bold")
    kilometertext.grid(row = 12, column = 1, stick = W)
    decimetertext = Label(root, text ="Decimeter/dm:", width = 15, font = "Arial 10 bold")
    decimetertext.grid(row = 14, column = 1, stick = W)
    millimetertext = Label(root, text ="Millimeter/mm:", width = 15, font = "Arial 10 bold")
    millimetertext.grid(row = 16, column = 1, stick = W)
    inchestext = Label(root, text ="Inches/in:", width = 15, font = "Arial 10 bold")
    inchestext.grid(row = 18, column = 1, stick = W)
    foottext = Label(root, text ="Foot/ft:", width = 15, font = "Arial 10 bold")
    foottext.grid(row = 20, column = 1, stick = W)
    yardtext = Label(root, text ="Yard/yd:", width = 15, font = "Arial 10 bold")
    yardtext.grid(row = 22, column = 1, stick = W)

#Text Translate Result
    metertranslate=Label(root, height = 1, width = 25, bg = "sky blue", font = "Arial 10 bold")
    metertranslate.grid(row = 9, column = 1)
    centimetertranslate=Label(root, height = 1, width = 25, bg = "sky blue", font = "Arial 10 bold")
    centimetertranslate.grid(row = 11, column = 1) 
    kilometertranslate=Label(root, height = 1, width = 25, bg = "sky blue", font = "Arial 10 bold")
    kilometertranslate.grid(row = 13, column = 1)
    decimetertranslate=Label(root, height = 1, width = 25, bg = "sky blue", font = "Arial 10 bold")
    decimetertranslate.grid(row = 15, column = 1)
    millimetertranslate=Label(root, height = 1, width = 25, bg = "sky blue", font = "Arial 10 bold")
    millimetertranslate.grid(row = 17, column = 1)
    inchestranslate=Label(root, height = 1, width = 25, bg = "sky blue", font = "Arial 10 bold")
    inchestranslate.grid(row = 19, column = 1)
    foottranslate=Label(root, height = 1, width = 25, bg = "sky blue", font = "Arial 10 bold")
    foottranslate.grid(row = 21, column = 1)
    yardtranslate=Label(root, height = 1, width = 25, bg = "sky blue", font = "Arial 10 bold")
    yardtranslate.grid(row = 23, column = 1)
      
#Button Exit
    btnexit = Button(root, text ="Translate Again", height = 2, width = 15, command = root.destroy, font = "Arial 10 bold")
    btnexit.grid(row = 25, column = 1)
    
#Translate Calculation      
    def hectometertranslate():
        try:
            hectometer = float(hectometerfield.get())
            meter = hectometer * 100
            centimeter = hectometer * 10000
            kilometer = hectometer * 0.1
            decimeter = hectometer * 1000
            millimeter = hectometer * 100000
            inches = hectometer * 3937.01
            foot = hectometer * 328.084
            yard = hectometer * 109.361
 
#Displaying Translate Calculation 
            metertranslate.configure(text = meter)
            centimetertranslate.configure(text = centimeter)
            kilometertranslate.configure(text = kilometer)
            decimetertranslate.configure(text = decimeter)
            millimetertranslate.configure(text = millimeter)
            inchestranslate.configure(text = inches)
            foottranslate.configure(text = foot)
            yardtranslate.configure(text = yard)
            
#When user not input integers 
        except:
            metertranslate.configure(text = "Check your hectometer value")
            centimetertranslate.configure(text = "Check your hectometer value")
            kilometertranslate.configure(text = "Check your hectometer value")
            decimetertranslate.configure(text = "Check your hectometer value")
            millimetertranslate.configure(text = "Check your hectometer value")
            inchestranslate.configure(text = "Check your hectometer value")
            foottranslate.configure(text = "Check your hectometer value")
            yardtranslate.configure(text = "Check your hectometer value")
            
#Button Translate        
    btntranslate = Button(root, text ="Translate", height = 3, width = 10, command = hectometertranslate)
    btntranslate.grid(row = 5, column = 1)
    
#Bottom Text      
    line = Label(root, text = "-------------------------------------", width = 30)
    line.grid(row = 27, column = 1)
    info = Label(root, text = "Distance Translation 2020", width = 20, font = "Calibre 8")
    info.grid(row = 28, column = 1)
    
#Centimeter Translation
def centimeterconvert():
    
    root = Tk()                        #second window open
    root.title("Distance Translation")         #second window title
    
#Window Size   
    widthwindow = 420
    heightwindow = 690

    screenwidth =root.winfo_screenwidth()
    screenheight =root.winfo_screenheight()

    xcoordinate = (screenwidth/2)-(widthwindow/2)
    ycoordinate = (screenheight/2)-(heightwindow/2)

    root.geometry("%dx%d+%d+%d" % (widthwindow, heightwindow, xcoordinate, ycoordinate))
    
#Window Title  
    title = Label(root, text = "Distance Translation", font="Arial 20 bold")
    title.grid(row =  0, column = 1)
    
#Displaying for Row Spacing    
    displayrow = Label(root, text = "", width = 10)
    displayrow.grid(row = 1, column = 0)
    displayrow = Label(root, text = "", width = 10)
    displayrow.grid(row = 4, column = 0)  
    displayrow = Label(root, text = "", width = 10)
    displayrow.grid(row = 7, column = 0)
    displayrow = Label(root, text = "", width = 10)
    displayrow.grid(row = 24, column = 0)
    displayrow = Label(root, text = "", width = 10)
    displayrow.grid(row = 26, column = 0)
    
#Centimeter User Input    
    centimetertext = Label(root, text ="Centimeter/cm:", width = 20)
    centimetertext.grid(row = 2, column = 1, stick = W)
    centimeterfield = Entry(root)
    centimeterfield.grid(row = 3, column = 1)
    
#Text Translate     
    metertext = Label(root, text ="Meter/m:", width = 15, font = "Arial 10 bold")
    metertext.grid(row = 8, column = 1, stick = W)
    hectometertext = Label(root, text ="Hectometer/hm:", width = 15, font = "Arial 10 bold")
    hectometertext.grid(row = 10, column = 1, stick = W)
    kilometertext = Label(root, text ="Kilometer/km:", width = 15, font = "Arial 10 bold")
    kilometertext.grid(row = 12, column = 1, stick = W)
    decimetertext = Label(root, text ="Decimeter/dm:", width = 15, font = "Arial 10 bold")
    decimetertext.grid(row = 14, column = 1, stick = W)
    millimetertext = Label(root, text ="Millimeter/mm:", width = 15, font = "Arial 10 bold")
    millimetertext.grid(row = 16, column = 1, stick = W)
    inchestext = Label(root, text ="Inches/in:", width = 15, font = "Arial 10 bold")
    inchestext.grid(row = 18, column = 1, stick = W)
    foottext = Label(root, text ="Foot/ft:", width = 15, font = "Arial 10 bold")
    foottext.grid(row = 20, column = 1, stick = W)
    yardtext = Label(root, text ="Yard/yd:", width = 15, font = "Arial 10 bold")
    yardtext.grid(row = 22, column = 1, stick = W)

#Text Translate Result
    metertranslate=Label(root, height = 1, width = 25, bg = "sky blue", font = "Arial 10 bold")
    metertranslate.grid(row = 9, column = 1)
    hectometertranslate=Label(root, height = 1, width = 25, bg = "sky blue", font = "Arial 10 bold")
    hectometertranslate.grid(row = 11, column = 1) 
    kilometertranslate=Label(root, height = 1, width = 25, bg = "sky blue", font = "Arial 10 bold")
    kilometertranslate.grid(row = 13, column = 1)
    decimetertranslate=Label(root, height = 1, width = 25, bg = "sky blue", font = "Arial 10 bold")
    decimetertranslate.grid(row = 15, column = 1)
    millimetertranslate=Label(root, height = 1, width = 25, bg = "sky blue", font = "Arial 10 bold")
    millimetertranslate.grid(row = 17, column = 1)
    inchestranslate=Label(root, height = 1, width = 25, bg = "sky blue", font = "Arial 10 bold")
    inchestranslate.grid(row = 19, column = 1)
    foottranslate=Label(root, height = 1, width = 25, bg = "sky blue", font = "Arial 10 bold")
    foottranslate.grid(row = 21, column = 1)
    yardtranslate=Label(root, height = 1, width = 25, bg = "sky blue", font = "Arial 10 bold")
    yardtranslate.grid(row = 23, column = 1)
      
#Button Exit
    btnexit = Button(root, text ="Translate Again", height = 2, width = 15, command = root.destroy, font = "Arial 10 bold")
    btnexit.grid(row = 25, column = 1)
    
#Translate Calculation      
    def centimetertranslate():
        try:
            centimeter = float(centimeterfield.get())
            meter = centimeter * 0.01
            hectometer = centimeter * 0.0001
            kilometer = centimeter * 0.00001
            decimeter = centimeter * 0.1
            millimeter = centimeter * 10
            inches = centimeter * 0.393701
            foot = centimeter * 0.0328084
            yard = centimeter * 0.0109361
 
#Displaying Translate Calculation 
            metertranslate.configure(text = meter)
            hectometertranslate.configure(text = hectometer)
            kilometertranslate.configure(text = kilometer)
            decimetertranslate.configure(text = decimeter)
            millimetertranslate.configure(text = millimeter)
            inchestranslate.configure(text = inches)
            foottranslate.configure(text = foot)
            yardtranslate.configure(text = yard)
            
#When user not input integers            
        except:
            metertranslate.configure(text = "Check your centimeter value")
            hectometertranslate.configure(text = "Check your centimeter value")
            kilometertranslate.configure(text = "Check your centimeter value")
            decimetertranslate.configure(text = "Check your centimeter value")
            millimetertranslate.configure(text = "Check your centimeter value")
            inchestranslate.configure(text = "Check your centimeter value")
            foottranslate.configure(text = "Check your centimeter value")
            yardtranslate.configure(text = "Check your centimeter value")
        
#Button Translate        
    btntranslate = Button(root, text ="Translate", height = 3, width = 10, command = centimetertranslate)
    btntranslate.grid(row = 5, column = 1)
    
#Bottom Text      
    line = Label(root, text = "-------------------------------------", width = 30)
    line.grid(row = 27, column = 1)
    info = Label(root, text = "Distance Translation 2020", width = 20, font = "Calibre 8")
    info.grid(row = 28, column = 1)
    
#Kilometer Translation
def kilometerconvert():
    
    root = Tk()                        #second window open
    root.title("Distance Translation")         #second window title
    
#Window Size   
    widthwindow = 420
    heightwindow = 690

    screenwidth =root.winfo_screenwidth()
    screenheight =root.winfo_screenheight()

    xcoordinate = (screenwidth/2)-(widthwindow/2)
    ycoordinate = (screenheight/2)-(heightwindow/2)

    root.geometry("%dx%d+%d+%d" % (widthwindow, heightwindow, xcoordinate, ycoordinate))
    
#Window Title  
    title = Label(root, text = "Distance Translation", font="Arial 20 bold")
    title.grid(row =  0, column = 1)
    
#Displaying for Row Spacing    
    displayrow = Label(root, text = "", width = 10)
    displayrow.grid(row = 1, column = 0)
    displayrow = Label(root, text = "", width = 10)
    displayrow.grid(row = 4, column = 0)  
    displayrow = Label(root, text = "", width = 10)
    displayrow.grid(row = 7, column = 0)
    displayrow = Label(root, text = "", width = 10)
    displayrow.grid(row = 24, column = 0)
    displayrow = Label(root, text = "", width = 10)
    displayrow.grid(row = 26, column = 0)
    
#Kilometer User Input    
    kilometertext = Label(root, text ="Kilometer/km:", width = 20)
    kilometertext.grid(row = 2, column = 1, stick = W)
    kilometerfield = Entry(root)
    kilometerfield.grid(row = 3, column = 1)
    
#Text Translate     
    metertext = Label(root, text ="Meter/m:", width = 15, font = "Arial 10 bold")
    metertext.grid(row = 8, column = 1, stick = W)
    hectometertext = Label(root, text ="Hectometer/hm:", width = 15, font = "Arial 10 bold")
    hectometertext.grid(row = 10, column = 1, stick = W)
    centimetertext = Label(root, text ="Centimeter/cm:", width = 15, font = "Arial 10 bold")
    centimetertext.grid(row = 12, column = 1, stick = W)
    decimetertext = Label(root, text ="Decimeter/dm:", width = 15, font = "Arial 10 bold")
    decimetertext.grid(row = 14, column = 1, stick = W)
    millimetertext = Label(root, text ="Millimeter/mm:", width = 15, font = "Arial 10 bold")
    millimetertext.grid(row = 16, column = 1, stick = W)
    inchestext = Label(root, text ="Inches/in:", width = 15, font = "Arial 10 bold")
    inchestext.grid(row = 18, column = 1, stick = W)
    foottext = Label(root, text ="Foot/ft:", width = 15, font = "Arial 10 bold")
    foottext.grid(row = 20, column = 1, stick = W)
    yardtext = Label(root, text ="Yard/yd:", width = 15, font = "Arial 10 bold")
    yardtext.grid(row = 22, column = 1, stick = W)

#Text Translate Result
    metertranslate=Label(root, height = 1, width = 25, bg = "sky blue", font = "Arial 10 bold")
    metertranslate.grid(row = 9, column = 1)
    hectometertranslate=Label(root, height = 1, width = 25, bg = "sky blue", font = "Arial 10 bold")
    hectometertranslate.grid(row = 11, column = 1) 
    centimetertranslate=Label(root, height = 1, width = 25, bg = "sky blue", font = "Arial 10 bold")
    centimetertranslate.grid(row = 13, column = 1)
    decimetertranslate=Label(root, height = 1, width = 25, bg = "sky blue", font = "Arial 10 bold")
    decimetertranslate.grid(row = 15, column = 1)
    millimetertranslate=Label(root, height = 1, width = 25, bg = "sky blue", font = "Arial 10 bold")
    millimetertranslate.grid(row = 17, column = 1)
    inchestranslate=Label(root, height = 1, width = 25, bg = "sky blue", font = "Arial 10 bold")
    inchestranslate.grid(row = 19, column = 1)
    foottranslate=Label(root, height = 1, width = 25, bg = "sky blue", font = "Arial 10 bold")
    foottranslate.grid(row = 21, column = 1)
    yardtranslate=Label(root, height = 1, width = 25, bg = "sky blue", font = "Arial 10 bold")
    yardtranslate.grid(row = 23, column = 1)
      
#Button Exit
    btnexit = Button(root, text ="Translate Again", height = 2, width = 15, command = root.destroy, font = "Arial 10 bold")
    btnexit.grid(row = 25, column = 1)
    
#Translate Calculation      
    def kilometertranslate():
        try:
            kilometer = float(kilometerfield.get())
            meter = kilometer * 1000
            hectometer = kilometer * 10
            centimeter = kilometer * 100000
            decimeter = kilometer * 10000
            millimeter = kilometer * 1000000
            inches = kilometer * 39370.1
            foot = kilometer * 3280.84
            yard = kilometer * 1093.61
 
#Displaying Translate Calculation 
            metertranslate.configure(text = meter)
            hectometertranslate.configure(text = hectometer)
            centimetertranslate.configure(text = centimeter)
            decimetertranslate.configure(text = decimeter)
            millimetertranslate.configure(text = millimeter)
            inchestranslate.configure(text = inches)
            foottranslate.configure(text = foot)
            yardtranslate.configure(text = yard)
            
#When user not input integers            
        except:
            metertranslate.configure(text = "Check your kilometer value")
            hectometertranslate.configure(text = "Check your kilometer value")
            centimetertranslate.configure(text = "Check your kilometer value")
            decimetertranslate.configure(text = "Check your kilometer value")
            millimetertranslate.configure(text = "Check your kilometer value")
            inchestranslate.configure(text = "Check your kilometer value")
            foottranslate.configure(text = "Check your kilometer value")
            yardtranslate.configure(text = "Check your kilometer value")
        
#Button Translate        
    btntranslate = Button(root, text ="Translate", height = 3, width = 10, command = kilometertranslate)
    btntranslate.grid(row = 5, column = 1)
    
#Bottom Text      
    line = Label(root, text = "-------------------------------------", width = 30)
    line.grid(row = 27, column = 1)
    info = Label(root, text = "Distance Translation 2020", width = 20, font = "Calibre 8")
    info.grid(row = 28, column = 1)

#Decimeter Translation
def decimeterconvert():
    
    root = Tk()                        #second window open
    root.title("Distance Translation")         #second window title
    
#Window Size   
    widthwindow = 420
    heightwindow = 690

    screenwidth =root.winfo_screenwidth()
    screenheight =root.winfo_screenheight()

    xcoordinate = (screenwidth/2)-(widthwindow/2)
    ycoordinate = (screenheight/2)-(heightwindow/2)

    root.geometry("%dx%d+%d+%d" % (widthwindow, heightwindow, xcoordinate, ycoordinate))
    
#Window Title  
    title = Label(root, text = "Distance Translation", font="Arial 20 bold")
    title.grid(row =  0, column = 1)
    
#Displaying for Row Spacing    
    displayrow = Label(root, text = "", width = 10)
    displayrow.grid(row = 1, column = 0)
    displayrow = Label(root, text = "", width = 10)
    displayrow.grid(row = 4, column = 0)  
    displayrow = Label(root, text = "", width = 10)
    displayrow.grid(row = 7, column = 0)
    displayrow = Label(root, text = "", width = 10)
    displayrow.grid(row = 24, column = 0)
    displayrow = Label(root, text = "", width = 10)
    displayrow.grid(row = 26, column = 0)
    
#Decimeter User Input    
    decimetertext = Label(root, text ="Decimeter/dm:", width = 20)
    decimetertext.grid(row = 2, column = 1, stick = W)
    decimeterfield = Entry(root)
    decimeterfield.grid(row = 3, column = 1)
    
#Text Translate     
    metertext = Label(root, text ="Meter/m:", width = 15, font = "Arial 10 bold")
    metertext.grid(row = 8, column = 1, stick = W)
    hectometertext = Label(root, text ="Hectometer/hm:", width = 15, font = "Arial 10 bold")
    hectometertext.grid(row = 10, column = 1, stick = W)
    centimetertext = Label(root, text ="Centimeter/cm:", width = 15, font = "Arial 10 bold")
    centimetertext.grid(row = 12, column = 1, stick = W)
    kilometertext = Label(root, text ="Kilometer/km:", width = 15, font = "Arial 10 bold")
    kilometertext.grid(row = 14, column = 1, stick = W)
    millimetertext = Label(root, text ="Millimeter/mm:", width = 15, font = "Arial 10 bold")
    millimetertext.grid(row = 16, column = 1, stick = W)
    inchestext = Label(root, text ="Inches/in:", width = 15, font = "Arial 10 bold")
    inchestext.grid(row = 18, column = 1, stick = W)
    foottext = Label(root, text ="Foot/ft:", width = 15, font = "Arial 10 bold")
    foottext.grid(row = 20, column = 1, stick = W)
    yardtext = Label(root, text ="Yard/yd:", width = 15, font = "Arial 10 bold")
    yardtext.grid(row = 22, column = 1, stick = W)

#Text Translate Result
    metertranslate=Label(root, height = 1, width = 25, bg = "sky blue", font = "Arial 10 bold")
    metertranslate.grid(row = 9, column = 1)
    hectometertranslate=Label(root, height = 1, width = 25, bg = "sky blue", font = "Arial 10 bold")
    hectometertranslate.grid(row = 11, column = 1) 
    centimetertranslate=Label(root, height = 1, width = 25, bg = "sky blue", font = "Arial 10 bold")
    centimetertranslate.grid(row = 13, column = 1)
    kilometertranslate=Label(root, height = 1, width = 25, bg = "sky blue", font = "Arial 10 bold")
    kilometertranslate.grid(row = 15, column = 1)
    millimetertranslate=Label(root, height = 1, width = 25, bg = "sky blue", font = "Arial 10 bold")
    millimetertranslate.grid(row = 17, column = 1)
    inchestranslate=Label(root, height = 1, width = 25, bg = "sky blue", font = "Arial 10 bold")
    inchestranslate.grid(row = 19, column = 1)
    foottranslate=Label(root, height = 1, width = 25, bg = "sky blue", font = "Arial 10 bold")
    foottranslate.grid(row = 21, column = 1)
    yardtranslate=Label(root, height = 1, width = 25, bg = "sky blue", font = "Arial 10 bold")
    yardtranslate.grid(row = 23, column = 1)
      
#Button Exit
    btnexit = Button(root, text ="Translate Again", height = 2, width = 15, command = root.destroy, font = "Arial 10 bold")
    btnexit.grid(row = 25, column = 1)
    
#Translate Calculation      
    def decimetertranslate():
        try:
            decimiter = float(decimeterfield.get())
            meter = decimiter * 0.1
            hectometer = decimiter * 0.001
            centimeter = decimiter * 10
            kilometer = decimiter * 0.0001
            millimeter = decimiter * 100
            inches = decimiter * 3.93701
            foot = decimiter * 0.328084
            yard = decimiter * 0.109361
 
#Displaying Translate Calculation 
            metertranslate.configure(text = meter)
            hectometertranslate.configure(text = hectometer)
            centimetertranslate.configure(text = centimeter)
            kilometertranslate.configure(text = kilometer)
            millimetertranslate.configure(text = millimeter)
            inchestranslate.configure(text = inches)
            foottranslate.configure(text = foot)
            yardtranslate.configure(text = yard)
            
#When user not input integers            
        except:
            metertranslate.configure(text = "Check your decimeter value")
            hectometertranslate.configure(text = "Check your decimeter value")
            centimetertranslate.configure(text = "Check your decimeter value")
            kilometertranslate.configure(text = "Check your decimeter value")
            millimetertranslate.configure(text = "Check your decimeter value")
            inchestranslate.configure(text = "Check your decimeter value")
            foottranslate.configure(text = "Check your decimeter value")
            yardtranslate.configure(text = "Check your decimeter value")
        
#Button Translate        
    btntranslate = Button(root, text ="Translate", height = 3, width = 10, command = decimetertranslate)
    btntranslate.grid(row = 5, column = 1)
    
#Bottom Text      
    line = Label(root, text = "-------------------------------------", width = 30)
    line.grid(row = 27, column = 1)
    info = Label(root, text = "Distance Translation 2020", width = 20, font = "Calibre 8")
    info.grid(row = 28, column = 1)
    
#Millimeter Translation
def millimeterconvert():
    
    root = Tk()                        #second window open
    root.title("Distance Translation")         #second window title
    
#Window Size   
    widthwindow = 420
    heightwindow = 690

    screenwidth =root.winfo_screenwidth()
    screenheight =root.winfo_screenheight()

    xcoordinate = (screenwidth/2)-(widthwindow/2)
    ycoordinate = (screenheight/2)-(heightwindow/2)

    root.geometry("%dx%d+%d+%d" % (widthwindow, heightwindow, xcoordinate, ycoordinate))
    
#Window Title  
    title = Label(root, text = "Distance Translation", font="Arial 20 bold")
    title.grid(row =  0, column = 1)
    
#Displaying for Row Spacing    
    displayrow = Label(root, text = "", width = 10)
    displayrow.grid(row = 1, column = 0)
    displayrow = Label(root, text = "", width = 10)
    displayrow.grid(row = 4, column = 0)  
    displayrow = Label(root, text = "", width = 10)
    displayrow.grid(row = 7, column = 0)
    displayrow = Label(root, text = "", width = 10)
    displayrow.grid(row = 24, column = 0)
    displayrow = Label(root, text = "", width = 10)
    displayrow.grid(row = 26, column = 0)
    
#Millimeter User Input    
    millimetertext = Label(root, text ="Millimeter/mm:", width = 20)
    millimetertext.grid(row = 2, column = 1, stick = W)
    millimeterfield = Entry(root)
    millimeterfield.grid(row = 3, column = 1)
    
#Text Translate     
    metertext = Label(root, text ="Meter/m:", width = 15, font = "Arial 10 bold")
    metertext.grid(row = 8, column = 1, stick = W)
    hectometertext = Label(root, text ="Hectometer/hm:", width = 15, font = "Arial 10 bold")
    hectometertext.grid(row = 10, column = 1, stick = W)
    centimetertext = Label(root, text ="Centimeter/cm:", width = 15, font = "Arial 10 bold")
    centimetertext.grid(row = 12, column = 1, stick = W)
    kilometertext = Label(root, text ="Kilometer/km:", width = 15, font = "Arial 10 bold")
    kilometertext.grid(row = 14, column = 1, stick = W)
    decimetertext = Label(root, text ="Decimeter/mm:", width = 15, font = "Arial 10 bold")
    decimetertext.grid(row = 16, column = 1, stick = W)
    inchestext = Label(root, text ="Inches/in:", width = 15, font = "Arial 10 bold")
    inchestext.grid(row = 18, column = 1, stick = W)
    foottext = Label(root, text ="Foot/ft:", width = 15, font = "Arial 10 bold")
    foottext.grid(row = 20, column = 1, stick = W)
    yardtext = Label(root, text ="Yard/yd:", width = 15, font = "Arial 10 bold")
    yardtext.grid(row = 22, column = 1, stick = W)

#Text Translate Result
    metertranslate=Label(root, height = 1, width = 25, bg = "sky blue", font = "Arial 10 bold")
    metertranslate.grid(row = 9, column = 1)
    hectometertranslate=Label(root, height = 1, width = 25, bg = "sky blue", font = "Arial 10 bold")
    hectometertranslate.grid(row = 11, column = 1) 
    centimetertranslate=Label(root, height = 1, width = 25, bg = "sky blue", font = "Arial 10 bold")
    centimetertranslate.grid(row = 13, column = 1)
    kilometertranslate=Label(root, height = 1, width = 25, bg = "sky blue", font = "Arial 10 bold")
    kilometertranslate.grid(row = 15, column = 1)
    decimetertranslate=Label(root, height = 1, width = 25, bg = "sky blue", font = "Arial 10 bold")
    decimetertranslate.grid(row = 17, column = 1)
    inchestranslate=Label(root, height = 1, width = 25, bg = "sky blue", font = "Arial 10 bold")
    inchestranslate.grid(row = 19, column = 1)
    foottranslate=Label(root, height = 1, width = 25, bg = "sky blue", font = "Arial 10 bold")
    foottranslate.grid(row = 21, column = 1)
    yardtranslate=Label(root, height = 1, width = 25, bg = "sky blue", font = "Arial 10 bold")
    yardtranslate.grid(row = 23, column = 1)
      
#Button Exit
    btnexit = Button(root, text ="Translate Again", height = 2, width = 15, command = root.destroy, font = "Arial 10 bold")
    btnexit.grid(row = 25, column = 1)
    
#Translate Calculation      
    def millimetertranslate():
        try:
            millimeter = float(millimeterfield.get())
            meter = millimeter * 0.001
            hectometer = millimeter * 0.00001
            centimeter = millimeter * 0.1
            kilometer = millimeter * 0.000001
            decimeter = millimeter * 0.01
            inches = millimeter * 0.0393701
            foot = millimeter * 0.00328084
            yard = millimeter * 0.00109361
 
#Displaying Translate Calculation 
            metertranslate.configure(text = meter)
            hectometertranslate.configure(text = hectometer)
            centimetertranslate.configure(text = centimeter)
            kilometertranslate.configure(text = kilometer)
            decimetertranslate.configure(text = decimeter)
            inchestranslate.configure(text = inches)
            foottranslate.configure(text = foot)
            yardtranslate.configure(text = yard)
            
#When user not input integers            
        except:
            metertranslate.configure(text = "Check your millimeter value")
            hectometertranslate.configure(text = "Check your millimeter value")
            centimetertranslate.configure(text = "Check your millimeter value")
            kilometertranslate.configure(text = "Check your millimeter value")
            decimetertranslate.configure(text = "Check your millimeter value")
            inchestranslate.configure(text = "Check your millimeter value")
            foottranslate.configure(text = "Check your millimeter value")
            yardtranslate.configure(text = "Check your millimeter value")
        
#Button Translate        
    btntranslate = Button(root, text ="Translate", height = 3, width = 10, command = millimetertranslate)
    btntranslate.grid(row = 5, column = 1)
    
#Bottom Text      
    line = Label(root, text = "-------------------------------------", width = 30)
    line.grid(row = 27, column = 1)
    info = Label(root, text = "Distance Translation 2020", width = 20, font = "Calibre 8")
    info.grid(row = 28, column = 1)

#Inches Translation
def inchesconvert():
    
    root = Tk()                        #second window open
    root.title("Distance Translation")         #second window title
    
#Window Size   
    widthwindow = 420
    heightwindow = 690

    screenwidth =root.winfo_screenwidth()
    screenheight =root.winfo_screenheight()

    xcoordinate = (screenwidth/2)-(widthwindow/2)
    ycoordinate = (screenheight/2)-(heightwindow/2)

    root.geometry("%dx%d+%d+%d" % (widthwindow, heightwindow, xcoordinate, ycoordinate))
    
#Window Title  
    title = Label(root, text = "Distance Translation", font="Arial 20 bold")
    title.grid(row =  0, column = 1)
    
#Displaying for Row Spacing    
    displayrow = Label(root, text = "", width = 10)
    displayrow.grid(row = 1, column = 0)
    displayrow = Label(root, text = "", width = 10)
    displayrow.grid(row = 4, column = 0)  
    displayrow = Label(root, text = "", width = 10)
    displayrow.grid(row = 7, column = 0)
    displayrow = Label(root, text = "", width = 10)
    displayrow.grid(row = 24, column = 0)
    displayrow = Label(root, text = "", width = 10)
    displayrow.grid(row = 26, column = 0)
    
#Inches User Input    
    inchestext = Label(root, text ="Inches/in:", width = 20)
    inchestext.grid(row = 2, column = 1, stick = W)
    inchesfield = Entry(root)
    inchesfield.grid(row = 3, column = 1)
    
#Text Translate     
    metertext = Label(root, text ="Meter/m:", width = 15, font = "Arial 10 bold")
    metertext.grid(row = 8, column = 1, stick = W)
    hectometertext = Label(root, text ="Hectometer/hm:", width = 15, font = "Arial 10 bold")
    hectometertext.grid(row = 10, column = 1, stick = W)
    centimetertext = Label(root, text ="Centimeter/cm:", width = 15, font = "Arial 10 bold")
    centimetertext.grid(row = 12, column = 1, stick = W)
    kilometertext = Label(root, text ="Kilometer/km:", width = 15, font = "Arial 10 bold")
    kilometertext.grid(row = 14, column = 1, stick = W)
    decimetertext = Label(root, text ="Decimeter/dm:", width = 15, font = "Arial 10 bold")
    decimetertext.grid(row = 16, column = 1, stick = W)
    millimetertext = Label(root, text ="Millimeter/mm:", width = 15, font = "Arial 10 bold")
    millimetertext.grid(row = 18, column = 1, stick = W)
    foottext = Label(root, text ="Foot/ft:", width = 15, font = "Arial 10 bold")
    foottext.grid(row = 20, column = 1, stick = W)
    yardtext = Label(root, text ="Yard/yd:", width = 15, font = "Arial 10 bold")
    yardtext.grid(row = 22, column = 1, stick = W)

#Text Translate Result
    metertranslate=Label(root, height = 1, width = 25, bg = "sky blue", font = "Arial 10 bold")
    metertranslate.grid(row = 9, column = 1)
    hectometertranslate=Label(root, height = 1, width = 25, bg = "sky blue", font = "Arial 10 bold")
    hectometertranslate.grid(row = 11, column = 1) 
    centimetertranslate=Label(root, height = 1, width = 25, bg = "sky blue", font = "Arial 10 bold")
    centimetertranslate.grid(row = 13, column = 1)
    kilometertranslate=Label(root, height = 1, width = 25, bg = "sky blue", font = "Arial 10 bold")
    kilometertranslate.grid(row = 15, column = 1)
    decimetertranslate=Label(root, height = 1, width = 25, bg = "sky blue", font = "Arial 10 bold")
    decimetertranslate.grid(row = 17, column = 1)
    millimetertranslate=Label(root, height = 1, width = 25, bg = "sky blue", font = "Arial 10 bold")
    millimetertranslate.grid(row = 19, column = 1)
    foottranslate=Label(root, height = 1, width = 25, bg = "sky blue", font = "Arial 10 bold")
    foottranslate.grid(row = 21, column = 1)
    yardtranslate=Label(root, height = 1, width = 25, bg = "sky blue", font = "Arial 10 bold")
    yardtranslate.grid(row = 23, column = 1)
      
#Button Exit
    btnexit = Button(root, text ="Translate Again", height = 2, width = 15, command = root.destroy, font = "Arial 10 bold")
    btnexit.grid(row = 25, column = 1)
    
#Translate Calculation      
    def inchestranslate():
        try:
            inches = float(inchesfield.get())
            meter = inches * 0.0254
            hectometer = inches * 0.000254
            centimeter = inches * 2.54
            kilometer = inches * 0.0000254
            decimeter = inches * 0.254
            millimeter = inches * 25.4
            foot = inches * 0.0833333
            yard = inches * 0.0277778
 
#Displaying Translate Calculation 
            metertranslate.configure(text = meter)
            hectometertranslate.configure(text = hectometer)
            centimetertranslate.configure(text = centimeter)
            kilometertranslate.configure(text = kilometer)
            decimetertranslate.configure(text = decimeter)
            millimetertranslate.configure(text = millimeter)
            foottranslate.configure(text = foot)
            yardtranslate.configure(text = yard)
            
#When user not input integers            
        except:
            metertranslate.configure(text = "Check your inches value")
            hectometertranslate.configure(text = "Check your inches value")
            centimetertranslate.configure(text = "Check your inches value")
            kilometertranslate.configure(text = "Check your inches value")
            decimetertranslate.configure(text = "Check your inches value")
            millimetertranslate.configure(text = "Check your inches value")
            foottranslate.configure(text = "Check your inches value")
            yardtranslate.configure(text = "Check your inches value")
        
#Button Translate        
    btntranslate = Button(root, text ="Translate", height = 3, width = 10, command = inchestranslate)
    btntranslate.grid(row = 5, column = 1)
    
#Bottom Text      
    line = Label(root, text = "-------------------------------------", width = 30)
    line.grid(row = 27, column = 1)
    info = Label(root, text = "Distance Translation 2020", width = 20, font = "Calibre 8")
    info.grid(row = 28, column = 1)
    
#Foot Translation
def footconvert():
    
    root = Tk()                        #second window open
    root.title("Distance Translation")         #second window title
    
#Window Size   
    widthwindow = 420
    heightwindow = 690

    screenwidth =root.winfo_screenwidth()
    screenheight =root.winfo_screenheight()

    xcoordinate = (screenwidth/2)-(widthwindow/2)
    ycoordinate = (screenheight/2)-(heightwindow/2)

    root.geometry("%dx%d+%d+%d" % (widthwindow, heightwindow, xcoordinate, ycoordinate))
    
#Window Title  
    title = Label(root, text = "Distance Translation", font="Arial 20 bold")
    title.grid(row =  0, column = 1)
    
#Displaying for Row Spacing    
    displayrow = Label(root, text = "", width = 10)
    displayrow.grid(row = 1, column = 0)
    displayrow = Label(root, text = "", width = 10)
    displayrow.grid(row = 4, column = 0)  
    displayrow = Label(root, text = "", width = 10)
    displayrow.grid(row = 7, column = 0)
    displayrow = Label(root, text = "", width = 10)
    displayrow.grid(row = 24, column = 0)
    displayrow = Label(root, text = "", width = 10)
    displayrow.grid(row = 26, column = 0)
    
#Foot User Input    
    foottext = Label(root, text ="Foot/ft:", width = 20)
    foottext.grid(row = 2, column = 1, stick = W)
    footfield = Entry(root)
    footfield.grid(row = 3, column = 1)
    
#Text Translate     
    metertext = Label(root, text ="Meter/m:", width = 15, font = "Arial 10 bold")
    metertext.grid(row = 8, column = 1, stick = W)
    hectometertext = Label(root, text ="Hectometer/hm:", width = 15, font = "Arial 10 bold")
    hectometertext.grid(row = 10, column = 1, stick = W)
    centimetertext = Label(root, text ="Centimeter/cm:", width = 15, font = "Arial 10 bold")
    centimetertext.grid(row = 12, column = 1, stick = W)
    kilometertext = Label(root, text ="Kilometer/km:", width = 15, font = "Arial 10 bold")
    kilometertext.grid(row = 14, column = 1, stick = W)
    decimetertext = Label(root, text ="Decimeter/dm:", width = 15, font = "Arial 10 bold")
    decimetertext.grid(row = 16, column = 1, stick = W)
    millimetertext = Label(root, text ="Millimeter/mm:", width = 15, font = "Arial 10 bold")
    millimetertext.grid(row = 18, column = 1, stick = W)
    inchestext = Label(root, text ="Inches/in:", width = 15, font = "Arial 10 bold")
    inchestext.grid(row = 20, column = 1, stick = W)
    yardtext = Label(root, text ="Yard/yd:", width = 15, font = "Arial 10 bold")
    yardtext.grid(row = 22, column = 1, stick = W)

#Text Translate Result
    metertranslate=Label(root, height = 1, width = 25, bg = "sky blue", font = "Arial 10 bold")
    metertranslate.grid(row = 9, column = 1)
    hectometertranslate=Label(root, height = 1, width = 25, bg = "sky blue", font = "Arial 10 bold")
    hectometertranslate.grid(row = 11, column = 1) 
    centimetertranslate=Label(root, height = 1, width = 25, bg = "sky blue", font = "Arial 10 bold")
    centimetertranslate.grid(row = 13, column = 1)
    kilometertranslate=Label(root, height = 1, width = 25, bg = "sky blue", font = "Arial 10 bold")
    kilometertranslate.grid(row = 15, column = 1)
    decimetertranslate=Label(root, height = 1, width = 25, bg = "sky blue", font = "Arial 10 bold")
    decimetertranslate.grid(row = 17, column = 1)
    millimetertranslate=Label(root, height = 1, width = 25, bg = "sky blue", font = "Arial 10 bold")
    millimetertranslate.grid(row = 19, column = 1)
    inchestranslate=Label(root, height = 1, width = 25, bg = "sky blue", font = "Arial 10 bold")
    inchestranslate.grid(row = 21, column = 1)
    yardtranslate=Label(root, height = 1, width = 25, bg = "sky blue", font = "Arial 10 bold")
    yardtranslate.grid(row = 23, column = 1)
      
#Button Exit
    btnexit = Button(root, text ="Translate Again", height = 2, width = 15, command = root.destroy, font = "Arial 10 bold")
    btnexit.grid(row = 25, column = 1)
    
#Translate Calculation      
    def foottranslate():
        try:
            foot = float(footfield.get())
            meter = foot * 0.3048
            hectometer = foot * 0.003048
            centimeter = foot * 30.48
            kilometer = foot * 0.0003048
            decimeter = foot * 3.048
            millimeter = foot * 304.8
            inches = foot * 12
            yard = foot * 0.333333
 
#Displaying Translate Calculation 
            metertranslate.configure(text = meter)
            hectometertranslate.configure(text = hectometer)
            centimetertranslate.configure(text = centimeter)
            kilometertranslate.configure(text = kilometer)
            decimetertranslate.configure(text = decimeter)
            millimetertranslate.configure(text = millimeter)
            inchestranslate.configure(text = inches)
            yardtranslate.configure(text = yard)
            
#When user not input integers            
        except:
            metertranslate.configure(text = "Check your foot value")
            hectometertranslate.configure(text = "Check your foot value")
            centimetertranslate.configure(text = "Check your foot value")
            kilometertranslate.configure(text = "Check your foot value")
            decimetertranslate.configure(text = "Check your foot value")
            millimetertranslate.configure(text = "Check your foot value")
            inchestranslate.configure(text = "Check your foot value")
            yardtranslate.configure(text = "Check your foot value")
        
#Button Translate        
    btntranslate = Button(root, text ="Translate", height = 3, width = 10, command = foottranslate)
    btntranslate.grid(row = 5, column = 1)
    
#Bottom Text      
    line = Label(root, text = "-------------------------------------", width = 30)
    line.grid(row = 27, column = 1)
    info = Label(root, text = "Distance Translation 2020", width = 20, font = "Calibre 8")
    info.grid(row = 28, column = 1)

#Yard Translation
def yardconvert():
    
    root = Tk()                        #second window open
    root.title("Distance Translation")         #second window title
    
#Window Size   
    widthwindow = 420
    heightwindow = 690

    screenwidth =root.winfo_screenwidth()
    screenheight =root.winfo_screenheight()

    xcoordinate = (screenwidth/2)-(widthwindow/2)
    ycoordinate = (screenheight/2)-(heightwindow/2)

    root.geometry("%dx%d+%d+%d" % (widthwindow, heightwindow, xcoordinate, ycoordinate))
    
#Window Title  
    title = Label(root, text = "Distance Translation", font="Arial 20 bold")
    title.grid(row =  0, column = 1)
    
#Displaying for Row Spacing    
    displayrow = Label(root, text = "", width = 10)
    displayrow.grid(row = 1, column = 0)
    displayrow = Label(root, text = "", width = 10)
    displayrow.grid(row = 4, column = 0)  
    displayrow = Label(root, text = "", width = 10)
    displayrow.grid(row = 7, column = 0)
    displayrow = Label(root, text = "", width = 10)
    displayrow.grid(row = 24, column = 0)
    displayrow = Label(root, text = "", width = 10)
    displayrow.grid(row = 26, column = 0)
    
#Yard User Input    
    yardtext = Label(root, text ="Yard/yd:", width = 20)
    yardtext.grid(row = 2, column = 1, stick = W)
    yardfield = Entry(root)
    yardfield.grid(row = 3, column = 1)
    
#Text Translate     
    metertext = Label(root, text ="Meter/m:", width = 15, font = "Arial 10 bold")
    metertext.grid(row = 8, column = 1, stick = W)
    hectometertext = Label(root, text ="Hectometer/hm:", width = 15, font = "Arial 10 bold")
    hectometertext.grid(row = 10, column = 1, stick = W)
    centimetertext = Label(root, text ="Centimeter/cm:", width = 15, font = "Arial 10 bold")
    centimetertext.grid(row = 12, column = 1, stick = W)
    kilometertext = Label(root, text ="Kilometer/km:", width = 15, font = "Arial 10 bold")
    kilometertext.grid(row = 14, column = 1, stick = W)
    decimetertext = Label(root, text ="Decimeter/dm:", width = 15, font = "Arial 10 bold")
    decimetertext.grid(row = 16, column = 1, stick = W)
    millimetertext = Label(root, text ="Millimeter/mm:", width = 15, font = "Arial 10 bold")
    millimetertext.grid(row = 18, column = 1, stick = W)
    inchestext = Label(root, text ="Inches/in:", width = 15, font = "Arial 10 bold")
    inchestext.grid(row = 20, column = 1, stick = W)
    foottext = Label(root, text ="Foot/ft:", width = 15, font = "Arial 10 bold")
    foottext.grid(row = 22, column = 1, stick = W)

#Text Translate Result
    metertranslate=Label(root, height = 1, width = 25, bg = "sky blue", font = "Arial 10 bold")
    metertranslate.grid(row = 9, column = 1)
    hectometertranslate=Label(root, height = 1, width = 25, bg = "sky blue", font = "Arial 10 bold")
    hectometertranslate.grid(row = 11, column = 1) 
    centimetertranslate=Label(root, height = 1, width = 25, bg = "sky blue", font = "Arial 10 bold")
    centimetertranslate.grid(row = 13, column = 1)
    kilometertranslate=Label(root, height = 1, width = 25, bg = "sky blue", font = "Arial 10 bold")
    kilometertranslate.grid(row = 15, column = 1)
    decimetertranslate=Label(root, height = 1, width = 25, bg = "sky blue", font = "Arial 10 bold")
    decimetertranslate.grid(row = 17, column = 1)
    millimetertranslate=Label(root, height = 1, width = 25, bg = "sky blue", font = "Arial 10 bold")
    millimetertranslate.grid(row = 19, column = 1)
    inchestranslate=Label(root, height = 1, width = 25, bg = "sky blue", font = "Arial 10 bold")
    inchestranslate.grid(row = 21, column = 1)
    foottranslate=Label(root, height = 1, width = 25, bg = "sky blue", font = "Arial 10 bold")
    foottranslate.grid(row = 23, column = 1)
      
#Button Exit
    btnexit = Button(root, text ="Translate Again", height = 2, width = 15, command = root.destroy, font = "Arial 10 bold")
    btnexit.grid(row = 25, column = 1)
    
#Translate Calculation      
    def yardtranslate():
        try:
            yard = float(yardfield.get())
            meter = yard * 0.9144
            hectometer = yard * 0.009144
            centimeter = yard * 91.44
            kilometer = yard * 0.0009144
            decimeter = yard * 9.144
            millimeter = yard * 914.4
            inches = yard * 36
            foot = yard * 3
 
#Displaying Translate Calculation 
            metertranslate.configure(text = meter)
            hectometertranslate.configure(text = hectometer)
            centimetertranslate.configure(text = centimeter)
            kilometertranslate.configure(text = kilometer)
            decimetertranslate.configure(text = decimeter)
            millimetertranslate.configure(text = millimeter)
            inchestranslate.configure(text = inches)
            foottranslate.configure(text = foot)
            
#When user not input integers            
        except:
            metertranslate.configure(text = "Check your yard value")
            hectometertranslate.configure(text = "Check your yard foot value")
            centimetertranslate.configure(text = "Check your yard foot value")
            kilometertranslate.configure(text = "Check your yard foot value")
            decimetertranslate.configure(text = "Check your yard foot value")
            millimetertranslate.configure(text = "Check your yard foot value")
            inchestranslate.configure(text = "Check your yard value")
            foottranslate.configure(text = "Check your yard value")
        
#Button Translate        
    btntranslate = Button(root, text ="Translate", height = 3, width = 10, command = yardtranslate)
    btntranslate.grid(row = 5, column = 1)
    
#Bottom Text      
    line = Label(root, text = "-------------------------------------", width = 30)
    line.grid(row = 27, column = 1)
    info = Label(root, text = "Distance Translation 2020", width = 20, font = "Calibre 8")
    info.grid(row = 28, column = 1)

#Displaying for Row Spacing  
displayrow = Label(root, text = "", width = 10)
displayrow.grid(row = 2, column = 0)
displayrow = Label(root, text = "")
displayrow.grid(row = 4, column = 0)
displayrow = Label(root, text = "")
displayrow.grid(row = 6, column = 0)
displayrow = Label(root, text = "", height = 2)
displayrow.grid(row = 8,column = 0)
displayrow = Label(root, text = "", height = 1)
displayrow.grid(row = 10,column = 0)

#Button Selection   
btnmeter = Button(root, text ="Meter", height = 3, width = 10, command = meterconvert)
btnmeter.grid(row = 3, column = 1)
btnhectometer = Button(root, text ="Hectometer", height = 3, width = 10, command = hectometerconvert)
btnhectometer.grid(row = 5, column = 1)
btncentimeter = Button(root, text ="Centimeter", height = 3, width = 10, command = centimeterconvert)
btncentimeter.grid(row = 7, column = 1)
btnkilometer = Button(root, text ="Kilometer", height = 3, width = 10, command = kilometerconvert)
btnkilometer.grid(row = 3, column = 2)
btndecimeter = Button(root, text ="Decimeter", height = 3, width = 10, command = decimeterconvert)
btndecimeter.grid(row = 5, column = 2)
btnmillimeter = Button(root, text ="Millimeter", height = 3, width = 10, command = millimeterconvert)
btnmillimeter.grid(row = 7, column = 2)
btninches = Button(root, text ="Inches", height = 3, width = 10, command = inchesconvert)
btninches.grid(row = 3, column = 3)
btnfoot = Button(root, text ="Foot", height = 3, width = 10, command = footconvert)
btnfoot.grid(row = 5, column = 3)
btnyard = Button(root, text ="Yard", height = 3, width = 10, command = yardconvert)
btnyard.grid(row = 7, column = 3)

#Button Exit
btnexit = Button(root, text ="Exit", height = 2, width = 10, command = root.destroy, font = "Arial 10 bold")
btnexit.grid(row = 9, column = 2)

#Bottom Text
line = Label(root, text = "-------------------------------------", width = 30)
line.grid(row =  11, column = 2)
info = Label(root, text = "Distance Translation 2020", width = 20, font = "Calibre 8")
info.grid(row =  12, column = 2)

root.mainloop()      #make window constantly open
#end of the code