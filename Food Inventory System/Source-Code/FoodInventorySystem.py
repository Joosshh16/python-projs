#start of the code
from tkinter import *           #import tkinter libraries
import tkinter.messagebox       #import tkinter messagebox
import sqlite3                   #import database  

window1 = Tk()                     #open window
window1.title("Food Inventory System")               #window title
window1.resizable (width=False, height = False)    #fixed size of the window

#Window Size
window1.geometry("800x550")


#Create or connect to  database
connect = sqlite3.connect("food.db")

#Create Cursor
conn = connect.cursor()

#create table, once the table created delete this syntax of code or make it as a comment
#conn.execute("CREATE TABLE tbl_fooddata(foodname TEXT, foodquantity TEXT, foodprice TEXT, foodstatus TEXT)")

#Window Title
title = Label(window1, text = "Food Inventory \nSystem", font="Arial 20 bold")
title.grid(row=0, column = 2)

#Row and Column Spacing
row = Label(window1, font="Arial 20 bold", width = 3)
row.grid(row = 0, column = 0)

row2 = Label(window1, font="Arial 20 bold")
row2.grid(row = 1, column = 1)

row3 = Label(window1, font="Arial 20 bold")
row3.grid(row = 2, column = 1)

#Insert Window
def insertdatawindow():
    
    insertwindow = Tk()  
#Window Size
    insertwindow.geometry("900x480")
    insertwindow.resizable (width=False, height = False)    #fixed size of the window

#Window Title
    titlename = Label(insertwindow, text = "Insert Data", font="Arial 30 bold", bd = 10)
    titlename.grid(row = 0, column = 2)

#Row and Column Spacing
    row = Label(insertwindow, width = 5)
    row.grid(row = 0, column =0) 
    row1 = Label(insertwindow, width = 5)
    row1.grid(row = 0, column =3)
    row2 = Label(insertwindow, width = 5)
    row2.grid(row = 5, column =0)
    row3 = Label(insertwindow, width = 5)
    row3.grid(row = 7, column =0)
    
#Text Label
    textfoodname = Label(insertwindow, text ="Food Name: ", width = 10, font="Arial 15 bold")
    textfoodname.grid(row = 1, column=1, stick = E)
    
    textfoodquantity = Label(insertwindow, text ="Food Quantity: ", width = 12, font="Arial 15 bold")
    textfoodquantity.grid(row = 2, column=1, stick = E)
    
    textfoodprice = Label(insertwindow, text ="Food Price: ", width = 10, font="Arial 15 bold")
    textfoodprice.grid(row = 3, column=1, stick = E)
    
    textfoodstatus = Label(insertwindow, text ="Food Status: ", width = 10, font="Arial 15 bold")
    textfoodstatus.grid(row = 4, column=1, stick = E)
    
    textdata = Label(insertwindow, width = 10, font="Arial 15 bold")
    textdata.grid(row = 8, column = 1, stick = E)
    
#Field Entry
    fieldfoodname = Entry(insertwindow, font="Arial 15 bold")
    fieldfoodname.grid(row = 1, column = 2)
    
    fieldfoodquantity = Entry(insertwindow, font="Arial 15 bold")
    fieldfoodquantity.grid(row = 2, column = 2)
    
    fieldfoodprice = Entry(insertwindow, font="Arial 15 bold")
    fieldfoodprice.grid(row = 3, column = 2)
    
    fieldfoodstatus = Entry(insertwindow, font="Arial 15 bold")
    fieldfoodstatus.grid(row = 4, column = 2)

#Clearing Data for Insert Window
    def reset():
        fieldfoodname.delete(0, 'end')
        fieldfoodquantity.delete(0, 'end')
        fieldfoodprice.delete(0, 'end')
        fieldfoodstatus.delete(0, 'end')
        
#Insert Data Function
    def insertdata():
        try:
            foodname = str(fieldfoodname.get())
            foodquantity = int(fieldfoodquantity.get())
            foodprice = float(fieldfoodprice.get())
            foodstatus = str(fieldfoodstatus.get())
            
#Create or connect to  database
            connect = sqlite3.connect("food.db")

#Create Cursor
            conn = connect.cursor()
            
#Insert Data            
            conn.execute("INSERT INTO tbl_fooddata VALUES(:fieldfoodname, :fieldfoodquantity, :fieldfoodprice, :fieldfoodstatus)",
                {
                     "fieldfoodname": foodname,
                     "fieldfoodquantity": foodquantity,
                     "fieldfoodprice": foodprice,
                     "fieldfoodstatus": foodstatus
                })
                    
