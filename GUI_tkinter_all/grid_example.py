import tkinter as tk
from PIL import Image
from PIL import ImageTk

class GUI:
    def __init__(self, master):
        master.title('Sample Messagebox')

        self.label_name = tk.Label(master, text='Adı Soyadı')
        self.label_name.grid(row=0, column=0, pady=(10, 5), padx=(10, 5), sticky='w')

        self.entry_name = tk.Entry(master, width=30)
        self.entry_name.grid(row=0, column=1, pady=(10, 5))

        self.label_no = tk.Label(master, text='No')
        self.label_no.grid(row=1, column=0, padx=(10, 5), sticky='w')

        self.entry_no = tk.Entry(master, width=30)
        self.entry_no.grid(row=1, column=1)

        self.check_button = tk.Checkbutton(master, text='E-Posta')
        self.check_button.grid(row=2, column=0, columnspan=2, sticky='w', padx=10, pady=10)

        img = Image.open('copy.png')
        img = img.resize((45, 45))
        img = ImageTk.PhotoImage(img)

        self.label_image = tk.Label(master, image=img)
        self.label_image.grid(row=0, column=2, columnspan=2, rowspan=2, sticky='wens')

        self.label_image.image=img

        self.button_ok = tk.Button(master, text='Ok', width=10)
        self.button_ok.grid(row=2, column=2, stick='w', padx=(0, 7))

        self.button_cancel = tk.Button(master, text='Cancel', width=10)
        self.button_cancel.grid(row=2, column=3, sticky='w', padx=(0, 10))

root = tk.Tk()
gdb = GUI(root)
root.mainloop()