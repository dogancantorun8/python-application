import tkinter as tk

class GUI:
    def __init__(self, master):
       master.geometry('800x600')
       master.resizable(width=False, height=False)
       master.title('Sample Text Widget')
       self.master = master

       self.text = tk.Text(master, font='Consolas 14', bg='light blue')
       self.text.place(x=0, y=0, width=800, height=550)

       self.button_ok = tk.Button(master, text='Ok', command=self.button_ok_handler)
       self.button_ok.place(x=30, y=560, width=60, height=30)

    def button_ok_handler(self):
        #s = self.text.get('1.3', '1.10') #1.satırın 3.karakterinden 10. karakterine kadar aldım
        #s = self.text.get('1', 'tk.END') #bu sekilde yaparsam text editorun tamamını alırım
        s = self.text.get('1.8 wordstart', 'end')
        #s = self.text.insert('1.8' ,' arayagirenyazi')
        #s = self.text.delete('1.8' ,'end') #delete ile silme yaptım
        print(s)

root = tk.Tk()
gdb = GUI(root)
root.mainloop()