#commit changes
            connect.commit()

#close connection
            connect.close()
            
            fieldfoodname.delete(0, END)
            fieldfoodquantity.delete(0, END)
            fieldfoodprice.delete(0, END)
            fieldfoodstatus.delete(0, END)
            
            textdata.configure(text = "Data Inserted")
        except:
#When the user input is invalid
            textdata.configure(text = "Wrong Data!")
            
        
#Buttons for Insert Window    
    btninsert = Button(insertwindow, text = "Insert", height = 2, width = 10, font= "Arial 12 bold", command = insertdata)
    btninsert.grid(row = 6, column = 1)
    
    btnreset = Button(insertwindow, text = "Reset", height = 2, width = 10, font= "Arial 12 bold", command = reset)
    btnreset.grid(row = 6, column = 2)
    
    btnexit = Button(insertwindow, text = "Back", height = 2, width = 10, font= "Arial 12 bold", command = insertwindow.destroy)
    btnexit.grid(row = 6, column = 3)
    
#Delete Window
def deletedatawindow():
    deletewindow = Tk()  
#Window Size
    deletewindow.geometry("850x430")
    deletewindow.resizable (width=False, height = False)    #fixed size of the window
    
#Window Title    
    titlename = Label(deletewindow, text = "Delete Data", font="Arial 30 bold", bd = 10)
    titlename.grid(row = 0, column = 2)

#Row and Column Spacing
    row = Label(deletewindow, width = 3)
    row.grid(row = 0, column = 0)
    row2 = Label(deletewindow, width = 3)
    row2.grid(row = 1, column = 0)
    row3 = Label(deletewindow, width = 3)
    row3.grid(row = 3, column = 0)
    row4 = Label(deletewindow, width = 3)
    row4.grid(row = 5, column = 0)
    
#Text Label
    textfoodid = Label(deletewindow, text ="Food ID: ", width = 10, font="Arial 15 bold")
    textfoodid.grid(row = 2, column=1, stick = E)
    
    textdata = Label(deletewindow, width = 11, font="Arial 15 bold")
    textdata.grid(row = 6, column = 1, stick = E)
    
#Field Entry
    fieldfoodid = Entry(deletewindow, font="Arial 15 bold")
    fieldfoodid.grid(row = 2, column = 2)
    
 #Clearing Data for Delete Window
    def reset():
        fieldfoodid.delete(0, 'end')

#Delete Data Function
    def deletedata():
        try:
            foodid = str(fieldfoodid.get())
            
#Create or connect to  database
            connect = sqlite3.connect("food.db")

#Create Cursor
            conn = connect.cursor()
        
#Delete Data
            conn.execute("DELETE from tbl_fooddata WHERE oid =?", (foodid))

 #commit changes
            connect.commit()

#close connection
            connect.close()
            
            fieldfoodid.delete(0, END)
            textdata.configure(text = "Data Deleted")
        except:
#When the user input is invalid
            textdata.configure(text = "Data Not Exist")
    
#Buttons for Delete Window
    btndelete = Button(deletewindow, text = "Delete", height = 2, width = 10, font= "Arial 12 bold", command = deletedata)
    btndelete.grid(row = 4, column = 1)
    
    btnreset = Button(deletewindow, text = "Reset", height = 2, width = 10, font= "Arial 12 bold", command = reset)
    btnreset.grid(row = 4, column = 2)
    
    btnexit = Button(deletewindow, text = "Back", height = 2, width = 10, font= "Arial 12 bold", command = deletewindow.destroy)
    btnexit.grid(row = 4, column = 3)
    
    
#View Data Window  
def viewdatawindow():
    
    viewwindow = Tk()
    
#Window Size
    viewwindow.geometry("800x600")
    viewwindow.resizable (width=False, height = False)    #fixed size of the window
    
#Window Title    
    titlename = Label(viewwindow, text = "Food Data", font="Arial 30 bold", bd = 10)
    titlename.grid(row = 0, column = 1)

#Row and Column Spacing  
    row = Label(viewwindow, font="Arial 30 bold", width = 3)
    row.grid(row = 0, column = 0)
    
    row1 = Label(viewwindow, font="Arial 30 bold", width = 3)
    row1.grid(row = 1, column = 1)
    
#Connect     
    connect = sqlite3.connect("food.db")

