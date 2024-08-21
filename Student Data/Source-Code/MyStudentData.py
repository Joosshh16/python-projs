#start of the code
from tkinter import *           #import tkinter libraries       
import tkinter.messagebox       #import tkinter messagebox
import sqlite3                  #import sqlite3

db = sqlite3.connect('StudentData.db')  #Create and Connect Database
cursor = db.cursor() #Create Cursor to Database
#Create Table for Database
cursor.execute("CREATE TABLE IF NOT EXISTS studsched_tbl(studnum TEXT, studname TEXT, studsched TEXT, studsubject TEXT, studteacher TEXT)")
cursor.execute("CREATE TABLE IF NOT EXISTS studact_tbl(studnum TEXT, studname TEXT, studsubject TEXT, studteacher TEXT, studstatus TEXT)")
db.commit() #Commit for Database

window1 = Tk()                     #open window
window1.title("Student Data")               #window title
window1.resizable (width=False, height = False)    #fixed size of the window

#Window Size
window1.geometry("400x430")

#Window Title
title = Label(window1, text = "My Student Data", font="Arial 30 bold")
title.grid(row = 0, column = 1)

#Row and Column Spacing For Window1
column = Label(window1, width = 5)
column.grid(row = 0, column = 0)
row = Label(window1)
row.grid(row = 1, column = 0)
row2 = Label(window1)
row2.grid(row = 3, column = 0)
row3 = Label(window1)
row3.grid(row = 5, column = 0)
row4 = Label(window1)
row4.grid(row = 7, column = 0)
row5 = Label(window1)
row5.grid(row = 9, column = 0)

#View Student Schedule
def viewstudsched():
    viewsched = Tk()                     #open window
    viewsched.title("Student Data")               #window title
    viewsched.resizable (width = False, height = False)    #fixed size of the window

#Window Size of View Student Schedule Window 
    viewsched.geometry("950x390")
            
#Row and Column Spacing For Student Schedule Window
    row = Label(viewsched, width = 5)
    row.grid(row = 0, column = 0)
    
#Data Status For View Student Schedule Window 
    titleschedres = Label(viewsched, width = 15, text = "Data Status", font="Arial 12 bold")
    titleschedres.grid(row = 1, column = 2, stick = W)
    
#Text Label For View Student Schedule Window 
    textstudnum = Label(viewsched, text = "Student Number:", width = 14, font="Arial 12 bold")
    textstudnum.grid(row = 2, column = 1, stick = E)
    
    textstudname = Label(viewsched, text = "Student Name:", width = 14, font="Arial 12 bold")
    textstudname.grid(row = 3, column = 1, stick = E)
    
#Field Entry For View Student Schedule Window 
    fieldstudnum = Entry(viewsched, font="Arial 12 bold", width = 10)
    fieldstudnum.grid(row = 2, column = 2)
    
    fieldstudname = Entry(viewsched, font="Arial 12 bold", width = 10)
    fieldstudname.grid(row = 3, column = 2)
    
#Search Student Schedule
    def seacrhsched():
        try:
            snum = int(fieldstudnum.get())
            sname = str(fieldstudname.get()) 

            conn = sqlite3.connect('StudentData.db')
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM studsched_tbl WHERE studnum=? OR studname=?",
                                   (snum, sname))
                    
            data = cursor.fetchall()
                    
            listsched.delete(0,END)
            for row in data:
                listsched.insert(END,(row))
                    
            conn.close()
            titleschedres.configure(text = "Search Result")
        except:
            titleschedres.configure(text = "Wrong Data Input")
            
#Buttons For View Student Schedule Window 
    btnsearchsched = Button(viewsched, text ="Search", height = 2, width = 10, font="Arial 10 bold", command = seacrhsched)
    btnsearchsched.grid(row = 4, column = 2)
    
    btnschedexit = Button(viewsched, text ="Exit", height = 2, width = 10, font="Arial 10 bold", command = viewsched.destroy)
    btnschedexit.grid(row = 4, column = 1)
    
#Text for Student Schedule Data Result
    textstuddata2 = Label(viewsched, text = "My Student \nSchedule", width = 10, font="Arial 12 bold")
    textstuddata2.grid(row = 0, column = 4, stick = E)
    
