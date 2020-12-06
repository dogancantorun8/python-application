import tkinter as tk
import tkinter.filedialog
import tkinter.messagebox

class GUI:
    def __init__(self, master):
        master.title('Sample Messagebox')

        self.frame1 = tk.Frame(master)
        self.label_name = tk.Label(self.frame1, text='Adı Soyadı', width=10)
        self.label_name.pack(side='left')

        self.entry_name = tk.Entry(self.frame1)
        self.entry_name.pack(side='left')

        self.frame1.pack(side='top', anchor='w')

        self.frame2 = tk.Frame(master)
        self.label_no = tk.Label(self.frame2, text='No', width=10)
        self.label_no.pack(side='left')

        self.entry_no = tk.Entry(self.frame2)
        self.entry_no.pack(side='left')

        self.frame2.pack(side='top', anchor='w')

        self.frame3 = tk.Frame(master)

        self.button_cancel = tk.Button(self.frame3, text='Cancel', width=5)
        self.button_cancel.pack(side='right')

        self.button_ok = tk.Button(self.frame3, text='Ok', width=5)
        self.button_ok.pack(side='right')

        self.frame3.pack(side='top', anchor='w', fill='x')
        master.resizable(width=False, height=False)


root = tk.Tk()
gdb = GUI(root)
root.mainloop()