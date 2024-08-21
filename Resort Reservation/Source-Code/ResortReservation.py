#start of the code
from tkinter import *           #import tkinter libraries       
import tkinter.messagebox       #import tkinter messagebox
import sqlite3                  #import sqlite3

db = sqlite3.connect('ResortReservation.db')  #Create and Connect Database
cursor = db.cursor() #Create Cursor to Database
#Create Table for Database
cursor.execute("CREATE TABLE IF NOT EXISTS reservationdata(resid TEXT, resname TEXT, rescontact TEXT, resdate TEXT, restime TEXT, respax TEXT, resstatus TEXT)")
db.commit() #Commit for Database


window1 = Tk()                     #open window
window1.title("Resort Reservation")               #window title
window1.resizable (width=False, height = False)    #fixed size of the window

#Window Size
window1.geometry("450x480")

#Window Title
title = Label(window1, text = "Resort Reservation", font="Arial 30 bold")
title.grid(row = 0, column = 1)

#Row and Column Spacing For Window1
column = Label(window1, width = 5)
column.grid(row = 0, column = 0)
row = Label(window1)
row.grid(row = 1, column = 0)
row2 = Label(window1)
row2.grid(row = 5, column = 0)
row3 = Label(window1)
row3.grid(row = 8, column = 0)
row4 = Label(window1)
row4.grid(row = 10, column = 0)
row5 = Label(window1)
row5.grid(row = 12, column = 0)

#Text Label For Window1
textline = Label(window1, text ="_______________________", width = 20, height = 2, font="Arial 15 bold")
textline.grid(row = 4, column = 1)

textadmin = Label(window1, text ="Admin Password", width = 20, font="Arial 15 bold")
textadmin.grid(row = 6, column = 1)

#Field Entry For Window1
fieldadmin = Entry(window1, show = "*", width = 20, font="Arial 10 bold")
fieldadmin.grid(row = 7 , column = 1)

#User Window
def user():
    window1.destroy()
    reserve = Tk()                     #open window
    reserve.title("Resort Reservation")               #window title
    reserve.resizable (width=False, height = False)    #fixed size of the window
    
    #Window Size
    reserve.geometry("625x500")
    
#Row and Column Spacing For Reserve Window
    column = Label(reserve, width = 5)
    column.grid(row = 0, column = 0)
    row = Label(reserve)
    row.grid(row = 1, column = 0)
    row2= Label(reserve)
    row2.grid(row = 3, column = 0)
    row3= Label(reserve)
    row3.grid(row = 6, column = 0)
    row4= Label(reserve)
    row4.grid(row = 9, column = 0)
    row5= Label(reserve)
    row5.grid(row = 12, column = 0)
    row6= Label(reserve)
    row6.grid(row = 14, column = 0)
    row6= Label(reserve)
    row6.grid(row = 16, column = 0)

#Reserve Window Title
    title = Label(reserve, text = "Resort Reservation", font="Arial 20 bold")
    title.grid(row = 0, column = 3)
    
    info = Label(reserve, text = "Input all data needed to reserve resort", font="Arial 10")
    info.grid(row = 2, column = 3)
    
#Data Status For Reserve Window
    textrname = Label(reserve, width = 10, text = "Name", font="Arial 12 bold")
    textrname.grid(row = 4, column = 2)
    
    textrcontact = Label(reserve, width = 15, text = "Contact Number", font="Arial 12 bold")
    textrcontact.grid(row = 4, column = 4)
    
    textrdate = Label(reserve, width = 10, text = "Date", font="Arial 12 bold")
    textrdate.grid(row = 7, column = 2)
    
    textrtime = Label(reserve, width = 10, text = "Time", font="Arial 12 bold")
    textrtime.grid(row = 7, column = 4)
    
    textrpax = Label(reserve, width = 10, text = "Person/s", font="Arial 12 bold")
    textrpax.grid(row = 10, column = 3)
    