#Listbox for Student Schedule Data Result
    listsched=Listbox(viewsched, height = 20, width = 90)
    listsched.grid(row = 1,column = 4, rowspan = 7, columnspan=2)     
    scrlsched=Scrollbar(viewsched)
    scrlsched.grid(row = 1,column = 3, sticky='ns',rowspan = 7)    
    listsched.configure(yscrollcommand = scrlsched.set)
    scrlsched.configure(command=listsched.yview)

#View Student Activity
def viewstudact():
    viewsact = Tk()                     #open window
    viewsact.title("Student Data")               #window title
    viewsact.resizable (width = False, height = False)    #fixed size of the window

#Window Size of View Student Activity Window 
    viewsact.geometry("950x390")
            
#Row and Column Spacing For Student Activity Window
    row = Label(viewsact, width = 5)
    row.grid(row = 0, column = 0)
    
#Data Status For View Student Activity Window 
    titleschedres = Label(viewsact, width = 15, text = "Data Status", font="Arial 12 bold")
    titleschedres.grid(row = 1, column = 2, stick = W)
    
#Text Label For View Student Activity Window 
    textstudnum = Label(viewsact, text = "Student Number:", width = 14, font="Arial 12 bold")
    textstudnum.grid(row = 2, column = 1, stick = E)
    
    textstudname = Label(viewsact, text = "Student Name:", width = 14, font="Arial 12 bold")
    textstudname.grid(row = 3, column = 1, stick = E)
    
#Field Entry For View Student Activity Window 
    fieldstudnum = Entry(viewsact, font="Arial 12 bold", width = 10)
    fieldstudnum.grid(row = 2, column = 2)
    
    fieldstudname = Entry(viewsact, font="Arial 12 bold", width = 10)
    fieldstudname.grid(row = 3, column = 2)
    
#Search Student Activity
    def seacrhstudact():
        try:
            snum = int(fieldstudnum.get())
            sname = str(fieldstudname.get()) 

            conn = sqlite3.connect('StudentData.db')
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM studact_tbl WHERE studnum=? OR studname=?",
                                   (snum, sname))
                    
            data = cursor.fetchall()
                    
            listact.delete(0,END)
            for row in data:
                listact.insert(END,(row))
                    
            conn.close()
            titleschedres.configure(text = "Search Result")
        except:
            titleschedres.configure(text = "Wrong Data Input")
            
#Buttons For View Student Activity Window 
    btnsearchsched = Button(viewsact, text ="Search", height = 2, width = 10, font="Arial 10 bold", command = seacrhstudact)
    btnsearchsched.grid(row = 4, column = 2)
    
    btnactexit = Button(viewsact, text ="Exit", height = 2, width = 10, font="Arial 10 bold", command = viewsact.destroy)
    btnactexit.grid(row = 4, column = 1)
    
#Text for Student Activity Data Result
    textstuddata2 = Label(viewsact, text = "My Student \nActivities", width = 10, font="Arial 12 bold")
    textstuddata2.grid(row = 0, column = 4, stick = E)
    
#Listbox for Student Activity Data Result
    listact=Listbox(viewsact, height = 20, width = 90)
    listact.grid(row = 1,column = 4, rowspan = 7, columnspan=2)     
    scrlact=Scrollbar(viewsact)
    scrlact.grid(row = 1,column = 3, sticky='ns',rowspan = 7)    
    listact.configure(yscrollcommand = scrlact.set)
    scrlact.configure(command=listact.yview)
    
#Admin Confirm Login Window
def adminconfirm():
    adminconfirm = Tk()                     #open window
    adminconfirm.title("Student Data")               #window title
    adminconfirm.resizable (width = False, height = False)    #fixed size of the window
    
#Window Size For Admin Confirm Window
    adminconfirm.geometry("300x400")

#Row and Column Spacing For Admin Confirm Window
    row = Label(adminconfirm, width = 3)
    row.grid(row = 0, column = 0)
    row2 = Label(adminconfirm, width = 3)
    row2.grid(row = 1, column = 0)
    row3 = Label(adminconfirm, width = 3)
    row3.grid(row = 5, column = 0)
    row4 = Label(adminconfirm, width = 3)
    row4.grid(row = 8, column = 0)
    