#Create Cursor
    conn = connect.cursor()
    
#Show Data
    conn.execute("SELECT *, oid FROM tbl_fooddata")
    data = conn.fetchall()
    
    printfoodname = ""
    printfoodquantity = ""
    printfoodprice = ""
    printfoodstatus = ""
    prindidkey =""
    for datas in data:
        data0 = str(datas[0])
        data1 = str(datas[1])
        data2 = str(datas[2])
        data3 = str(datas[3])
        idkey = str(datas[4])
        
        printfoodname += data0 +"\n"
        printfoodquantity += data1 +"\n"
        printfoodprice += data2 +"\n"
        printfoodstatus += data3 +"\n"
        prindidkey += idkey +"\n"

#Text Label Data
    textfoodidkey = Label(viewwindow, text = prindidkey, width = 5, font = "Arial 12 bold")
    textfoodidkey.grid(row = 2, column = 0, stick = E)
    
    textfoodname = Label(viewwindow, text = printfoodname, width = 5, font = "Arial 12 bold")
    textfoodname.grid(row = 2, column = 1, stick = E)
    
    textfoodquantity = Label(viewwindow, text = printfoodquantity, width = 5, font = "Arial 12 bold")
    textfoodquantity.grid(row = 2, column = 2, stick = E)
    
    textfoodprice = Label(viewwindow, text = printfoodprice, width = 5, font = "Arial 12 bold")
    textfoodprice.grid(row = 2, column = 3, stick = E)
    
    textfoodstatus = Label(viewwindow, text = printfoodstatus, width = 5, font = "Arial 12 bold")
    textfoodstatus.grid(row = 2, column = 4, stick = E)
    
#Button Exit
    btnexit = Button(viewwindow, text = "Back", height = 2, width = 10, font= "Arial 12 bold", command = viewwindow.destroy)
    btnexit.grid(row = 5, column = 1)

    
#commit changes
    connect.commit()

#close connection
    connect.close()
    
#Update Window
def updatedatawindow():
    updatewindow = Tk()  
#Window Size
    updatewindow.geometry("800x430")
    updatewindow.resizable (width=False, height = False)    #fixed size of the window

#Window Title
    titlename = Label(updatewindow, text = "Insert Data", font="Arial 30 bold", bd = 10)
    titlename.grid(row = 0, column = 2)

#Row and Column Spacing
    row = Label(updatewindow, width = 5)
    row.grid(row = 0, column =0) 
    row1 = Label(updatewindow, width = 5)
    row1.grid(row = 2, column =3)
    
#Text Label
    textfoodid = Label(updatewindow, text ="Food ID: ", width = 10, font="Arial 15 bold")
    textfoodid.grid(row = 1, column=1, stick = E)
    
#Field Entry
    fieldfoodid = Entry(updatewindow, font="Arial 15 bold")
    fieldfoodid.grid(row = 1, column = 2)
    
 #Clearing Data for Update Data Window
    def reset():
        fieldfoodid.delete(0, 'end')
        
    def updatedatawin():
        updatedata = Tk()  
#Window Size
        updatedata.geometry("850x500")
        updatedata.resizable (width=False, height = False)    #fixed size of the window

#Window Title
        titlename = Label(updatedata, text = "Update Data", font="Arial 30 bold", bd = 10)
        titlename.grid(row = 0, column = 2)
        
#Row and Column Spacing
        row = Label(updatedata, width = 5)
        row.grid(row = 0, column =0) 
        row1 = Label(updatedata, width = 5)
        row1.grid(row = 0, column =3)
        row2 = Label(updatedata, width = 5)
        row2.grid(row = 5, column =0)
        row3 = Label(updatedata, width = 5)
        row3.grid(row = 7, column =0)
        
#Text Label
        textfoodname = Label(updatedata, text ="Food Name: ", width = 10, font="Arial 15 bold")
        textfoodname.grid(row = 1, column=1, stick = E)
        
        textfoodquantity = Label(updatedata, text ="Food Quantity: ", width = 12, font="Arial 15 bold")
        textfoodquantity.grid(row = 2, column=1, stick = E)
        
        textfoodprice = Label(updatedata, text ="Food Price: ", width = 10, font="Arial 15 bold")
        textfoodprice.grid(row = 3, column=1, stick = E)
        
        textfoodstatus = Label(updatedata, text ="Food Status: ", width = 10, font="Arial 15 bold")
        textfoodstatus.grid(row =4, column=1, stick = E)
        
        textdata = Label(updatedata, width = 11, font="Arial 15 bold")
        textdata.grid(row = 8, column = 1, stick = E)
        
