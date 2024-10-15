from tkinter import *
from tkinter import messagebox

ws = Tk()
ws.title('Radiobutton')
ws.geometry('200x200')

def viewSelected():
    choice  = var.get()
    if choice == 1:
       output = "Male"

    elif choice == 2:
       output =  "Female"
    
    else:
        output = "Invalid selection"

    return messagebox.showinfo('Radiobutton', f'You Selected {output}.')
    
var = IntVar()
Radiobutton(ws, text="Male", variable=var, value=1, command=viewSelected).pack()
Radiobutton(ws, text="Female", variable=var, value=2, command=viewSelected).pack()

ws.mainloop()