#Window Title For Admin Confirm Window
    texttitle = Label(adminconfirm, text = "Admin Login", font="Arial 30 bold")
    texttitle.grid(row = 0, column = 1)
    
    textstatus = Label(adminconfirm, text = "Manage Student Data", font="Arial 10 bold")
    textstatus.grid(row = 4, column = 1)
    
#Text For Admin Confirm Window
    textadmin = Label(adminconfirm, text = "Admin Password: ", width = 15, font="Arial 12 bold")
    textadmin.grid(row = 2, column = 1)
    
#Field Entry For Admin Confirm Window
    fieldadmin = Entry(adminconfirm, show = "*", font="Arial 12 bold", width = 10)
    fieldadmin.grid(row = 3, column = 1)

#Student Schedule Window    
    def studentsched():
        adminpass = str(fieldadmin.get())
        
        if (adminpass == "admin"):
            adminconfirm.destroy()
            studsched = Tk()                     #open window
            studsched.title("Student Data")               #window title
            studsched.resizable (width = False, height = False)    #fixed size of the window

#Window Size of Student Schedule Window 
            studsched.geometry("950x520")
            
#Row and Column Spacing For Student Schedule Window
            row = Label(studsched, width = 5)
            row.grid(row = 0, column = 0)
            row2 = Label(studsched, width = 5)
            row2.grid(row = 7, column = 0)
                
#Data Status For Student Schedule Window 
            titleadmindata1 = Label(studsched, width = 15, text = "Data Status", font="Arial 12 bold")
            titleadmindata1.grid(row = 1, column = 2, stick = W)
        
#Text Label For Student Schedule Window 
            textstudnum = Label(studsched, text = "Student Number:", width = 14, font="Arial 12 bold")
            textstudnum.grid(row = 2, column = 1, stick = E)
            
            textstudname = Label(studsched, text = "Student Name:", width = 12, font="Arial 12 bold")
            textstudname.grid(row = 3, column = 1, stick = E)
            
            textstudsched = Label(studsched, text = "Schedule:", width = 10, font="Arial 12 bold")
            textstudsched.grid(row = 4, column = 1, stick = E)
            
            textstudsubject = Label(studsched, text = "Subject:", width = 10, font="Arial 12 bold")
            textstudsubject.grid(row = 5, column = 1, stick = E)
            
            textstudteacher = Label(studsched, text = "Teacher:", width = 10, font="Arial 12 bold")
            textstudteacher.grid(row = 6, column = 1, stick = E)
            
#Field Entry For Student Schedule Window 
            fieldstudnum = Entry(studsched, font="Arial 12 bold", width = 10)
            fieldstudnum.grid(row = 2, column = 2)
            
            fieldstudname = Entry(studsched, font="Arial 12 bold", width = 10)
            fieldstudname.grid(row = 3, column = 2)
            
            fieldstudsched = Entry(studsched, font="Arial 12 bold", width = 10)
            fieldstudsched.grid(row = 4, column = 2)
            
            fieldstudsubject = Entry(studsched, font="Arial 12 bold", width = 10)
            fieldstudsubject.grid(row = 5, column = 2)
            
            fieldstudteacher = Entry(studsched, font="Arial 12 bold", width = 10)
            fieldstudteacher.grid(row = 6, column = 2)
            
#Selecting Data of Student Schedule Window 
            def get_selected_row1(event):
                global selected_data1
                index=list1.curselection()
                selected_data1=list1.get(index)
                fieldstudnum.delete(0,END)
                fieldstudnum.insert(END,selected_data1[0])
                
                fieldstudname.delete(0,END)
                fieldstudname.insert(END,selected_data1[1])
                
                fieldstudsched.delete(0,END)
                fieldstudsched.insert(END,selected_data1[2])
                
                fieldstudsubject.delete(0,END)
                fieldstudsubject.insert(END,selected_data1[3])
                
                fieldstudteacher.delete(0,END)
                fieldstudteacher.insert(END,selected_data1[4])
                
#Searhing Data of Student Schedule Window 
            def search1():
                try:
                    snum = int(fieldstudnum.get())
                    sname = str(fieldstudname.get())
                    ssched = str(fieldstudsched.get())
                    ssubject = str(fieldstudsubject.get())
                    steacher = str(fieldstudteacher.get())    
                    
                    conn = sqlite3.connect('StudentData.db')
                    cursor = conn.cursor()
                    cursor.execute("SELECT * FROM studsched_tbl WHERE studnum=? OR studname=? OR studsched=?  OR  studsubject=?  OR  studteacher=?",
                                   (snum, sname, ssched, ssubject, steacher))
                    
                    data = cursor.fetchall()
                    
                    list1.delete(0,END)
                    for row in data:
                        list1.insert(END,(row))
                    
                    conn.close()
                    titleadmindata1.configure(text = "Search Result")
                except:
                    titleadmindata1.configure(text = "Wrong Data Input")
            