#Field Entry
        
        fieldfoodname = Entry(updatedata, font="Arial 15 bold")
        fieldfoodname.grid(row = 1, column = 2)
        
        fieldfoodquantity = Entry(updatedata, font="Arial 15 bold")
        fieldfoodquantity.grid(row = 2, column = 2)
        
        fieldfoodprice = Entry(updatedata, font="Arial 15 bold")
        fieldfoodprice.grid(row = 3, column = 2)
        
        fieldfoodstatus = Entry(updatedata, font="Arial 15 bold")
        fieldfoodstatus.grid(row = 4, column = 2)
        
        try:
#Connect     
            connect = sqlite3.connect("food.db")

#Create Cursor
            conn = connect.cursor()
                
            recordfood_id = fieldfoodid.get()
            
#Show Data
            conn.execute("SELECT * FROM tbl_fooddata WHERE foodname = " + recordfood_id)
            data = conn.fetchall()
            
#Attach Update Data                
            for datas in data:
                fieldfoodname.insert(0, datas[0])
                fieldfoodquantity.insert(0, datas[1])
                fieldfoodprice.insert(0, datas[2])
                fieldfoodstatus.insert(0, datas[3])
                
#commit changes
            connect.commit()

#close connection
            connect.close()
            
        except:
#When the user input not exist
            textdata.configure( text = "Data Not Exist")
            
        def updatedatas():
        #Connect     
            connect = sqlite3.connect("food.db")

                        #Create Cursor
            conn = connect.cursor()
                                    
            conn.execute("""UPDATE tbl_fooddata SET
                        foodname = :name,
                        foodquantity = :quantity,
                        foodprice = :price,
                        foodstatus = :status
                        WHERE oid = :oid""",
                        {
                        'name': fieldfoodname.get(),
                        'quantity': fieldfoodquantity.get(),
                        'price': fieldfoodprice.get(),
                        'status': fieldfoodstatus.get(),
                        'oid' : recordfood_id           
                        })
                                    
                        #commit changes
            connect.commit()

                        #close connection
            connect.close()
                    
       
        btnupdate = Button(updatedata, text = "Update", height = 2, width = 10, font= "Arial 12 bold", command = updatedatas)
        btnupdate.grid(row = 6, column = 1)
                    
        btnexit = Button(updatedata, text = "Back", height = 2, width = 10, font= "Arial 12 bold", command = updatedata.destroy)
        btnexit.grid(row = 6, column = 3)
        
              
#Buttons for Update Window    
    btnupdate = Button(updatewindow, text = "Update", height = 2, width = 10, font= "Arial 12 bold", command = updatedatawin)
    btnupdate.grid(row = 3, column = 1)
        
    btnreset = Button(updatewindow, text = "Reset", height = 2, width = 10, font= "Arial 12 bold", command = reset)
    btnreset.grid(row = 3, column = 2)
        
    btnexit = Button(updatewindow, text = "Back", height = 2, width = 10, font= "Arial 12 bold", command = updatewindow.destroy)
    btnexit.grid(row = 3, column = 3)
    
#For Exit Button
def exitbutton():
    exitbutton = tkinter.messagebox.askyesno("Confirmation", "Are you sure you want to exit?")
    if exitbutton > 0:
        window1.destroy()  
       
#Window Buttons
btninsert = Button(window1, text = "Insert", height = 3, width = 10, font= "Arial 12 bold", command = insertdatawindow)
btninsert.grid(row = 1, column = 1)

btnupdate = Button(window1, text = "Update", height = 3, width = 10, font=" Arial 12 bold", command = updatedatawindow)
btnupdate.grid(row = 3, column = 1)

btndelete = Button(window1, text = "Delete", height = 3, width = 10, font= "Arial 12 bold", command = deletedatawindow)
btndelete.grid(row = 1, column = 3)

btnview = Button(window1, text = "View Data", height = 3, width = 10, font= "Arial 12 bold", command = viewdatawindow)
btnview.grid(row = 3, column = 3)

btnexit = Button(window1, text = "Exit", height = 3, width = 10, font= "Arial 12 bold", command = exitbutton)
btnexit.grid(row = 4, column = 2)

#commit changes
connect.commit()

#close connection
connect.close()

window1.mainloop()      #make window constantly open
#end of the code