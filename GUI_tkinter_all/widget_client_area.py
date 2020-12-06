#bir widgetin tum clien area yı kaplamasını istersem
import tkinter as tk

class GUI:
    def __init__(self, master):
        master.title('Sample Messagebox')

        self.text = tk.Text(master, bg='white', font='Arial 20')
        self.text.pack(side='top', expand=True, fill='both')

root = tk.Tk()
gdb = GUI(root)
root.mainloop()