#Viewing Data of Student Schedule Window              
            def view1():
                conn = sqlite3.connect('StudentData.db')
                cursor = conn.cursor()
                cursor.execute('SELECT * FROM studsched_tbl')
                data = cursor.fetchall()
                list1.delete(0,END)
                
                for datas in data:
                    list1.insert(END,datas)
                    
                conn.close()
                titleadmindata1.configure(text = "Data Status")
            
#Inserting Data For Student Schedule Window   
            def insert1():
                try:
                    snum = int(fieldstudnum.get())
                    sname = str(fieldstudname.get())
                    ssched = str(fieldstudsched.get())
                    ssubject = str(fieldstudsubject.get())
                    steacher = str(fieldstudteacher.get())
                    
                    conn = sqlite3.connect('StudentData.db')
                    
                    with conn:
                        cursor = conn.cursor()
                        cursor.execute('INSERT INTO studsched_tbl(studnum, studname, studsched, studsubject, studteacher) VALUES(?,?,?,?,?)',
                                       (snum, sname, ssched, ssubject, steacher))
                        db.close()
                        
                    fieldstudnum.delete(0, 'end')
                    fieldstudname.delete(0, 'end')
                    fieldstudsched.delete(0, 'end')
                    fieldstudsubject.delete(0, 'end')
                    fieldstudteacher.delete(0, 'end')
                    
                    conn.close()
                        
                    titleadmindata1.configure(text = "Data Inserted")
            
                    list1.delete(0,END)
                    list1.insert(END,(snum,sname,ssched,ssubject,steacher))
                except:
                    titleadmindata1.configure(text = "Wrong Data Input")
                    
#Updating Data for Student Schedule Window 
            def update1():
                try:
                    snum = int(fieldstudnum.get())
                    sname = str(fieldstudname.get())
                    ssched = str(fieldstudsched.get())
                    ssubject = str(fieldstudsubject.get())
                    steacher = str(fieldstudteacher.get())
          
                    conn = sqlite3.connect('StudentData.db')
                    cursor = conn.cursor()
                    cursor.execute("UPDATE studsched_tbl SET studname = ?, studsched =?, studsubject =?, studteacher = ?  WHERE studnum = ?",
                                   (sname, ssched, ssubject, steacher, snum))
                    conn.commit()
                    
                    fieldstudnum.delete(0, 'end')
                    fieldstudname.delete(0, 'end')
                    fieldstudsched.delete(0, 'end')
                    fieldstudsubject.delete(0, 'end')
                    fieldstudteacher.delete(0, 'end')
                    
                    conn.close()
                    titleadmindata1.configure(text = "Data Updated")
                except:
                    titleadmindata1.configure(text = "Wrong Data Input")
                    
#Deleting Data For Student Schedule Window 
            def delete1():
                try:
                    delet = int(fieldstudnum.get())
                    conn = sqlite3.connect('StudentData.db')
                    cursor = conn.cursor()
                    cursor.execute("DELETE FROM studsched_tbl WHERE studnum = ?",(delet,))
                    conn.commit()
                    
                    fieldstudnum.delete(0, 'end')
                    fieldstudname.delete(0, 'end')
                    fieldstudsched.delete(0, 'end')
                    fieldstudsubject.delete(0, 'end')
                    fieldstudteacher.delete(0, 'end')
                    
                    conn.close()
                    titleadmindata1.configure(text = "Data Deleted")
                except:
                    titleadmindata1.configure(text = "Wrong Data Input")
            
