from tkinter import *
root=Tk()
btn=Button(root,text="click me",bd='5',command=root.destroy)
btn.pack(side="Top")
root.mainloop()
