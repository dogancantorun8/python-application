import tkinter as tk

import tkinter as tk

class GUI:
    def __init__(self, master):
        master.geometry('800x600')
        master.title('Sample Messagebox')

        self.canvas = tk.Canvas(master, bg='white')
        self.canvas.pack(fill='both', expand=True)

        self.canvas.create_line(0, 100, 100, 100, fill='red', width=10, capstyle='round', joinstyle='miter')
        self.canvas.create_line(100, 100, 100, 200, fill='red', width=10, capstyle='round')

        self.canvas.create_rectangle(150, 150, 200, 200, width=8, fill='blue', outline='red')
        self.canvas.create_polygon([(500, 50), (300, 300), (500, 500), (700, 300)], fill='magenta', outline='blue', width=5)
        self.canvas.create_arc(200, 400, 400, 500, fill='blue', width=5, outline='red')

        self.canvas.create_oval(100, 450, 200, 500, fill='lightblue', width=5, outline='red')

root = tk.Tk()
gdb = GUI(root)
root.mainloop()
