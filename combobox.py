from tkinter import *

ws = Tk()
ws.title('combo box')
ws.geometry('400x300')


def display_selected(choice):
    choice = variable.get()
    print(choice)

Universities = ['LASU','UNILAG', 'IMSU','FUTO','OOU','OAU','UNIBEN']

# setting variable for Integers
variable = StringVar()
variable.set(Universities[3])

# creating widget
dropdown = OptionMenu(
    ws,
    variable,
    *Universities,
    command=display_selected
)

# positioning widget
dropdown.pack(expand=True)

# infinite loop 
ws.mainloop()
