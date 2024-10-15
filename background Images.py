from tkinter import *
root=Tk()
root.geometry("700x500")
bg=PhotoImage(file="\\Users\\Jesh Matthew pc\\OneDrive\\Documents\\For code\\Works\\my new work\\Images\\Webber.png")
#show image using Label
label1=Label(root,image=bg)
label1.place(x=0,y=0)
label2=Label(root,text="Welcome to my image background setup",bg='powder blue',font=("Arial",15,"bold"),bd=10)
label2.pack(pady=50)
#create frame
frame1=Frame(root)
frame1.pack(pady=50)
#Add buttons
button1=Button(frame1,text="Exit",font=("Arial",20,"bold"),bg="green")
button1.pack(pady=20)
button2=Button(frame1,text="Start")
button2.pack(pady=20)
button3=Button(frame1,text="Reset")
button3.pack(pady=20)
root.mainloop()
