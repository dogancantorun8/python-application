import tkinter as tk

class GUI:
    def __init__(self, master):
        master.title('Sample Messagebox')

        self.button1 = tk.Button(master, text='1', width=10)
        self.button1.grid(row=0, column=0)

        self.button2 = tk.Button(master, text='2', width=10)
        self.button2.grid(row=0, column=1)

        self.button3 = tk.Button(master, text='3', width=10)
        self.button3.grid(row=0, column=2)

        self.button4 = tk.Button(master, text='4', width=10)
        self.button4.grid(row=1, column=0)

        self.button5 = tk.Button(master, text='5', width=10)
        self.button5.grid(row=1, column=1, columnspan=2, sticky='we')

root = tk.Tk()
gdb = GUI(root)
root.mainloop()