#Buttons for Student Schedule Window 
            btninsert1 = Button(studsched, text ="Insert", height = 2, width = 10, font="Arial 10 bold", command = insert1)
            btninsert1.grid(row = 8, column = 1)
            
            btnupdate1 = Button(studsched, text ="Update", height = 2, width = 10, font="Arial 10 bold", command = update1)
            btnupdate1.grid(row = 9, column = 1)
            
            btndelete1 = Button(studsched, text ="Delete", height = 2, width = 10, font="Arial 10 bold", command = delete1)
            btndelete1.grid(row = 10, column = 1)
            
            btnview1 = Button(studsched, text ="View", height = 2, width = 10, font="Arial 10 bold", command = view1)
            btnview1.grid(row = 8, column = 2)
            
            btnsearch1 = Button(studsched, text ="Search", height = 2, width = 10, font="Arial 10 bold", command = search1)
            btnsearch1.grid(row = 9, column = 2)
            
            btnexit1 = Button(studsched, text ="Exit", height = 2, width = 10, font="Arial 10 bold", command = studsched.destroy)
            btnexit1.grid(row = 10, column = 2)
    
            textstuddata1 = Label(studsched, text = "Student \nSchedule", width = 10, font="Arial 12 bold")
            textstuddata1.grid(row = 0, column = 4, stick = E)
        
#Listbox for Student Schedule Data Result
            list1=Listbox(studsched, height = 20, width = 90)
            list1.grid(row = 1,column = 4, rowspan = 7, columnspan=2)     
            scrl1=Scrollbar(studsched)
            scrl1.grid(row = 1,column = 3, sticky='ns',rowspan = 7)    
            list1.configure(yscrollcommand = scrl1.set)
            scrl1.configure(command=list1.yview)
            list1.bind('<<ListboxSelect>>',get_selected_row1)
        else:
#When the user input wrong password
            textstatus.configure(text = "Wrong Pass")

#Student Activity Window    
    def studentactivity():
        adminpass = str(fieldadmin.get())
        
        if (adminpass == "admin"):
            adminconfirm.destroy()
            studact = Tk()                     #open window
            studact.title("Student Data")               #window title
            studact.resizable (width = False, height = False)    #fixed size of the window

#Window Size of Student Activity Window 
            studact.geometry("950x520")
            
#Row and Column Spacing For Student Activity Window
            row = Label(studact, width = 5)
            row.grid(row = 0, column = 0)
            row2 = Label(studact, width = 5)
            row2.grid(row = 7, column = 0)
            
#Data Status For Student Activity Window 
            titleadmindata2 = Label(studact, width = 15, text = "Data Status", font="Arial 12 bold")
            titleadmindata2.grid(row = 1, column = 2, stick = W)
            
#Text Label For Student Activity Window 
            textstudnum1 = Label(studact, text = "Student Number:", width = 14, font="Arial 12 bold")
            textstudnum1.grid(row = 2, column = 1, stick = E)
            
            textstudname1 = Label(studact, text = "Student Name:", width = 12, font="Arial 12 bold")
            textstudname1.grid(row = 3, column = 1, stick = E)
            
            textstudsubject1 = Label(studact, text = "Subject:", width = 10, font="Arial 12 bold")
            textstudsubject1.grid(row = 4, column = 1, stick = E)
            
            textstudteacher1 = Label(studact, text = "Teacher:", width = 10, font="Arial 12 bold")
            textstudteacher1.grid(row = 5, column = 1, stick = E)
            
            textstatus1 = Label(studact, text = "Status:", width = 10, font="Arial 12 bold")
            textstatus1.grid(row = 6, column = 1, stick = E)
            
#Field Entry For Student Activity Window 
            fieldstudnum1 = Entry(studact, font="Arial 12 bold", width = 10)
            fieldstudnum1.grid(row = 2, column = 2)
            
            fieldstudname1 = Entry(studact, font="Arial 12 bold", width = 10)
            fieldstudname1.grid(row = 3, column = 2)
            
            fieldstudsubject1 = Entry(studact, font="Arial 12 bold", width = 10)
            fieldstudsubject1.grid(row = 4, column = 2)
            
            fieldstudteacher1 = Entry(studact, font="Arial 12 bold", width = 10)
            fieldstudteacher1.grid(row = 5, column = 2)
            
            fieldstatus1 = Entry(studact, font="Arial 12 bold", width = 10)
            fieldstatus1.grid(row = 6, column = 2)
            
