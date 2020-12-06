import tkinter as tk
from PIL import Image
from PIL import ImageTk

#mouse a tıkladığında image yaratıyor
class GUI:
    def __init__(self, master):
        master.geometry('800x600')
        master.title('Sample Messagebox')

        img = Image.open('abbey_road.jpg')
        img = ImageTk.PhotoImage(img)

        self.canvas = tk.Canvas(master, bg='white')
        self.canvas.img = img
        self.canvas.bind('<Button-1>', self.click_handler)

        self.canvas.pack(fill='both', expand=True)

    def click_handler(self, event):
        self.canvas.create_image(event.x, event.y, image=self.canvas.img)

root = tk.Tk()
gdb = GUI(root)
root.mainloop()
