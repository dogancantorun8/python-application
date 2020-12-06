
#checkbox durumuna göre
import tkinter as tk

class GUI:
   def __init__(self, master):
       master.geometry('400x350')
       master.title('Sample Data Binding')
       self.master = master

       self.confim_result = tk.IntVar()
       self.confim_result.set(1) #burada 0 veya 1 veririrm 2,3 gibi sayıları tanımlayamam

       self.checkbutton_confirm = tk.Checkbutton(master, text='Okudum Onaylıyorum', font='Arial 10', variable=self.confim_result)
       self.checkbutton_confirm.place(x=10, y=10)

       self.button_ok = tk.Button(master, text='Ok', command=self.button_ok_handler)
       self.button_ok.place(x=200, y=10, width=70, height=70)

   def button_ok_handler(self):
      print('Checked' if self.confim_result.get() else 'Unchecked')


root = tk.Tk()
gdb = GUI(root)
root.mainloop()
