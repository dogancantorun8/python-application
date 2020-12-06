import tkinter as tk

class GUI:
   def __init__(self, master):
       master.geometry('400x350')
       master.title('Sample Data Binding')
       self.master = master

       self.listbox_cities = tk.Listbox(root, height=15, font='Arial 12', bg='light blue', fg='red', selectmode=tk.EXTENDED)
       self.listbox_cities.place(x=10, y=10)

       self.cities = {'Ankara': 6, 'İzmir': 35, 'İstanbul': 34, 'Eskişehir': 26, 'Aydın': 9, 'Samsun': 55,'Kocaeli': 41,
                      'Bilecik': 11, 'Bursa': 16, 'Manisa': 45, 'Maraş': 46, 'Balıkesir': 10, 'Ağrı': 4,
                      'Trabzon': 61, 'Mersin': 33, 'Siirt':56, 'Tunceli': 62, 'Tekirdağ': 59 }


       for key in self.cities.keys():
          self.listbox_cities.insert(tk.END, key)

       self.listbox_cities.bind('<Double-Button-1>', self.listbox_double_click)
       self.listbox_cities.activate(1)


       self.button_ok = tk.Button(master, text='Ok', command=self.button_ok_handler)
       self.button_ok.place(x=200, y=10, width=70, height=70)

       self.listbox_cities.focus()

   def button_ok_handler(self):
      s = self.listbox_cities.get(tk.ACTIVE)
      print(s)
      sel = self.listbox_cities.curselection()
      print(sel)

   def listbox_double_click(self, m):
       s = self.listbox_cities.get(tk.ACTIVE)
       print(self.cities[s])

root = tk.Tk()
gdb = GUI(root)
root.mainloop()