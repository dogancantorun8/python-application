import tkinter as tk

#burada main frame üzerine ikinci bir frame yaratıp componentlerimi ikinci yarattığım frame üzerinde gruplandırıyorum
class GUI:
    def __init__(self, master):
        self.master = master
        master.geometry('800x600')
        self.frame = tk.Frame(master, bg='yellow')
        self.frame.place(x=50, y=50, width=300, height=300)

        self.button_ok = tk.Button(self.frame, text='Ok')
        self.button_ok.place(x=0, y=0, width=50, height=50)


root = tk.Tk()
gui = GUI(root)
root.mainloop()

