import tkinter as tk
import tkinter.ttk as ttk
import tkinter.messagebox

#fbot ve anzelijg.github.io ttk icin referans sitelerim
#bu GuI de grid geometry manager kullanarak oluşturdum.
#combobox tk de olmayıp ttk de mevcuttur.
class GUI:
    def __init__(self, master):
        master.geometry('900x800')
        master.title('Sample Messagebox')

        self.label_name = ttk.Label(master, text='Adı Soyadı', font='Arial 16')
        self.label_name.grid(row=0, column=0, pady=5)

        self.entry_name = ttk.Entry(master, font='Arial 16')
        self.entry_name.grid(row=0, column=1, padx=(10, 0))

        self.label_no = ttk.Label(master, text='No', font='Arial 16')
        self.label_no.grid(row=1, column=0, pady=5)

        self.entry_no = ttk.Entry(master, font='Arial 16')
        self.entry_no.grid(row=1, column=1, padx=(10, 0))

        self.button_ok = ttk.Button(master, text='Ok', command=self.button_ok_handler)
        self.button_ok.grid(row=2, column=0, padx=(10, 0), pady=(20, 0))

        self.button_cancel = ttk.Button(master, text='Cancel')
        self.button_cancel.grid(row=2, column=1, padx=(10, 0), pady=(20, 0))

        self.check_button_email = ttk.Checkbutton(master, text='E Posta ile haber ver')
        self.check_button_email.grid(row=3, column=0, padx=(10, 0), pady=(20, 0))

        self.radio_button_a = ttk.Radiobutton(master, text='A')
        self.radio_button_a.grid(row=4, column=0, padx=(10, 0), pady=(20, 0))

        self.radio_button_b = ttk.Radiobutton(master, text='B')
        self.radio_button_b.grid(row=4, column=1, padx=(10, 0), pady=(20, 0))

        #tkinterdan farklı olarak ttkde combobox yaratıyorum
        #text variable ile comboboxun içindeki değeri get kullanıyormuş gibi alıyorum
        self.combobox_tv = tk.StringVar()

        self.combobox = ttk.Combobox(master, height=10, textvariable=self.combobox_tv, state='readonly')
        self.combobox.grid(row=5, column=0, padx=(10, 0))
        #comboboxun icine degerleri giriyorum
        self.combobox['values'] = ('Ankara', 'İzmir', 'Bursa', 'Çanakkale', 'Eskişehir')
        self.combobox.current(1)
        #comboboxun icine yeni degerler ekliyorum
        self.combobox['values'] += ('Sakarya', 'Samsun')
        #egercombobox bind yapılırsa ne olacagını yazıyorum
        self.combobox.bind('<<ComboboxSelected>>', self.combobox_selected_handler)

        #counter yaratmak istersem kullanıyorum
        self.spinbox1 = ttk.Spinbox(master, from_=0, to=10, width=10, wrap=True, increment=2, state='readonly')
        self.spinbox1.grid(row=6, column=0, pady=10)

        # counter yaratmak istersem kullanıyorum
        self.spinbox2 = ttk.Spinbox(master, values=['Ankara', 'İzmir', 'Kayseri', 'Samsun', 'Eskişehir'])
        self.spinbox2.grid(row=6, column=1, pady=10)

        self.progressbar = ttk.Progressbar(master, maximum=100, length=400)
        self.progressbar['value'] = 30
        self.progressbar.grid(row=7, column=0, columnspan=3, sticky='w') #sticky yardımıyla sola yasladım

        self.button_progress = ttk.Button(master, text='Progress', command=self.button_progress_handler)
        self.button_progress.grid(row=7, column=10)

        #notebook yaratıyorum tab kontrol diye
        self.notebook=ttk.Notebook(master,width=400,height=400)
        self.notebook.grid(row=8,columnspan=4,sticky='w',padx=10)


        #degistirmek istediğim kısmı notebooka bağlıyorum
        self.frame_keyboard_setting=ttk.Frame(self.notebook)
        self.frame_mouse_setting = ttk.Frame(self.notebook)
        self.notebook.add(self.frame_keyboard_setting,text='Keyboard')
        self.notebook.add(self.frame_mouse_setting, text='Mouse ')

        self.check_button_sound=ttk.Checkbutton(self.frame_keyboard_setting,text='Sound')
        self.check_button_sound.grid(row=0,column=0,pady=20)

        #keyboard settings penceremin icine butonlarımı yerleştirdim 
        self.radio_fast = ttk.Radiobutton(self.frame_keyboard_setting, text='Fast')
        self.radio_fast.grid(row=1, column=0, pady=20)

        self.radio_slow = ttk.Radiobutton(self.frame_keyboard_setting, text='slow')
        self.radio_slow.grid(row=1, column=1, pady=20)






    def button_ok_handler(self):
        print(self.combobox.get())  #combobox icinde secilen herhangi bir degeri backende print ediyorum
        print(self.combobox_tv.get()) #combobox icinde secilen herhangi bir degeri backende print ediyorum degisken yardımıyla
        print(self.spinbox1.get()) #spinbox icersindekini almak istersem kullanıyorum

    def combobox_selected_handler(self, event):
        print('Selected')

    def button_progress_handler(self):
        if self.progressbar['value'] == self.progressbar['maximum']:
            tk.messagebox.showinfo(title='Warning', message='it reached maximum value')
        self.progressbar['value'] = self.progressbar['value'] + 1

root = tk.Tk()
gdb = GUI(root)
root.mainloop()