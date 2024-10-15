import tkinter as tk

class ATM:
    def __init__(self, master):
        self.master = master
        master.title("ATM Machine")

        self.label = tk.Label(master, text="Welcome to the ATM Machine!")
        self.label.pack()

        self.withdraw_button = tk.Button(master, text="Withdraw", command=self.withdraw)
        self.withdraw_button.pack()

        self.balance_button = tk.Button(master, text="Balance", command=self.balance)
        self.balance_button.pack()

        self.quit_button = tk.Button(master, text="Quit", command=master.quit)
        self.quit_button.pack()

    def withdraw(self):
        print("Withdraw")

    def balance(self):
        print("Balance")

root = tk.Tk()
my_gui = ATM(root)
root.mainloop()