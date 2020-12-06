import tkinter as tk
from tkinter import messagebox
from tkinter import simpledialog
from tkinter import filedialog
import os

#kullanıcıdan giris almak istersek kullanıyoruz
class GUI:

    def __init__(self, master):
        master.geometry('800x600')
        master.title('Sample DialogBox')
        self.master = master

        self.button_ok = tk.Button(master, text='Ok', command=self.button_ok_handler)
        self.button_ok.place(x=30, y=30, width=60, height=30)

        self.button2 = tk.Button(master, text='but2', command=self.button2_handler)
        self.button2.place(x=80, y=80, width=60, height=30)



    def button_ok_handler(self):
        result = simpledialog.askstring('Deger girme', 'Bir deger giriniz:')
        if result !=None:
            messagebox.showinfo(message=result)


    def button2_handler(self):
        path = filedialog.askdirectory(title='Dizin secin') #sectigim directory pathine erişiyorum
        if path !='':
            #messagebox.showinfo(message=path)
            result2=os.listdir(path)
            s='\n'.join(result2) #listeyi string haline getirdim
            messagebox.showinfo(message=s) #path icindeki tum dosyaları display ediyorum




root = tk.Tk()
gdb = GUI(root)
root.mainloop()