#Selecting Data of Student Activity Window 
            def get_selected_row2(event):
                global selected_data2
                index=list2.curselection()
                selected_data2=list2.get(index)
                fieldstudnum1.delete(0,END)
                fieldstudnum1.insert(END,selected_data2[0])
                
                fieldstudname1.delete(0,END)
                fieldstudname1.insert(END,selected_data2[1])
                
                fieldstudsubject1.delete(0,END)
                fieldstudsubject1.insert(END,selected_data2[2])
                
                fieldstudteacher1.delete(0,END)
                fieldstudteacher1.insert(END,selected_data2[3])
                
                fieldstatus1.delete(0,END)
                fieldstatus1.insert(END,selected_data2[4])
                
#Searhing Data of Student Activity Window 
            def search2():
                try:
                    snum1 = int(fieldstudnum1.get())
                    sname1 = str(fieldstudname1.get())
                    ssubject1 = str(fieldstudsubject1.get())
                    steacher1 = str(fieldstudteacher1.get())
                    sstatus1 = str(fieldstatus1.get())    
                    
                    conn = sqlite3.connect('StudentData.db')
                    cursor = conn.cursor()
                    cursor.execute("SELECT * FROM studact_tbl WHERE studnum=? OR studname=? OR studsubject=?  OR  studteacher=?  OR  studstatus=?",
                                   (snum1, sname1, ssubject1, steacher1, sstatus1))
                    
                    data = cursor.fetchall()
                    
                    list2.delete(0,END)
                    for row in data:
                        list2.insert(END,(row))
                    
                    conn.close()
                    titleadmindata2.configure(text = "Search Result")
                except:
                    titleadmindata2.configure(text = "Wrong Data Input")
                
#Viewing Data of Student Activity Window              
            def view2():
                conn = sqlite3.connect('StudentData.db')
                cursor = conn.cursor()
                cursor.execute('SELECT * FROM studact_tbl')
                data = cursor.fetchall()
                list2.delete(0,END)
                
                for datas in data:
                    list2.insert(END,datas)
                    
                conn.close()
                titleadmindata2.configure(text = "Data Status")
                
#Inserting Data For Student Activity Window   
            def insert2():
                try:
                    snum1 = int(fieldstudnum1.get())
                    sname1 = str(fieldstudname1.get())
                    ssubject1 = str(fieldstudsubject1.get())
                    steacher1 = str(fieldstudteacher1.get())
                    sstatus1 = str(fieldstatus1.get())
                    
                    conn = sqlite3.connect('StudentData.db')
                    
                    with conn:
                        cursor = conn.cursor()
                        cursor.execute('INSERT INTO studact_tbl(studnum, studname, studsubject, studteacher, studstatus) VALUES(?,?,?,?,?)',
                                       (snum1, sname1, ssubject1, steacher1, sstatus1))
                        db.close()
                        
                    fieldstudnum1.delete(0, 'end')
                    fieldstudname1.delete(0, 'end')
                    fieldstudsubject1.delete(0, 'end')
                    fieldstudteacher1.delete(0, 'end')
                    fieldstatus1.delete(0, 'end')
                    
                    conn.close()
                        
                    titleadmindata2.configure(text = "Data Inserted")
            
                    list2.delete(0,END)
                    list2.insert(END,(snum1,sname1,ssubject1,steacher1,sstatus1))
                except:
                    titleadmindata2.configure(text = "Wrong Data Input")
                    
#Updating Data for Student Activity Window 
            def update2():
                try:
                    snum1 = int(fieldstudnum1.get())
                    sname1 = str(fieldstudname1.get())
                    ssubject1 = str(fieldstudsubject1.get())
                    steacher1 = str(fieldstudteacher1.get())
                    sstatus1 = str(fieldstatus1.get())
          
                    conn = sqlite3.connect('StudentData.db')
                    cursor = conn.cursor()
                    cursor.execute("UPDATE studact_tbl SET studname = ?, studsubject =?, studteacher =?, studstatus = ?  WHERE studnum = ?",
                                   (sname1, ssubject1, steacher1, sstatus1, snum1))
                    conn.commit()
                    
                    fieldstudnum1.delete(0, 'end')
                    fieldstudname1.delete(0, 'end')
                    fieldstudsubject1.delete(0, 'end')
                    fieldstudteacher1.delete(0, 'end')
                    fieldstatus1.delete(0, 'end')
                    
                    conn.close()
                    titleadmindata2.configure(text = "Data Updated")
                except:
                    titleadmindata2.configure(text = "Wrong Data Input")
                    
