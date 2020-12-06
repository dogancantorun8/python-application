import tkinter as tk
from tkinter import messagebox
from tkinter import simpledialog

class GUI:
    def __init__(self, master):
       master.geometry('800x600')
       master.title('Sample Messagebox')
       self.master = master

       self.button_ok = tk.Button(master, text='Ok', command=self.button_ok_handler)
       self.button_ok.place(x=30, y=30, width=60, height=30)

    def button_ok_handler(self):
       #messagebox.showinfo(title='Ornek mesaj',message='bu bir deneme')
       #messagebox.showerror(title='Ornek mesaj',message='bu bir deneme') #hata ile ilgili bunu eklerim
       result=messagebox.askyesnocancel(title='Ornek mesaj',message='Are you sure?') #result degiskenine deger atadım
       if result=='yes':
           messagebox.showinfo(message='Evet')
       else:
           messagebox.showinfo(message='İptal')

       


root = tk.Tk()
gdb = GUI(root)
root.mainloop()
