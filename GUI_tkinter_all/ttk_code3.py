import tkinter as tk
import tkinter.ttk as ttk

class GUI:
    def __init__(self, master):
        master.geometry('900x800')
        master.title('Sample Messagebox')

        self.ddict = {'Deri Mantarı': 'Deri mantarı tehlikeli olmayan kronik bir hastalıktır.',
                      'Bakteri Enfeksiyonları': 'Yüksek ateş görülür, antibiyotikle tedavi edilir.'}

        self.frame = tk.Frame(master)
        self.treeview = ttk.Treeview(self.frame, height=30)
        self.text = tk.Text(self.frame)

        self.treeview.bind('<<TreeviewSelect>>', self.treeview_select_handler)
        self.treeview.pack(side='left', expand=True, fill='both')
        self.text.pack(side='left', expand=True, fill='both')
        self.frame.pack(side='top', expand=True, fill='both')

        id1 = self.treeview.insert('', 0, text='Hastalıklar')
        self.treeview.insert(id1, 0, text='Kalp Hastalıkları')
        id2 = self.treeview.insert(id1, 1, text='Enfeksiyon Hastalıkları')
        self.treeview.insert(id2, 0, text='Bakteri Enfeksiyonları')
        self.treeview.insert(id2, 1, text='Viral Enfeksiyonlar')

        id3 = self.treeview.insert(id1, 2, text='Deri Hastalıkları')
        self.treeview.insert(id3, 0, text='Deri Mantarı')
        self.treeview.insert(id3, 1, text='Egzama')

        self.button_ok = ttk.Button(master, text='Ok', command=self.button_ok_handler)
        self.button_ok.pack(pady='10', side='top')



    def button_ok_handler(self):
      pass

    def treeview_select_handler(self, event):
        selected_id = self.treeview.selection()[0]
        text = self.treeview.item(selected_id, option='text')
        value = self.ddict.get(text)
        if value:
            self.text.delete('1.0', 'end')
            self.text.insert('end', value)
            print(text)
        else:
            self.text.delete('1.0', 'end')





root = tk.Tk()
gdb = GUI(root)
root.mainloop()