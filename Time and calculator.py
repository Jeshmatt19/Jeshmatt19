from tkinter import *
import random
import time;

root=Tk()
root.geometry("1200x700+0+0")
root.title("time and date system")
text_Input=StringVar ()
operator=""

Tops=Frame(root,width=200,height=50,bg="green",relief=SUNKEN)
Tops.pack(side=TOP)

fl=Frame(root,width=300,height=700,bg="green",relief=SUNKEN)
fl.pack(side=LEFT)

f2=Frame(root,width=300,height=700,bg="green",relief=SUNKEN)
f2.pack(side=RIGHT)

#"===============================TIME=============================="
localtime=time.asctime (time.localtime (time.time ()))
#"============================INFO================================="
lblinfo=Label(Tops, font=('arial',50,'bold'),text="time Systems",
               fg="steel blue",bd=10,anchor='w')
lblinfo.grid (row=0,column=0)
lblDateTime=Label(Tops, font= ('arial',20,'bold'),text=localtime,
                   fg="green",
                   bg="green",bd=10,anchor='w')
lblDateTime.grid(row=1, column=0)
text_Input=StringVar ()
operator=""

txtdisplay =Entry(f2,font=('ariel',16,'bold'),textvariable=text_Input,
                  bd=5,insertwidth=5,
                  bg="green",justify='right')
txtdisplay.grid(columnspan=1)

def btnClick(numbers):
    global operator
    operator=operator+str(numbers)
    text_Input.set(operator)

def btnClearDisplay():
    global operator
    operator=""
    text_Input.set("")

def btnEqualsInput():
    global operator
    sumup=str(eval(operator))
    text_Input.set(sumup)
    operator=""

btn7=Button(f2,padx=16,pady=16,bd=8,fg="Black",font=('arial',20, 'bold'),
            text="7",
            bg="green",command=lambda:btnClick(7)).grid(row=2,column=0)

btn8=Button(f2, padx=16,pady=16,bd=8,fg="Black",
             font=('arial',20,'bold'),text="8",
            bg="green", command=lambda:btnClick(8)).grid(row=2,column=1)

btn9=Button(f2, padx=16,pady=16,bd=8,fg="Black",font=('arial'
                                                      ,20,'bold'),text="9",
bg="green",command=lambda:btnClick(9)).grid(row=2,column=2)

Addition=Button (f2, padx=16,pady=16,bd=8,fg="black",
                 font=('arial',20,'bold'),text="+",
                 bg="green",command=lambda:btnClick("+")).grid(row=2,column=3)
#------------------------------------------------------------------------------------------
btn4=Button(f2,padx=16,pady=16,bd=8,fg="Black",
            font=('arial',20,'bold'),text="4",
            bg="green",command=lambda:btnClick(4)).grid(row=3,column=0)

btn5=Button(f2,padx=16,pady=16,bd=8,fg="Black",
            font=('arial',20,'bold'),text="5",
            bg="green",command=lambda:btnClick(5)).grid(row=3,column=1)

btn6=Button(f2,padx=16,pady=16,bd=8,fg="Black",
            font=('arial',20,'bold'),text="6",
            bg="green",command=lambda:btnClick(6)).grid(row=3,column=2)

subtraction=Button(f2,padx=16,pady=16,bd=8,fg="Black",
                    font=('arial', 20,'bold'),text="-",
                    bg="green",command=lambda:btnClick("-")).grid(row=3,column=3)
#-------------------------------------------------------------------------------------------
btn4=Button(f2,padx=16,pady=16,bd=8,fg="Black",
            font=('arial',20,'bold'),text="1",
            bg="green",command=lambda:btnClick(1)).grid(row=4,column=0)

btn5=Button(f2,padx=16,pady=16,bd=8,fg="Black",
            font=('arial',20,'bold'),text="2",
            bg="green",command=lambda:btnClick(2)).grid(row=4,column=1)

btn6=Button(f2,padx=16,pady=16,bd=8,fg="Black",
            font=('arial',20,'bold'),text="3",
            bg="green",command=lambda:btnClick(3)).grid(row=4,column=2)

multiply=Button(f2,padx=16,pady=16,bd=8,fg="Black",
                    font=('arial', 20,'bold'),text="*",
                    bg="green",command=lambda:btnClick("*")).grid(row=4,column=3)
#---------------------------------------------------------------------------------------------
btn0=Button(f2,padx=16,pady=16,bd=8,fg="Black",
                font=('arial',20,'bold'),text="0",bg="green",
                command=lambda:btnClick(0)).grid(row=5,column=0)
btnClear=Button(f2,padx=16,pady=16,bd=8,fg="Black",
                font=('arial',20,'bold'),text="C",bg="green",
                command=btnClearDisplay).grid(row=5,column=1)
btnEqual=Button(f2, padx=16,pady=16,bd=8,fg="Black",
                font=('arial',20,'bold'),text="=",bg="green",
                command=btnEqualsInput).grid(row=5,column=2)
Division=Button(f2,padx=16,pady=16,bd=8,fg="Black",
                    font=('arial', 20,'bold'),text="/",
                    bg="green",command=lambda:btnClick("/")).grid(row=5,column=3)

root.mainloop ()