#Field Entry For Reserve Window
    fieldrname = Entry(reserve, font="Arial 12 bold", width = 15)
    fieldrname.grid(row = 5, column = 2)
    
    fieldrcontact = Entry(reserve, font="Arial 12 bold", width = 15)
    fieldrcontact.grid(row = 5, column = 4)
    
    fieldrdate = Entry(reserve, font="Arial 12 bold", width = 15)
    fieldrdate.grid(row = 8, column = 2)
    
    fieldrtime = Entry(reserve, font="Arial 12 bold", width = 15)
    fieldrtime.grid(row = 8, column = 4)
    
    fieldrpax = Entry(reserve, font="Arial 12 bold", width = 15)
    fieldrpax.grid(row = 11, column = 3)
    
#Reservation for Resort Through Reserve Window
    def reservedata():
        try:
            rname = str(fieldrname.get())
            rcontact = str(fieldrcontact.get())
            rdate = str(fieldrdate.get())
            rtime = str(fieldrtime.get())
            rpax = int(fieldrpax.get())
            
            conn = sqlite3.connect('ResortReservation.db')
                
            with conn:
                cursor = conn.cursor()
                cursor.execute('INSERT INTO reservationdata(resname, rescontact, resdate, restime, respax) VALUES(?,?,?,?,?)',
                               (rname, rcontact, rdate, rtime, rpax))
                    
            conn.close()
            
            tkinter.messagebox.showinfo("Reserve Success", "You input data to reserve, wait for approval in a few days") 
            reserve.destroy()
        except:
            tkinter.messagebox.showinfo("Invalid Input", "Please Check your data to reserve") 
    
#Buttons For Reserve Window
    btnreserve = Button(reserve, text ="Reserve", height = 3, width = 15, font="Arial 10 bold", command = reservedata)
    btnreserve.grid(row = 13, column = 3)
    
    btncancel = Button(reserve, text ="Cancel", height = 2, width = 10, font="Arial 10 bold", command = reserve.destroy)
    btncancel.grid(row = 15, column = 3)
   
#Bottom Text For Reserve Window
    textline = Label(reserve, text ="-------------------------------------", width = 20)
    textline.grid(row = 17, column = 3)
    textinfo = Label(reserve, text ="Resort Reservation 2020", width = 20)
    textinfo.grid(row = 18, column = 3)
   
#Admin Window
def admin():
    passw = str(fieldadmin.get())
    
    if (passw == "admin"):
        data = Tk()                     #open window
        data.title("Classroom Schedule")               #window title
        data.resizable (width=False, height = False)    #fixed size of the window

#Window Size For Admin Window
        data.geometry("1050x500")
        
#Row and Column Spacing For Admin Window
        row = Label(data, width = 3)
        row.grid(row = 0, column = 0)
        
#Text For Admin Window
        textroomdata = Label(data, text = "Resort Reservation \nDatabase", font="Arial 12 bold")
        textroomdata.grid(row = 0, column = 2, stick = E)
        
    
#Data Status For Admin Window
        title = Label(data, width = 10, text = "Data Status", font="Arial 12 bold")
        title.grid(row = 1, column = 4, stick = W)
        
#Text For Admin Window
        textresid = Label(data, text = "Reserve ID:", width = 14, font="Arial 12 bold")
        textresid.grid(row = 2, column = 4, stick = W)
        
        textresname = Label(data, text = "Name:", width = 14, font="Arial 12 bold")
        textresname.grid(row = 3, column = 4, stick = W)
        
        textrescontact = Label(data, text = "Contact Number:", width = 14, font="Arial 12 bold")
        textrescontact.grid(row = 4, column = 4, stick = W)
        
        textresdate = Label(data, text = "Reserve Date:", width = 14, font="Arial 12 bold")
        textresdate.grid(row = 2, column = 6, stick = W)
        
        textrestime = Label(data, text = "Reserve Time:  ", width = 14, font="Arial 12 bold")
        textrestime.grid(row = 3, column = 6, stick = W)
        
        textrespax = Label(data, text = "Reserve Pax:", width = 14, font="Arial 12 bold")
        textrespax.grid(row = 4, column = 6, stick = W)
        
        textresstat = Label(data, text = "Reserve Status:  ", width = 14, font="Arial 12 bold")
        textresstat.grid(row = 5, column = 4, stick = W)
        
