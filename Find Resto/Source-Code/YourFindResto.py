from tkinter import *           #import tkinter
import sqlite3                  #import sqlite3
import tkinter.messagebox       #import tkinter messagebox

window1 = Tk()                     #open window
window1.title("Find Resto")               #window title
window1.resizable (width=False, height = False)    #fixed size of the window

db = sqlite3.connect('RestoData.db')  #Create and Connect Database
cursor = db.cursor() #Create Cursor to Database
#Create Table for Database
cursor.execute("CREATE TABLE IF NOT EXISTS restotbl(restoid TEXT, restoname TEXT, restoplace TEXT, restotime TEXT, restoprice TEXT)")
db.commit() #Commit for Database

#Window1 Size
window1.geometry("400x350")

#Window1 Frames
title = Frame(window1, width = 800, height = 150  , bd = 10)
title.pack(side = TOP)

windowdata = Frame(window1, width = 600, height = 300 )
windowdata.pack(side = LEFT)

user = Frame(windowdata, width = 400, height = 500 , bd = 10)
user.pack(side = LEFT)

admin = Frame(windowdata, width = 400, height = 500 , bd = 10)
admin.pack(side = RIGHT)

b = Frame(windowdata, width = 150, height = 500 , bd = 10)
b.pack(side = BOTTOM)


#Window Title
texttitle = Label(title, text = "Your Find Resto", font="Arial 20 bold")
texttitle.grid(row= 0, column = 0)

#Spacing for Frame admin
textadminpass = Label(admin, width = 2)
textadminpass.grid(row = 2, column = 0)

#Spacing for Frame user
textuser = Label(user, width = 3)
textuser.grid(row = 0, column = 0)

#Text Windows
textadminpass = Label(admin, text = "  Admin Pass  ", width = 10, font="Arial 20 bold")
textadminpass.grid(row = 0, column = 1, stick = W)
    
#Field Entry
fieldadminpass = Entry(admin, show = "*", font="Arial 12 bold", width = 10)
fieldadminpass.grid(row = 1, column = 1)

#Text Variables Data
restoid = StringVar()
restoname = StringVar()
restoplace = StringVar()
restotime = StringVar()
restoprice = StringVar()

#For Exit Window
def exitwindow():
    exitwindow = tkinter.messagebox.askyesno("Confirmation", "Are you sure you want to cancel your delivery?")
    if exitwindow > 0:
        window1.destroy()

#For User Window
def userwindow():
    user = Tk()                     #open window
    user.title("Find Resto")               #window title
    user.resizable (width=False, height = False)    #fixed size of the window
    
#Window Size For Admin Window
    user.geometry("870x430")
    
#Row and Column Spacing For Admin Window
    row = Label(user, width = 3)
    row.grid(row = 0, column = 0)
    
#Window Status    
    title = Label(user, width = 10, font="Arial 12 bold")
    title.grid(row = 1, column = 1, stick = W)
    
#Text For User Window 
    textrestoname = Label(user, text = "Resto Name:  ", width = 10, font="Arial 12 bold")
    textrestoname.grid(row = 2, column = 1, stick = W)
        
    textrestoplace = Label(user, text = "Resto Place:  ", width = 10, font="Arial 12 bold")
    textrestoplace.grid(row = 3, column = 1, stick = W)
    
#Field Entry For User Window
    fieldrestoname = Entry(user, font="Arial 12 bold", width = 10, textvar = restoname)
    fieldrestoname.grid(row = 2, column = 2)
        
    fieldrestoplace = Entry(user, font="Arial 12 bold", width = 10, textvar = restoplace)
    fieldrestoplace.grid(row = 3, column = 2)
    
#For Search Resto in User Window
    def searchresto():
            
        rname = str(fieldrestoname.get())
        rplace = str(fieldrestoplace.get())
            
        conn = sqlite3.connect('RestoData.db')
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM restotbl WHERE restoname=? OR restoplace=?",
                       (rname, rplace))
            
        data = cursor.fetchall()
            
        list1.delete(0,END)
        for row in data:
            list1.insert(END,(row))
            
        conn.close()
        
        title.configure(text = "Resto Result")
    
#Text Windows For User Window
    textrestodata = Label(user, text = "Your Resto", font="Arial 12 bold")
    textrestodata.grid(row = 0, column = 3, stick = W)
    
#Listbox for Data Result    
    list1=Listbox(user,height = 20, width = 85)
    list1.grid(row = 1,column = 4 , rowspan = 7, columnspan=2)     
    scrl=Scrollbar(user)
    scrl.grid(row = 1,column = 3, sticky='ns',rowspan = 7)    
    list1.configure(yscrollcommand = scrl.set)
    scrl.configure(command=list1.yview)
    
