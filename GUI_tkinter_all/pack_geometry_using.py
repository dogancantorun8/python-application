import tkinter as tk
import tkinter.filedialog
import tkinter.messagebox

#pixel hesabı yapmadan pack manager ile genisletilebilir bir pencere olusturdum
class GUI:
    def __init__(self, master):
        master.title('Sample Messagebox')

        self.master = master

        self.toolbar = tk.Frame(master)
        self.toolbar.pack(side='top', expand=True, fill='x')

        img = tk.PhotoImage(file='open.png')
        self.toolbar_button_open = tk.Button(self.toolbar, command=self.file_open_handler, image=img, padx=0, pady=0)
        self.toolbar_button_open.image = img
        self.toolbar_button_open.pack(side='left')

        img = tk.PhotoImage(file='save.png')
        self.toolbar_button_saveas = tk.Button(self.toolbar, command=self.file_saveas_handler, image=img, padx=0,
                                               pady=0)
        self.toolbar_button_saveas.image = img
        self.toolbar_button_saveas.pack(side='left')

        img = tk.PhotoImage(file='close.png')
        self.toolbar_button_close = tk.Button(self.toolbar, command=self.file_close_handler, image=img, padx=0, pady=0,
                                              state=tk.DISABLED)
        self.toolbar_button_close.image = img
        self.toolbar_button_close.pack(side='left')

        img = tk.PhotoImage(file='exit.png')
        self.toolbar_button_exit = tk.Button(self.toolbar, command=self.master.quit, image=img, padx=0, pady=0)
        self.toolbar_button_exit.image = img
        self.toolbar_button_exit.pack(side='left')

        img = tk.PhotoImage(file='cut.png')
        self.toolbar_button_cut = tk.Button(self.toolbar, command=self.edit_cut_handler, image=img, padx=0, pady=0)
        self.toolbar_button_cut.image = img
        self.toolbar_button_cut.place(x=300, y=0, width=64, height=64)

        #esit boxu expand yazarak genisletilebilir yaptım
        self.text = tk.Text(master, bg='white', font='Arial 20')
        self.text.pack(side='top', expand=True, fill='both')


    def file_open_handler(self, *args):
        try:
            path = tk.filedialog.askopenfilename(title='Dosya Seçimi',
                                                 filetypes=[('Python Files', '*.py'), ('Text Files', '*.txt')])
            if path != '':
                with open(path) as f:
                    self.text.delete('1.0', 'end')
                    self.text.insert('1.0', f.read())
            self.toolbar_button_open.config(state=tk.DISABLED)
            self.toolbar_button_close.config(state=tk.NORMAL)

        except Exception as e:
            tk.messagebox.showerror(title='Error', message=str(e))

    def file_saveas_handler(self, *args):
        try:
            path = tk.filedialog.asksaveasfilename(title='Dosya Seçimi',
                                                   filetypes=[('Python Files', '*.py'), ('Text Files', '*.txt')])
            if path != '':
                print(path)
                with open(path, 'w') as f:
                    s = self.text.get('1.0', 'end')
                    f.write(s)
        except Exception as e:
            tk.messagebox.showerror(title='Error', message=str(e))

    def file_close_handler(self):
        self.text.delete('1.0', 'end')
        self.toolbar_button_open.config(state=tk.NORMAL)
        self.toolbar_button_close.config(state=tk.DISABLED)

    def edit_cut_handler(self, *args):
        print('Cut')

    def edit_copy_handler(self, *args):
        print('Copy')

    def edit_paste_handler(self, *args):
        print('Paste')

root = tk.Tk()
gdb = GUI(root)
root.mainloop()