#Deleting Data For Student Activity Window 
            def delete2():
                try:
                    delet = int(fieldstudnum1.get())
                    conn = sqlite3.connect('StudentData.db')
                    cursor = conn.cursor()
                    cursor.execute("DELETE FROM studact_tbl WHERE studnum = ?",(delet,))
                    conn.commit()
                    
                    fieldstudnum1.delete(0, 'end')
                    fieldstudname1.delete(0, 'end')
                    fieldstudsubject1.delete(0, 'end')
                    fieldstudteacher1.delete(0, 'end')
                    fieldstatus1.delete(0, 'end')
                    
                    conn.close()
                    titleadmindata2.configure(text = "Data Deleted")
                except:
                    titleadmindata2.configure(text = "Wrong Data Input")
                
#Buttons for Student Activities Window 
            btninsert2 = Button(studact, text ="Insert", height = 2, width = 10, font="Arial 10 bold", command = insert2)
            btninsert2.grid(row = 8, column = 1)
            
            btnupdate2 = Button(studact, text ="Update", height = 2, width = 10, font="Arial 10 bold", command = update2)
            btnupdate2.grid(row = 9, column = 1)
            
            btndelete2 = Button(studact, text ="Delete", height = 2, width = 10, font="Arial 10 bold", command = delete2)
            btndelete2.grid(row = 10, column = 1)
            
            btnview2 = Button(studact, text ="View", height = 2, width = 10, font="Arial 10 bold", command = view2)
            btnview2.grid(row = 8, column = 2)
            
            btnsearch2 = Button(studact, text ="Search", height = 2, width = 10, font="Arial 10 bold", command = search2)
            btnsearch2.grid(row = 9, column = 2)
            
            btnexit2 = Button(studact, text ="Exit", height = 2, width = 10, font="Arial 10 bold", command = studact.destroy)
            btnexit2.grid(row = 10, column = 2)  
                
            textstuddata2 = Label(studact, text = "Student \nActivities", width = 10, font="Arial 12 bold")
            textstuddata2.grid(row = 0, column = 4, stick = E)
            
#Listbox for Student Activity Data Result
            list2=Listbox(studact, height = 20, width = 90)
            list2.grid(row = 1,column = 4, rowspan = 7, columnspan=2)     
            scrl2=Scrollbar(studact)
            scrl2.grid(row = 1,column = 3, sticky='ns',rowspan = 7)    
            list2.configure(yscrollcommand = scrl2.set)
            scrl2.configure(command=list2.yview)
            list2.bind('<<ListboxSelect>>',get_selected_row2)
            
        else:
#When the user input wrong password
            textstatus.configure(text = "Wrong Pass")
        
#Buttons For Admin Confirm Window
    btnloginsched = Button(adminconfirm, text ="Student \nSchedule", height = 3, width = 10, font="Arial 10 bold", command = studentsched)
    btnloginsched.grid(row = 6, column = 1)
    
    btnloginact = Button(adminconfirm, text ="Student \n Activities", height = 3, width = 10, font="Arial 10 bold", command = studentactivity)
    btnloginact.grid(row = 7, column = 1)
    
    btnexit = Button(adminconfirm, text ="Exit", height = 1, width = 10, font="Arial 10 bold", command = adminconfirm.destroy)
    btnexit.grid(row = 9, column = 1)

#Text Line for Window1
textline = Label(window1, text ="_______________________", width = 20, font="Arial 15 bold")
textline.grid(row = 6, column = 1)

#Buttons For Window1
btnstudentsched= Button(window1, text ="My \nStudent \nSchedule", height = 3, width = 12, font="Arial 10 bold", command = viewstudsched)
btnstudentsched.grid(row = 2, column = 1)

btnstudentact = Button(window1, text ="My \nStudent \nActivity", height = 3, width = 12, font="Arial 10 bold", command = viewstudact)
btnstudentact.grid(row = 4, column = 1)

btnadmin = Button(window1, text ="Admin", height = 3, width = 12, font="Arial 10 bold", command = adminconfirm)
btnadmin.grid(row = 8, column = 1)

btnexit = Button(window1, text ="Exit", height = 2, width = 12, font="Arial 10 bold", command = window1.destroy)
btnexit.grid(row = 10, column = 1)

window1.mainloop()      #make window constantly open