#Field Entry For Admin Window
        fieldresid = Entry(data, font="Arial 12 bold", width = 10)
        fieldresid.grid(row = 2, column = 5)
        
        fieldresname = Entry(data, font="Arial 12 bold", width = 10)
        fieldresname.grid(row = 3, column = 5)
        
        fieldrescontact = Entry(data, font="Arial 12 bold", width = 10)
        fieldrescontact.grid(row = 4, column = 5)
        
        fieldresdate = Entry(data, font="Arial 12 bold", width = 10)
        fieldresdate.grid(row = 2, column = 7)
        
        fieldrestime = Entry(data, font="Arial 12 bold", width = 10)
        fieldrestime.grid(row = 3, column = 7)
        
        fieldrespax = Entry(data, font="Arial 12 bold", width = 10)
        fieldrespax.grid(row = 4, column = 7)
        
        fieldresstat = Entry(data, font="Arial 12 bold", width = 10)
        fieldresstat.grid(row = 5, column = 5)
        
#Selecting Data        
        def get_selected_row(event):
            global selected_data
            index=listdata.curselection()
            selected_data=listdata.get(index)
            fieldresid.delete(0,END)
            fieldresid.insert(END,selected_data[0])
            
            fieldresname.delete(0,END)
            fieldresname.insert(END,selected_data[1])
            
            fieldrescontact.delete(0,END)
            fieldrescontact.insert(END,selected_data[2])
            
            fieldresdate.delete(0,END)
            fieldresdate.insert(END,selected_data[3])
            
            fieldrestime.delete(0,END)
            fieldrestime.insert(END,selected_data[4])
            
            fieldrespax.delete(0,END)
            fieldrespax.insert(END,selected_data[5])
            
            fieldresstat.delete(0,END)
            fieldresstat.insert(END,selected_data[6])
            
#Showing Data                  
        def show():
            conn = sqlite3.connect('ResortReservation.db')
            cursor = conn.cursor()
            cursor.execute('SELECT * FROM reservationdata')
            data = cursor.fetchall()
            listdata.delete(0,END)
            
            for datas in data:
                listdata.insert(END,datas)
                
            conn.close()
            
#Searching Data
        def search():
            rid = str(fieldresid.get())
            rname = str(fieldresname.get())
            rcontact = str(fieldrescontact.get())
            rdate = str(fieldresdate.get())
            rtime = str(fieldrestime.get())
            rpax = str(fieldrespax.get())
            rstat = str(fieldresstat.get())  
            
            conn = sqlite3.connect('ResortReservation.db')
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM reservationdata WHERE resid=? OR resname=? OR rescontact=? OR resdate=? OR restime=? OR respax=? OR resstatus=?",
                           (rid, rname, rcontact, rdate, rtime, rpax, rstat))
            
            data = cursor.fetchall()
            
            listdata.delete(0,END)
            for row in data:
                listdata.insert(END,(row))
            
            conn.close()
        
        
#Inserting Data       
        def insert():
            try:
                rid = str(fieldresid.get())
                rname = str(fieldresname.get())
                rcontact = str(fieldrescontact.get())
                rdate = str(fieldresdate.get())
                rtime = str(fieldrestime.get())
                rpax = int(fieldrespax.get())
                rstat = str(fieldresstat.get())
                
                conn = sqlite3.connect('ResortReservation.db')
                
                with conn:
                    cursor = conn.cursor()
                    cursor.execute('INSERT INTO reservationdata(resid, resname, rescontact, resdate, restime, respax, resstatus) VALUES(?,?,?,?,?,?,?)',
                                   (rid, rname, rcontact, rdate, rtime, rpax, rstat))
                    
                fieldresid.delete(0, 'end')
                fieldresname.delete(0, 'end')
                fieldrescontact.delete(0, 'end')
                fieldresdate.delete(0, 'end')
                fieldrestime.delete(0, 'end')
                fieldrespax.delete(0, 'end')
                fieldresstat.delete(0, 'end')
                
                conn.close()
                    
                title.configure(text = "Data Inserted")
        
                listdata.delete(0,END)
                listdata.insert(END,(rid,rname,rcontact,rdate,rtime,rpax,rstat))
            except:
                title.configure(text = "Wrong Data")
                