#Buttons for User Window
    btnsearchresto = Button(user, text = "Search \n My Resto", height = 2, width = 10, font= "Arial 12 bold", command = searchresto)
    btnsearchresto.grid(row = 4, column = 2)
    
    btnexit = Button(user, text = "Exit", height = 1, width = 10, font= "Arial 12 bold", command = user.destroy)
    btnexit.grid(row = 5, column = 2)

#For Admin Window
def adminwindow():
    passw = str(fieldadminpass.get())
    
#Password for Admin
    if (passw == "admin"):
        data = Tk()                     #open window
        data.title("Find Resto")               #window title
        data.resizable (width=False, height = False)    #fixed size of the window

#Window Size For Admin Window
        data.geometry("900x490")
        
#Row and Column Spacing For Admin Window
        row = Label(data, width = 3)
        row.grid(row = 0, column = 0)
        row2 = Label(data, width = 3)
        row2.grid(row = 1, column = 0)
        row3 = Label(data, width = 3)
        row3.grid(row = 7, column = 0)
        row4 = Label(data, width = 3)
        row4.grid(row = 12, column = 0)
        
#Data Status For Admin Window
        title = Label(data, width = 10, text = "Data Status", font="Arial 12 bold")
        title.grid(row = 1, column = 1, stick = W)
        
#Text For Admin Window
        textrestoid = Label(data, text = "Resto ID:  ", width = 10, font="Arial 12 bold")
        textrestoid.grid(row = 2, column = 1, stick = W)
        
        textrestoname = Label(data, text = "Resto Name:  ", width = 10, font="Arial 12 bold")
        textrestoname.grid(row = 3, column = 1, stick = W)
        
        textrestoplace = Label(data, text = "Resto Place:  ", width = 10, font="Arial 12 bold")
        textrestoplace.grid(row = 4, column = 1, stick = W)
        
        textrestotime = Label(data, text = "Resto Time:  ", width = 10, font="Arial 12 bold")
        textrestotime.grid(row = 5, column = 1, stick = W)
        
        textrestoprice = Label(data, text = "Resto Price:  ", width = 10, font="Arial 12 bold")
        textrestoprice.grid(row = 6, column = 1, stick = W)
        
#Field Entry For Admin Window
        fieldrestoid = Entry(data, font="Arial 12 bold", width = 10, textvar = restoid)
        fieldrestoid.grid(row = 2, column = 2)
        
        fieldrestoname = Entry(data, font="Arial 12 bold", width = 10, textvar = restoname)
        fieldrestoname.grid(row = 3, column = 2)
        
        fieldrestoplace = Entry(data, font="Arial 12 bold", width = 10, textvar = restoplace)
        fieldrestoplace.grid(row = 4, column = 2)
        
        fieldrestotime = Entry(data, font="Arial 12 bold", width = 10, textvar = restotime)
        fieldrestotime.grid(row = 5, column = 2)
        
        fieldrestoprice = Entry(data, font="Arial 12 bold", width = 10, textvar = restoprice)
        fieldrestoprice.grid(row = 6, column = 2)
        
#Selecting Data        
        def get_selected_row(event):
            global selected_data
            index=list1.curselection()
            selected_data=list1.get(index)
            fieldrestoid.delete(0,END)
            fieldrestoid.insert(END,selected_data[0])
            
            fieldrestoname.delete(0,END)
            fieldrestoname.insert(END,selected_data[1])
            
            fieldrestoplace.delete(0,END)
            fieldrestoplace.insert(END,selected_data[2])
            
            fieldrestotime.delete(0,END)
            fieldrestotime.insert(END,selected_data[3])
            
            fieldrestoprice.delete(0,END)
            fieldrestoprice.insert(END,selected_data[4])
            
#Searhing Data
        def search():
            
            rid = str(fieldrestoid.get())
            rname = str(fieldrestoname.get())
            rplace = str(fieldrestoplace.get())
            rtime = str(fieldrestotime.get())
            rprice = str(fieldrestoprice.get())
            
            conn = sqlite3.connect('RestoData.db')
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM restotbl WHERE restoid=? OR restoname=? OR restoplace=?  OR  restotime=?  OR  restoprice=?",
                           (rid, rname, rplace, rtime, rprice))
            
            data = cursor.fetchall()
            
            list1.delete(0,END)
            for row in data:
                list1.insert(END,(row))
            
            conn.close()
        
#Inserting Data       
        def insert():
            try:
                rid = int(fieldrestoid.get())
                rname = str(fieldrestoname.get())
                rplace = str(fieldrestoplace.get())
                rtime = str(fieldrestotime.get())
                rprice = str(fieldrestoprice.get())
                
                conn = sqlite3.connect('RestoData.db')
                
                with conn:
                    cursor = conn.cursor()
                    cursor.execute('INSERT INTO restotbl(restoid, restoname, restoplace, restotime, restoprice) VALUES(?,?,?,?,?)',
                                   (rid, rname, rplace, rtime, rprice))
                    db.close()
                    
                fieldrestoid.delete(0, 'end')
                fieldrestoname.delete(0, 'end')
                fieldrestoplace.delete(0, 'end')
                fieldrestotime.delete(0, 'end')
                fieldrestoprice.delete(0, 'end')
                
                conn.close()
                    
                title.configure(text = "Data Inserted")
        
                list1.delete(0,END)
                list1.insert(END,(rid,rname,rplace,rtime,rprice))
            except:
                title.configure(text = "Wrong Data")
                
