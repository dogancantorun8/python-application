import tkinter as tk
import tkinter.messagebox


class GUI:
    def __init__(self, master):
        master.geometry('800x600')
        master.title('Sample Messagebox')
        master.resizable(width=False, height=False)
        self.master = master

        self.button = tk.Button(master, text='Ok')
        self.button.place(x=10, y=10, width=100, height=100)
        self.button_x = 10
        self.button_y = 10

        self.button.bind('<Button-1>', self.button_down_handler)
        #tasıma islemi icin tanımladıgım binding islemi
        self.button.bind('<B1-Motion>', self.button_motion_handler)

    #event tetiklendiginde ilk konumları degiskenlere atıyorum
    def button_down_handler(self, event):
        self.button_firstx = event.x
        self.button_firsty = event.y

    #konum degisliginde motion handlerda ne kadar degistigini delta icerisinde tutuyorum
    def button_motion_handler(self, event):
        deltax = event.x - self.button_firstx
        deltay = event.y - self.button_firsty

        #butonun yeni konumu mutlak delta kadar eklenmisi oluyor
        self.button_x += deltax
        self.button_y += deltay

        #buttonun son konumu tekrardan ilk konum olarak veriliyor
        self.button.place(x=self.button_x, y=self.button_y)


root = tk.Tk()
gdb = GUI(root)
root.mainloop()
