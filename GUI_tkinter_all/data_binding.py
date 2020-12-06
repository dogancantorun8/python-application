
#data binding islemiyle text field yazılan ne varsa herhangi bir variable a alıp islem yaparız
#textboxta yaptıgım degisiklik degiskeni etkiledi degiskendeki degisiklik de testboxu etkiledi
#entry get methodunu kullanmadan dogrudan field icerisinden degiskeni alıp islem yapabiliyoruz


import tkinter as tk

class GUIDatabase:
   def __init__(self, master):
       master.geometry('370x180')
       master.title('Sample Data Binding')
       self.master = master
       self.entry_name_text = tk.StringVar() #binding islemi string ozelinde yapılmıs
       self.entry_name_text.set('This is a test')

       self.entry_name = tk.Entry(master, font='Arial 15', textvariable=self.entry_name_text)
       self.entry_name.place(x=10, y=10)
       self.entry_name.focus()

       self.button_ok = tk.Button(master, text='Ok', command=self.button_ok_handler)
       self.button_ok.place(x=10, y=50, width=70, height=70)

   def button_ok_handler(self):
      s = self.entry_name_text.get()
      print(s)

root = tk.Tk()
gdb = GUIDatabase(root)
root.mainloop()

