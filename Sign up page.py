from tkinter import *
from tkinter import messagebox
ws = Tk()
ws.title ('Creating Sign-up form')
ws.geometry('250x300')
def selection():
    choice = var.get()
    if choice==1:
        m = 'Ms'
    elif choice ==2:
        m = 'Mr'
    elif choice==3:
           pass
    return m
def submit():
    name=name_Tf.get()
    m=selection()
    return messagebox.showinfo('python',f'[m] {name},submitted form')
def close():
    ws.destroy()
frame1=Label(ws)
frame1.pack()
frame2=LabelFrame(frame1,text='Gender' ,padx=30, pady=10)
var =IntVar()
Label(frame1, text  = 'FULL NAME').grid(row=0,column=0,padx=5,pady=5)
Label(frame1, text  = 'Email').grid(row=1,column=0,padx=5,pady=5)
Label(frame1, text  = 'Password').grid(row=2,column=0,padx=5,pady=5)
Radiobutton(frame2,text = 'Female', variable = var,value=1, command=selection).pack()
Radiobutton(frame2,text = 'Male', variable = var,value=2, command=selection).pack(anchor=W)
name_Tf=Entry (frame1)
name_Tf.grid(row=0,column=2)
Entry(frame1).grid(row=0,column=2)
Entry(frame1,show= '*').grid(row=2,column=2)
frame2.grid(row=3,columnspan=3,padx=30)
Button(frame1,text='submit',command = submit,padx=50,pady=5).grid(row=4,columnspan=4,pady=5)
Button(frame1,text="EXIT PROGRAM",font=('Times',14),command=close).grid(row=5,columnspan=5,pady=6)
ws.mainloop()
