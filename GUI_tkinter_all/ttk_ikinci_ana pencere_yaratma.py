import tkinter as tk
from PIL import Image
from PIL import ImageTk

class GUI:
    def __init__(self, master):
        master.geometry('800x600')
        master.title('Tk Sınıfından Ana pencere')
        self.master = master

        self.text = tk.Text(master)
        self.text.pack(side='top', fill='both', expand=True)
        self.button_create = tk.Button(master, text='Create Modal Dialog', command=self.button_create_handler)
        self.button_create.pack()

    def button_create_handler(self):
        self.myDialog = MyDialog(self.master)

class MyDialog(tk.Toplevel):
    def __init__(self, master):
        super().__init__(master)
        self.geometry('+400+400')
        master.resizable(width=False, height=False)

        self.transient(master)
        self.grab_set()

        master.resizable(width=True, height=True)

        self.label_name = tk.Label(self, text='Adı Soyadı')
        self.label_name.grid(row=0, column=0, pady=(10, 5), padx=(10, 5), sticky='w')

        self.entry_name = tk.Entry(self, width=30)
        self.entry_name.grid(row=0, column=1, pady=(10, 5))

        self.label_no = tk.Label(self, text='No')
        self.label_no.grid(row=1, column=0, padx=(10, 5), sticky='w')

        self.entry_no = tk.Entry(self, width=30)
        self.entry_no.grid(row=1, column=1)

        self.check_button = tk.Checkbutton(self, text='E-Posta')
        self.check_button.grid(row=2, column=0, columnspan=2, sticky='w', padx=10, pady=10)

        img = Image.open('copy.png')
        img = img.resize((45, 45))
        img = ImageTk.PhotoImage(img)

        self.label_image = tk.Label(self, image=img)
        self.label_image.grid(row=0, column=2, columnspan=2, rowspan=2, sticky='wens')

        self.label_image.image = img

        self.button_ok = tk.Button(self, text='Ok', width=10, command=self.button_ok_handler)
        self.button_ok.grid(row=2, column=2, stick='w', padx=(0, 7))

        self.button_cancel = tk.Button(self, text='Cancel', width=10, command=self.button_cancel_handler)
        self.button_cancel.grid(row=2, column=3, sticky='w', padx=(0, 10))

    def button_ok_handler(self):
        self.destroy()

    def button_cancel_handler(self):
        self.destroy()


root = tk.Tk()
gdb = GUI(root)

root.mainloop()