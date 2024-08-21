#start of the code
from tkinter import *           #import tkinter libraries       
import tkinter.messagebox       #import tkinter messagebox
import sqlite3                  #import sqlite3

db = sqlite3.connect('ClassroomSchedule.db')  #Create and Connect Database
cursor = db.cursor() #Create Cursor to Database
#Create Table for Database
cursor.execute("CREATE TABLE IF NOT EXISTS classdatatbl(roomid TEXT, roomnumber TEXT, roomsection TEXT, roomteacher TEXT, roomsched TEXT)")
db.commit() #Commit for Database

window1 = Tk()                     #open window
window1.title("Classroom Schedule")               #window title
window1.resizable (width=False, height = False)    #fixed size of the window

#Window Size
window1.geometry("480x455")

#Window Title
title = Label(window1, text = "Classroom Schedule", font="Arial 30 bold")
title.grid(row = 0, column = 1)

#Row and Column Spacing For Window1
column = Label(window1, width = 5)
column.grid(row = 0, column = 0)
column2 = Label(window1, width = 3)
column2.grid(row = 0, column = 2)
row = Label(window1, width = 3)
row.grid(row = 1, column = 0)
row2 = Label(window1, height = 2)
row2.grid(row = 2, column = 0)
row3 = Label(window1)
row3.grid(row = 3, column = 0)
row4 = Label(window1)
row4.grid(row = 7, column = 0)
row5 = Label(window1)
row5.grid(row = 9, column = 0)
row6 = Label(window1)
row6.grid(row = 11, column = 0)

#Text Label For Window1
textline = Label(window1, text ="_______________________", width = 20, height = 2, font="Arial 15 bold")
textline.grid(row = 4, column = 1)
textadmin = Label(window1, text ="Admin Pass: ", width = 20, font="Arial 15 bold")
textadmin.grid(row = 5, column = 1)

#Field Entry For Window1
fieldadmin = Entry(window1, show = "*", width = 20, font="Arial 10 bold")
fieldadmin.grid(row = 6 , column = 1)

#User Window
def user():
    user = Tk()                     #open window
    user.title("Classroom Schedule")               #window title
    user.resizable (width=False, height = False)    #fixed size of the window

#Window Size
    user.geometry("950x410")
    
    #Row and Column Spacing For Window1
    column = Label(user, width = 5)
    column.grid(row = 0, column = 0)
    column2 = Label(user, width = 5)
    column2.grid(row = 0, column = 3)
    column3 = Label(user, width = 5)
    column3.grid(row = 2, column = 3)
    
    title = Label(user, width = 15, font="Arial 12 bold")
    title.grid(row = 1, column = 1, stick = W)
#Field Entry For Window1
    textroom = Label(user, text ="Room Number", width = 20, height = 2, font="Arial 15 bold")
    textroom.grid(row = 2, column = 1)
    
    fieldroom = Entry(user, width = 20, font="Arial 10 bold")
    fieldroom.grid(row = 3 , column = 1)
    
    textsection = Label(user, text ="Section", width = 20, height = 2, font="Arial 15 bold")
    textsection.grid(row = 4, column = 1)
    
    fieldsection = Entry(user, width = 20, font="Arial 10 bold")
    fieldsection.grid(row = 5 , column = 1)
    
    textline = Label(user, text ="Classroom \nSchedule", font="Arial 15 bold")
    textline.grid(row = 0, column = 3)
    
#For Search Classroom in User Window    
    def searchsched():
        rname = str(fieldroom.get())
        rsec = str(fieldsection.get())
        
        conn = sqlite3.connect('ClassroomSchedule.db')
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM classdatatbl WHERE roomnumber=? OR roomsection=?",
                       (rname, rsec))
            
        data = cursor.fetchall()
            
        list1.delete(0,END)
        for row in data:
            list1.insert(END,(row))
            
        conn.close()
        
        title.configure(text = "Classroom Result")
    
    #Listbox for Data Result    
    list1=Listbox(user,height = 20, width = 85)
    list1.grid(row = 1,column = 4, rowspan = 7, columnspan=2)     
    scrl=Scrollbar(user)
    scrl.grid(row = 1,column = 3, sticky='ns',rowspan = 7)    
    list1.configure(yscrollcommand = scrl.set)
    scrl.configure(command=list1.yview)
    
    btnsearch = Button(user, text = "Search", height = 1, width = 10, font= "Arial 12 bold", command = searchsched)
    btnsearch.grid(row = 6, column = 1)
    
    btnexit = Button(user, text = "Exit", height = 1, width = 10, font= "Arial 12 bold", command = user.destroy)
    btnexit.grid(row = 7, column = 1)
        
