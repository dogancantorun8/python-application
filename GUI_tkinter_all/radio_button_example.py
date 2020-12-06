import tkinter as tk

class GUI:
   def __init__(self, master):
       master.geometry('400x350')
       master.title('Sample Data Binding')
       self.master = master

       self.radio_result = tk.StringVar()
       self.radio_result.set(None)

       self.radio1 = tk.Radiobutton(master, text='Elma', value='Elma', variable=self.radio_result) #variable ları value ile tutuyoruz
       self.radio1.place(x=10, y=10)
       self.radio2 = tk.Radiobutton(master, text='Armut', value='Armut', variable=self.radio_result)
       self.radio2.place(x=10, y=30)
       self.radio3 = tk.Radiobutton(master, text='Kiraz', value='Kiraz', variable=self.radio_result)
       self.radio3.place(x=10, y=50)
       self.radio4 = tk.Radiobutton(master, text='Şeftati', value='Şeftali', variable=self.radio_result)
       self.radio4.place(x=10, y=70)
       self.radio5 = tk.Radiobutton(master, text='Portakal', value='Portakal', variable=self.radio_result)
       self.radio5.place(x=10, y=90)

       self.button_ok = tk.Button(master, text='Ok', command=self.button_ok_handler)
       self.button_ok.place(x=200, y=10, width=70, height=70)

   def button_ok_handler(self):
      print(self.radio_result.get())

root = tk.Tk()
gdb = GUI(root)
root.mainloop()