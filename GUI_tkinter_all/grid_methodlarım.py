import tkinter as tk

class GUI:
    def __init__(self, master):
        master.title('Sample Messagebox')

        self.button1 = tk.Button(master, text='1', width=10)
        self.button1.grid(row=0, column=0, sticky='nswe')

        self.button2 = tk.Button(master, text='2', width=10)
        self.button2.grid(row=0, column=1,  sticky='nswe')

        self.button3 = tk.Button(master, text='3', width=10)
        self.button3.grid(row=0, column=2, sticky='nswe')

        self.button4 = tk.Button(master, text='4', width=10)
        self.button4.grid(row=1, column=0, sticky='nswe')

        self.button5 = tk.Button(master, text='5', width=10)
        self.button5.grid(row=1, column=1, sticky='nswe')

        self.button6 = tk.Button(master, text='6', width=10)
        self.button6.grid(row=1, column=2, sticky='nswe')

        self.button7 = tk.Button(master, text='7', width=10)
        self.button7.grid(row=2, column=0, sticky='nswe')

        self.button8 = tk.Button(master, text='8', width=10)
        self.button8.grid(row=2, column=1, sticky='nswe')

        self.button9 = tk.Button(master, text='9', width=10)
        self.button9.grid(row=2, column=2, sticky='nswe')

        master.columnconfigure(0, weight=1) #weight ile pencere buyunce componentlerde buyuyor
        master.columnconfigure(1, weight=1)
        master.columnconfigure(2, weight=1)

        master.rowconfigure(0, weight=1)
        master.rowconfigure(1, weight=1)
        master.rowconfigure(2, weight=1)

root = tk.Tk()
gdb = GUI(root)
root.mainloop()