#Admin Window 
def admin():
    passw = str(fieldadmin.get())
    
    if (passw == "admin"):
        data = Tk()                     #open window
        data.title("Classroom Schedule")               #window title
        data.resizable (width=False, height = False)    #fixed size of the window

#Window Size For Admin Window
        data.geometry("900x500")
        
#Row and Column Spacing For Admin Window
        row = Label(data, width = 3)
        row.grid(row = 0, column = 0)
        row2 = Label(data, width = 3)
        row2.grid(row = 7, column = 0)
        row2 = Label(data, width = 3)
        row2.grid(row = 7, column = 3)
        
#Data Status For Admin Window
        title = Label(data, width = 10, text = "Data Status", font="Arial 12 bold")
        title.grid(row = 1, column = 4, stick = W)
        
        #Text For Admin Window
        textroomid = Label(data, text = "Room ID:  ", width = 10, font="Arial 12 bold")
        textroomid.grid(row = 2, column = 4, stick = W)
        
        textroomnumber = Label(data, text = "Room Number:  ", width = 15, font="Arial 12 bold")
        textroomnumber.grid(row = 3, column = 4, stick = W)
        
        textroomsection = Label(data, text = "Room Section:  ", width = 15, font="Arial 12 bold")
        textroomsection.grid(row = 4, column = 4, stick = W)
        
        textroomteacher = Label(data, text = "Room Teacher:  ", width = 15, font="Arial 12 bold")
        textroomteacher.grid(row = 5, column = 4, stick = W)
        
        textroomsched = Label(data, text = "Room Schedule:  ", width = 15, font="Arial 12 bold")
        textroomsched.grid(row = 6, column = 4, stick = W)
        
#Field Entry For Admin Window
        fieldroomid = Entry(data, font="Arial 12 bold", width = 10)
        fieldroomid.grid(row = 2, column = 5)
        
        fieldroomnumber = Entry(data, font="Arial 12 bold", width = 10)
        fieldroomnumber.grid(row = 3, column = 5)
        
        fieldroomsection = Entry(data, font="Arial 12 bold", width = 10)
        fieldroomsection.grid(row = 4, column = 5)
        
        fieldroomteacher = Entry(data, font="Arial 12 bold", width = 10)
        fieldroomteacher.grid(row = 5, column = 5)
        
        fieldroomsched = Entry(data, font="Arial 12 bold", width = 10)
        fieldroomsched.grid(row = 6, column = 5)
        
#Selecting Data        
        def get_selected_row(event):
            global selected_data
            index=list1.curselection()
            selected_data=list1.get(index)
            fieldroomid.delete(0,END)
            fieldroomid.insert(END,selected_data[0])
            
            fieldroomnumber.delete(0,END)
            fieldroomnumber.insert(END,selected_data[1])
            
            fieldroomsection.delete(0,END)
            fieldroomsection.insert(END,selected_data[2])
            
            fieldroomteacher.delete(0,END)
            fieldroomteacher.insert(END,selected_data[3])
            
            fieldroomsched.delete(0,END)
            fieldroomsched.insert(END,selected_data[4])
            
#Showing Data                  
        def show():
            conn = sqlite3.connect('ClassroomSchedule.db')
            cursor = conn.cursor()
            cursor.execute('SELECT * FROM classdatatbl')
            data = cursor.fetchall()
            list1.delete(0,END)
            
            for datas in data:
                list1.insert(END,datas)
                
            conn.close()
            
#Searhing Data
        def search():
            rid = str(fieldroomid.get())
            rnumber = str(fieldroomnumber.get())
            rsection = str(fieldroomsection.get())
            rteacher = str(fieldroomteacher.get())
            rsched = str(fieldroomsched.get())    
            
            conn = sqlite3.connect('ClassroomSchedule.db')
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM classdatatbl WHERE roomid=? OR roomnumber=? OR roomsection=?  OR  roomteacher=?  OR  roomsched=?",
                           (rid, rnumber, rsection, rteacher, rsched))
            
            data = cursor.fetchall()
            
            list1.delete(0,END)
            for row in data:
                list1.insert(END,(row))
            
            conn.close()
        
#Inserting Data       
        def insert():
            try:
                rid = int(fieldroomid.get())
                rnumber = str(fieldroomnumber.get())
                rsection = str(fieldroomsection.get())
                rteacher = str(fieldroomteacher.get())
                rsched = str(fieldroomsched.get())
                
                conn = sqlite3.connect('ClassroomSchedule.db')
                
                with conn:
                    cursor = conn.cursor()
                    cursor.execute('INSERT INTO classdatatbl(roomid, roomnumber, roomsection, roomteacher, roomsched) VALUES(?,?,?,?,?)',
                                   (rid, rnumber, rsection, rteacher, rsched))
                    db.close()
                    
                fieldroomid.delete(0, 'end')
                fieldroomnumber.delete(0, 'end')
                fieldroomsection.delete(0, 'end')
                fieldroomteacher.delete(0, 'end')
                fieldroomsched.delete(0, 'end')
                
                conn.close()
                    
                title.configure(text = "Data Inserted")
        
                list1.delete(0,END)
                list1.insert(END,(rid,rnumber,rsection,rteacher,rsched))
            except:
                title.configure(text = "Wrong Data")
                
