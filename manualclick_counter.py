import time
from tkinter import * # Import tkinter modul

root = Tk() # Initialize the Tkinter Window

root.geometry("172x115+1650+37") 
root.resizable(False,False)
root.configure(background="black")
root.overrideredirect(1) # Remove the window status top bar  

p=-1
s=0
res=0

def click(): # Function to add 1st and 2nd digits
    global p,s,res
    if res==0:
        p=p+1
        if p==10:
            p=0
            s=s+1
    else:
        p=0
        s=0
        res=0

    #Print the numbers in the window screen
    label1=Label(root,font=("alarm clock",60,"bold"),text='%i%i'%(s,p), bd=0,bg='black', fg="red", padx=0, pady=0)
    label1.grid(row=2,column=1, columnspan=2, ipadx=15, ipady=4)

def rs(): # Function to put both digits in 0
    global res
    res=1
    click()

#Print the buttons in the windown screen with the respective function command
button1=Button(root,text="Click",command=click, width=7,borderwidth=2)
button1.grid(row=1,column=1,sticky='W',pady=0)
button2=Button(root,text="Reset",command=rs, width=7,borderwidth=2)
button2.grid(row=1,column=2,sticky='W')

click()

root.mainloop()