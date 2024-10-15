from tkinter import *
root = Tk()
root.title('Checkbox')
Checkbox1=IntVar()
Check=Checkbutton(root,text="python",variable=Checkbox1,height=2,width=10)
Check.pack()
Checkbox2=IntVar()
Check=Checkbutton(root,text="Java",variable=Checkbox2,height=2,width=10)
Check.pack()
Checkbox3=IntVar()
Check=Checkbutton(root,text="C#",variable=Checkbox3,height=2,width=10)
Check.pack()
Checkbox4=IntVar()
Check=Checkbutton(root,text="SAS",variable=Checkbox4,height=2,width=10)
Check.pack()

root.mainloop()

