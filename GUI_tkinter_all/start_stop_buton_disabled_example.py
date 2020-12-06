
#start stop mechanism example
import tkinter as tk

class GUIDatabase:
   def __init__(self, master):
       self.master = master
       master.geometry('360x180')

       self.button_start = tk.Button(master, text='Start', command=self.button_start_handler)
       self.button_start.place(x=10, y=10, width=70, height=70)

       self.button_stop = tk.Button(master, text='Stop', state=tk.DISABLED, command=self.button_stop_handler)
       self.button_stop.place(x=100, y=10, width=70, height=70)

   def button_start_handler(self):
      print('Started')
      self.button_start.config(state=tk.DISABLED)
      self.button_stop.config(state=tk.NORMAL)

   def button_stop_handler(self):
      print('Stopped')
      self.button_start.config(state=tk.NORMAL)
      self.button_stop.config(state=tk.DISABLED)


root = tk.Tk()
gdb = GUIDatabase(root)
root.mainloop()
