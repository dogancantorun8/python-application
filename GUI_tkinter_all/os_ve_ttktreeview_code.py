import tkinter as tk
import tkinter.ttk as ttk
import os
import os.path
import datetime

ROOT_PATH = 'C:\\'

class GUI:
    def __init__(self, master):
        master.geometry('900x800')
        master.title('Sample Messagebox')

        self.frame = tk.Frame(master)
        self.treeview = ttk.Treeview(self.frame, height=30, selectmode='browse', columns=('Directory', 'Modification Date'))
        self.text = tk.Text(self.frame, width=40)

        self.treeview.heading('Directory', text='Directory')
        self.treeview.heading('Modification Date', text='Modification Date')

        self.treeview.bind('<<TreeviewSelect>>', self.treeview_select_handler)
        self.treeview.bind('<<TreeviewOpen>>', self.treeview_open_handler)

        self.treeview.pack(side='left', expand=True, fill='both')
        self.text.pack(side='left', expand=True, fill='both')
        self.frame.pack(side='top', expand=True, fill='both')

        with os.scandir(ROOT_PATH) as it1:
            for entry1 in it1:
                try:
                    if entry1.is_dir():
                        id = self.treeview.insert('', 'end', tags=(entry1.path, False), text=os.path.basename(entry1.path), values=[os.path.dirname(entry1.path), self.getdate(entry1.path)])
                        with os.scandir(entry1.path) as it2:
                            for entry2 in it2:
                                if entry2.is_dir():
                                    self.treeview.insert(id, 'end', tags=(entry2.path, False), text=os.path.basename(entry2.path), values=[os.path.dirname(entry2.path), self.getdate(entry2.path)])
                except:
                    pass

        self.button_ok = ttk.Button(master, text='Ok', command=self.button_ok_handler)
        self.button_ok.pack(pady='10', side='top')

    def button_ok_handler(self):
      pass

    def treeview_select_handler(self, event):
        pass

    def treeview_open_handler(self, event):
        id = self.treeview.selection()[0]

        if self.treeview.item(id, 'tags')[1] == 'True':
            return

        for itemid in self.treeview.get_children(id):
            path = self.treeview.item(itemid, 'tags')[0]
            try:
                with os.scandir(path) as it:
                    for entry in it:
                            if entry.is_dir():
                                self.treeview.insert(itemid, 'end', tags=(entry.path, False), text=os.path.basename(entry.path), values=[os.path.dirname(entry.path), self.getdate(entry.path)])
            except:
                pass

        self.treeview.item(id, tags=(id, True))

    def getdate(self, path):
        t = os.path.getmtime(path)
        dt = datetime.datetime.fromtimestamp(t)
        return f'{dt.day:02d}/{dt.month:02d}/{dt.year:04d}'


root = tk.Tk()
gdb = GUI(root)
root.mainloop()