#Updating Data
        def update():
            try:
                rid = str(fieldresid.get())
                rname = str(fieldresname.get())
                rcontact = str(fieldrescontact.get())
                rdate = str(fieldresdate.get())
                rtime = str(fieldrestime.get())
                rpax = int(fieldrespax.get())
                rstat = str(fieldresstat.get())
      
                conn = sqlite3.connect('ResortReservation.db')
                cursor = conn.cursor()
                cursor.execute("UPDATE reservationdata SET resid = ?, rescontact =?, resdate =?, restime=?, respax=?, resstatus=?  WHERE resname = ?",
                               (rid, rcontact, rdate, rtime, rpax, rstat, rname))
                conn.commit()
                
                fieldresid.delete(0, 'end')
                fieldresname.delete(0, 'end')
                fieldrescontact.delete(0, 'end')
                fieldresdate.delete(0, 'end')
                fieldrestime.delete(0, 'end')
                fieldrespax.delete(0, 'end')
                fieldresstat.delete(0, 'end')
                
                conn.close()
                title.configure(text = "Data Updated")
            except:
                title.configure(text = "Wrong Data")
                
#Deleting Data
        def delete():
            try:
                passw = str(fieldresname.get())
                conn = sqlite3.connect('ResortReservation.db')
                cursor = conn.cursor()
                cursor.execute("DELETE FROM reservationdata WHERE resname = ?",(passw,))
                conn.commit()
                
                fieldresid.delete(0, 'end')
                fieldresname.delete(0, 'end')
                fieldrescontact.delete(0, 'end')
                fieldresdate.delete(0, 'end')
                fieldrestime.delete(0, 'end')
                fieldrespax.delete(0, 'end')
                fieldresstat.delete(0, 'end')
                
                conn.close()
                title.configure(text = "Data Deleted")
            except:
                title.configure(text = "Wrong Data")
                
#Listbox for Data       
        listdata=Listbox(data,height = 25, width = 80)
        listdata.grid(row = 1, column = 2 , rowspan = 7, columnspan=2)
        scrldata=Scrollbar(data)
        scrldata.grid(row = 1,column = 1, sticky='ns',rowspan = 7)
        listdata.configure(yscrollcommand = scrldata.set)
        scrldata.configure(command=listdata.yview)
        listdata.bind('<<ListboxSelect>>',get_selected_row)
        
#Buttons For Admin Window
        btninsert = Button(data, text = "Insert", height = 2, width = 10, font= "Arial 12 bold", command = insert)
        btninsert.grid(row = 6, column = 4)
        
        btnupdate = Button(data, text = "Update \n Approve", height = 2, width = 10, font= "Arial 12 bold", command = update)
        btnupdate.grid(row = 6, column = 5)
        
        btndelete = Button(data, text = "Delete", height = 2, width = 10, font= "Arial 12 bold", command = delete)
        btndelete.grid(row = 6, column = 6)
        
        btnshow = Button(data, text = "Show", height = 2, width = 10, font= "Arial 12 bold", command = show)
        btnshow.grid(row = 7, column = 4)
        
        btnsearch = Button(data, text = "Search", height = 2, width = 10, font= "Arial 12 bold", command = search)
        btnsearch.grid(row = 7, column = 5)
        
        btnexit = Button(data, text = "Exit", height = 2, width = 10, font= "Arial 12 bold", command = data.destroy)
        btnexit.grid(row = 7, column = 6)
    else:
#If the admin input wrong password
        tkinter.messagebox.showinfo("Input Invalid", "Wrong Admin Input")
        
        

#Buttons For Window1
btnreserve = Button(window1, text ="Reserve Now", height = 3, width = 15, font="Arial 10 bold", command = user)
btnreserve.grid(row = 3, column = 1)

btnadmin = Button(window1, text ="Admin", height = 3, width = 15, font="Arial 10 bold", command = admin)
btnadmin.grid(row = 9, column = 1)

btnadmin = Button(window1, text ="Exit", height = 2, width = 10, font="Arial 10 bold", command = window1.destroy)
btnadmin.grid(row = 11, column = 1)

#Bottom Text For Window1
textline = Label(window1, text ="-------------------------------------", width = 20)
textline.grid(row = 13, column = 1)
textinfo = Label(window1, text ="Resort Reservation 2020", width = 20)
textinfo.grid(row = 14, column = 1)

window1.mainloop()   
#end of the code