#Showing Data                  
        def show():
            conn = sqlite3.connect('RestoData.db')
            cursor = conn.cursor()
            cursor.execute('SELECT * FROM restotbl')
            data = cursor.fetchall()
            list1.delete(0,END)
            
            for datas in data:
                list1.insert(END,datas)
                
            conn.close()
            
#Updating Data
        def update():
            try:
                rid = int(fieldrestoid.get())
                rname = str(fieldrestoname.get())
                rplace = str(fieldrestoplace.get())
                rtime = str(fieldrestotime.get())
                rprice = str(fieldrestoprice.get())
      
                conn = sqlite3.connect('RestoData.db')
                cursor = conn.cursor()
                cursor.execute("UPDATE restotbl SET restoname = ?, restoplace =?, restotime =?, restoprice = ?  WHERE restoid = ?",
                               (rname, rplace, rtime, rprice, rid))
                conn.commit()
                
                fieldrestoid.delete(0, 'end')
                fieldrestoname.delete(0, 'end')
                fieldrestoplace.delete(0, 'end')
                fieldrestotime.delete(0, 'end')
                fieldrestoprice.delete(0, 'end')
                
                conn.close()
                title.configure(text = "Data Updated")
            except:
                title.configure(text = "Wrong Data")
        
#Deleting Data
        def delete():
            try:
                dele = int(fieldrestoid.get())
                conn = sqlite3.connect('RestoData.db')
                cursor = conn.cursor()
                cursor.execute("DELETE FROM restotbl WHERE restoid = ?",(dele,))
                conn.commit()
                
                fieldrestoid.delete(0, 'end')
                fieldrestoname.delete(0, 'end')
                fieldrestoplace.delete(0, 'end')
                fieldrestotime.delete(0, 'end')
                fieldrestoprice.delete(0, 'end')
                
                conn.close()
                title.configure(text = "Data Deleted")
            except:
                title.configure(text = "Wrong Data")
        
#Buttons For Admin Window
        btninsert = Button(data, text = "Insert", height = 1, width = 10, font= "Arial 12 bold", command = insert)
        btninsert.grid(row = 8, column = 1)
        
        btnupdate = Button(data, text = "Update", height = 1, width = 10, font= "Arial 12 bold", command = update)
        btnupdate.grid(row = 9, column = 1)
        
        btndelete = Button(data, text = "Delete", height = 1, width = 10, font= "Arial 12 bold", command = delete)
        btndelete.grid(row = 10, column = 1)
        
        btnshow = Button(data, text = "Show", height = 1, width = 10, font= "Arial 12 bold", command = show)
        btnshow.grid(row = 8, column = 2)
        
        btnsearch = Button(data, text = "Search", height = 1, width = 10, font= "Arial 12 bold", command = search)
        btnsearch.grid(row = 9, column = 2)
        
        btnexit = Button(data, text = "Exit", height = 1, width = 10, font= "Arial 12 bold", command = data.destroy)
        btnexit.grid(row = 10, column = 2)
        
#Text For Admin Window
        textrestodata = Label(data, text = "Resto Database", font="Arial 12 bold")
        textrestodata.grid(row = 0, column = 3, stick = W)
        
#Listbox for Data       
        list1=Listbox(data,height = 20, width = 85)
        list1.grid(row = 1,column = 4 , rowspan = 7, columnspan=2)
        scrl=Scrollbar(data)
        scrl.grid(row = 1,column = 3, sticky='ns',rowspan = 7)
        list1.configure(yscrollcommand = scrl.set)
        scrl.configure(command=list1.yview)
        list1.bind('<<ListboxSelect>>',get_selected_row)
       
    else:
#If the admin input wrong password
        tkinter.messagebox.showinfo("Input Invalid", "Wrong Admin Input")
    
#Window Buttons
btnuser = Button(user, text = "Find \n My Resto", height = 3, width = 10, font= "Arial 12 bold", command = userwindow)
btnuser.grid(row = 1, column = 1)

btnexit = Button(user, text = "Exit", height = 1, width = 10, font= "Arial 12 bold", command = exitwindow)
btnexit.grid(row = 2, column = 1)

btnadmin = Button(admin, text = "I'm Admin", height = 2, width = 10, font= "Arial 12 bold", command =adminwindow)
btnadmin.grid(row = 3, column = 1)

db.close()  #Close Connection database

window1.mainloop()      #make window constantly open
#end of the code