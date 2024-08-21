#start of the code
from tkinter import *           #import tkinter libraries 
from tkinter import filedialog  #import tkinter filedialog
import tkinter.messagebox       #import tkinter messagebox

#Saving File
def save_file():
    textsave=str(text.get(0.0,END))
    f = filedialog.asksaveasfile(mode='w', title = "Select file",filetypes = (("txt files","*.txt"),("all files","*.*")),
                                 defaultextension=".txt")
    if f is None:
        return

    f.write(textsave)
    f.close()
    text.delete(1.0,END)
    
    tkinter.messagebox.showinfo("Save File Success", "Success to save your File") 

#Opening Path File
def open_file():
    text.delete(1.0,END)
    filename =  filedialog.askopenfilename(initialdir = "/",title = "Select file",filetypes = (("txt files","*.txt"),("all files","*.*")))
    text.insert(1.0,filename)
    
    tkinter.messagebox.showinfo("Open File Success", "The link is in the textbox") 
    
root = Tk() #open window
root.title("Editor")               #window title
root.resizable (width=False, height = False)    #fixed size of the window

#Window Size
root.geometry("1080x800")

#Window Title
title = Label(root, text = "Editor", font="Arial 20 bold")
title.grid(row = 0, column = 1)

#Row and Column Spacing
column = Label(root, width = 5)
column.grid(row = 1, column = 0)
row = Label(root)
row.grid(row = 3, column = 0)

#Text
text = Text(root)
text.grid(row =2, column = 1)

scrldata=Scrollbar(root)
scrldata.grid(row = 2,column = 0, sticky='ns',rowspan = 1)
text.configure(yscrollcommand = scrldata.set)
scrldata.configure(command=text.yview)

#Buttons for Window1
btnsave = Button(root, text= "Save as", height = 2, width = 10, command = save_file)
btnsave.grid(row = 4, column = 1)

btnsave = Button(root, text= "Open", height = 2, width = 10, command = open_file)
btnsave.grid(row = 5, column = 1)

root.mainloop()
#end of the code