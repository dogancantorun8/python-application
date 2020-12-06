import tkinter as tk

#entryi genisletilebilir bir hale getirdim
class GUI:
    def __init__(self, master):
        master.title('Sample Messagebox')
        master.resizable(width=True, height=False)

        self.label_name = tk.Label(master, text='Adı Soyadı')
        self.label_name.grid(row=0, column=0, padx=(10, 10))

        self.entry_name = tk.Entry(master)
        self.entry_name.grid(row=0, column=1, sticky='we', padx=(0, 10))

        self.label_no = tk.Label(master, text='No')
        self.label_no.grid(row=1, column=0, padx=(10, 10), pady=(5, 10))

        self.entry_no = tk.Entry(master)
        self.entry_no.grid(row=1, column=1, sticky='we', padx=(0, 10), pady=(5, 10))

        master.columnconfigure(1, weight=1)

root = tk.Tk()
gdb = GUI(root)
root.mainloop()