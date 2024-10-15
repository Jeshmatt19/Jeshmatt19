from tkinter import *
from tkinter.ttk import Combobox

ws = Tk()
ws.title("Python Guides")
ws.geometry("200x200")


def search_items():
    search_value = variable.get()
    if search_value == "" or search_value == " ":
        combo['values'] = item_names
    else:
        value_to_display = []
        for value in item_names:
            if search_value in value:
                value_to_display.append(value)
        combo['values'] = value_to_display


item_names = list([str(a) for _ in range(100) for a in range(10)])

combo = Combobox(ws, state='readonly')
combo['values'] = item_names
combo.pack()

variable=StringVar()
entry1 = Entry(ws, textvariable=variable)
entry1.pack()

button = Button(ws, text="search", command=search_items)
button.pack()

ws.mainloop()