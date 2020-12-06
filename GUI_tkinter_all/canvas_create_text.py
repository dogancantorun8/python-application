import tkinter as tk
import datetime

class GUI:
    def __init__(self, master):
        master.geometry('800x600')
        master.title('Sample Messagebox')

        self.canvas = tk.Canvas(master, bg='white')
        self.canvas.pack(fill='both', expand=True)

        #yazının hangi koordinatlarda olacağını create_text fonk içinde belirtiyoruz
        self.text_id = self.canvas.create_text(200, 100, text='This is a test', font='Arial 12 bold underline', fill='red')

        xpos = 100
        ypos = 20
        for i in range(20):
            self.canvas.create_text(xpos, ypos, text=str(i), font='Arial 12 bold', fill='blue')
            ypos += 20

        #su andaki saati alı yazdırıyorum
        t = datetime.datetime.now()
        self.canvas.create_text(300, 300, text=f'{t.hour}:{t.minute}:{t.second}', fill='magenta', font='Calibri 30 bold')

root = tk.Tk()
gdb = GUI(root)
root.mainloop()

