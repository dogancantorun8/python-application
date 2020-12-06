##ttk_styles:tk de style nesnesi yaratıp işlem yapmam
#ttk widgeetları icin gecerlidir.bir style nesnesi yarat ve istediğin widgetların configürasyonlarının bu nesne  üzerinden yap
#TButton dersem tum butonlarımı config ederim yani style nesnem ile configleri yapabilirim
#tcl.tk şeklinde aratırsam  bu konuda help alabilirim
import tkinter as tk
import tkinter.ttk as ttk

class GUI:
    def __init__(self, master):
        master.geometry('800x600')
        master.title('Sample Messagebox')

        style = ttk.Style()
        style.configure('N1.TEntry', foreground='red')
        style.configure('N2.TEntry', foreground='blue')


        self.entry1= ttk.Entry(master, font='Arial 20', style='N1.TEntry')
        #print(self.entry.winfo_class())
        self.entry1.pack(expand=True, fill='x', anchor='n', padx=10, pady=10)

        self.entry2 = ttk.Entry(master, style='N2.TEntry')
        # print(self.entry.winfo_class())
        self.entry2.pack(expand=True, fill='x', anchor='n', padx=10, pady=10)

        style.configure('TButton', font='Arial 20', foreground='red', background='yellow')

        self.button_ok = ttk.Button(master, text='Ok', style='TButton')
        self.button_ok.pack()


root = tk.Tk()
gdb = GUI(root)
root.mainloop()

