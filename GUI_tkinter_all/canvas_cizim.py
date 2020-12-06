import tkinter as tk
import tkinter.messagebox

#canvas kullanınca  mouse ile cizim yapabiliyorum
class GUI:
    def __init__(self, master):
        master.geometry('800x600')
        master.title('Sample Messagebox')
        master.resizable(width=False, height=False)
        self.master = master

        self.canvas = tk.Canvas(master, bg='light blue') #canvas nesnesi tanımlıyorum
        self.canvas.place(x=20, y=20, width=600, height=400) # canvasın konumunu  belirtiyorum

        #cizimin basladıgı yeri alıyorum button 1 ile
        self.canvas.bind('<Button-1>', self.button_down_handler)

        #mouse ile basılı tutma eventini gerceklestiriyorum
        self.canvas.bind('<B1-Motion>', self.button_motion_handler)

    def button_down_handler(self, event):
        #farenin ilk basıldıgı koordinatları kaydettim
        self.x_prev = event.x
        self.y_prev = event.y

    def button_motion_handler(self, event):

        self.canvas.create_line(self.x_prev, self.y_prev, event.x, event.y, width=3) #farenin ilk koodinatları ve son koordinatları paraetre olarak alınıp cizim yaptırıldı
        #farenin en son kaldığı yer ilk konumu tutan  degiskenlere atandı
        self.x_prev = event.x
        self.y_prev = event.y

root = tk.Tk()
gdb = GUI(root)
root.mainloop()