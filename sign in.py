from tkinter import *
ws = Tk()
ws.geometry("700x500")
bg=PhotoImage(file="\\Users\\Jesh Matthew pc\\OneDrive\\Documents\\For code\\Works\\my new work\\Images\\Webber.png")
#show image using Label
label1=Label(ws,image=bg)
label1.place(x=0,y=0)
ws.title('PythonGuides')
ws.config(bg='#0B5A81')

f = ('Times', 14)
var = StringVar()
var.set('male')

right_frame = Frame(
    ws, 
    bd=2, 
    bg='#CCCCCC',
    relief=SOLID, 
    padx=10, 
    pady=10
    )


Label(
    right_frame, 
    text="Email", 
    bg='#CCCCCC',
    font=f
    ).grid(row=1, column=0, sticky=W, pady=10)

Label(
    right_frame, 
    text="Password", 
    bg='#CCCCCC',
    font=f
    ).grid(row=5, column=0, sticky=W, pady=10)

register_email = Entry(
    right_frame, 
    font=f
    )

register_pwd = Entry(
    right_frame, 
    font=f,
    show='*'
)

register_btn = Button(
    right_frame, 
    width=15, 
    text='Sign-In', 
    font=f, 
    relief=SOLID,
    cursor='hand2',
    command=None
)


register_email.grid(row=1, column=1, pady=10, padx=20) 
register_pwd.grid(row=5, column=1, pady=10, padx=20)
register_btn.grid(row=7, column=1, pady=10, padx=20)
right_frame.pack()


ws.mainloop()
import sqlite3
connection=sqlite3.connect("Form.db")
crsr=connection.cursor()
crsr.execute("SELECT * From Student")
ans=crsr.fetchall()
for i in ans:
    print(i)
