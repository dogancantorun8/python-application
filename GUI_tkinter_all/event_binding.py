# mesaj baglamaları
#klavye mouse gibi hareketlerde message binding islemi oluşur ve aksiyon alırız

import tkinter as tk


class GUI:
    def __init__(self, master):
        master.geometry('800x600')
        master.title('Sample Messagebox')
        master.resizable(width=False, height=False)
        self.master = master

        self.frame = tk.Frame(master, bg='light blue')
        self.frame.place(x=100, y=100, width=100, height=100)

        #frame penceresinde farenin sol tusuna basımını isledim
        self.frame.bind('<Button-1>', self.frame_button_down_handler)

        #root penceresinde farenin sol tusuna basımını isledim
        master.bind('<Button-1>', self.button_down_handler) #ana pencerede farenin sol tusuna basildiginda haberdar et demek

    def button_down_handler(self, pos):
        #pos bind methodunun çıktısı olarak geliyor ve jangi tuşa hangi koordinatta basıldıgını donuyor 
        print('root', '->', pos)

    def frame_button_down_handler(self, pos): #farenin sol tusuna basıldıgında yakalayan handler
        print('frame', '->', pos)
        return "break"


root = tk.Tk()
gdb = GUI(root)
root.mainloop()