#Updating Data
        def update():
            try:
                rid = int(fieldroomid.get())
                rnumber = str(fieldroomnumber.get())
                rsection = str(fieldroomsection.get())
                rteacher = str(fieldroomteacher.get())
                rsched = str(fieldroomsched.get())
      
                conn = sqlite3.connect('ClassroomSchedule.db')
                cursor = conn.cursor()
                cursor.execute("UPDATE classdatatbl SET roomnumber = ?, roomsection =?, roomteacher =?, roomsched = ?  WHERE roomid = ?",
                               (rnumber, rsection, rteacher, rsched, rid))
                conn.commit()
                
                fieldroomid.delete(0, 'end')
                fieldroomnumber.delete(0, 'end')
                fieldroomsection.delete(0, 'end')
                fieldroomteacher.delete(0, 'end')
                fieldroomsched.delete(0, 'end')
                
                conn.close()
                title.configure(text = "Data Updated")
            except:
                title.configure(text = "Wrong Data")
                
#Deleting Data
        def delete():
            try:
                delet = int(fieldroomid.get())
                conn = sqlite3.connect('ClassroomSchedule.db')
                cursor = conn.cursor()
                cursor.execute("DELETE FROM classdatatbl WHERE roomid = ?",(delet,))
                conn.commit()
                
                fieldroomid.delete(0, 'end')
                fieldroomnumber.delete(0, 'end')
                fieldroomsection.delete(0, 'end')
                fieldroomteacher.delete(0, 'end')
                fieldroomsched.delete(0, 'end')
                
                conn.close()
                title.configure(text = "Data Deleted")
            except:
                title.configure(text = "Wrong Data")
                
#Buttons For Admin Window
        btninsert = Button(data, text = "Insert", height = 1, width = 10, font= "Arial 12 bold", command = insert)
        btninsert.grid(row = 8, column = 4)
        
        btnupdate = Button(data, text = "Update", height = 1, width = 10, font= "Arial 12 bold", command = update)
        btnupdate.grid(row = 9, column = 4)
        
        btndelete = Button(data, text = "Delete", height = 1, width = 10, font= "Arial 12 bold", command = delete)
        btndelete.grid(row = 10, column = 4)
        
        btnsearch = Button(data, text = "Search", height = 1, width = 10, font= "Arial 12 bold", command = search)
        btnsearch.grid(row = 8, column = 5)
        
        btnshow = Button(data, text = "Show", height = 1, width = 10, font= "Arial 12 bold", command = show)
        btnshow.grid(row = 9, column = 5)
        
        btnexit = Button(data, text = "Exit", height = 1, width = 10, font= "Arial 12 bold", command = data.destroy)
        btnexit.grid(row = 10, column = 5)
                 
#Text For Admin Window
        textroomdata = Label(data, text = "Classroom \nSchedule \nDatabase", font="Arial 12 bold")
        textroomdata.grid(row = 0, column = 2, stick = E)
        
#Listbox for Data       
        list1=Listbox(data,height = 20, width = 80)
        list1.grid(row = 1, column = 2 , rowspan = 7, columnspan=2)
        scrl=Scrollbar(data)
        scrl.grid(row = 1,column = 1, sticky='ns',rowspan = 7)
        list1.configure(yscrollcommand = scrl.set)
        scrl.configure(command=list1.yview)
        list1.bind('<<ListboxSelect>>',get_selected_row)
           
    else:
#If the admin input wrong password
        tkinter.messagebox.showinfo("Input Invalid", "Wrong Admin Input")
        
#Button Reset For Window1
btnschedule = Button(window1, text ="Search \nRoom Schedule", height = 2, width = 15, font="Arial 10 bold", command = user)
btnschedule.grid(row = 3, column = 1)

btnadmin = Button(window1, text ="Admin", height = 2, width = 15, font="Arial 10 bold", command = admin)
btnadmin.grid(row = 8, column = 1)

btnexit = Button(window1, text ="Exit", height = 2, width = 10, font="Arial 10 bold", command = window1.destroy)
btnexit.grid(row = 10, column = 1)

#Bottom Text
textline = Label(window1, text ="---------------------------------", width = 20)
textline.grid(row = 12, column = 1)
textinfo = Label(window1, text ="Classroom Schedule 2020", width = 20)
textinfo.grid(row = 13, column = 1)

window1.mainloop()      #make window constantly open
#end of the code