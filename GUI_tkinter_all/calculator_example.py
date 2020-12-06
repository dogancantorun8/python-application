import tkinter as tk

class GUI:
    def __init__(self, master):
        master.title('Calculator')
        master.resizable(width=False, height=False)

        #master penceremi GUI'ye baslamadan konumlandırıyorum bunun üzerine frameleri insa ediyorum
        self.frame_main = tk.Frame(master)
        #konumlandırma icin pack yöntemini kullanıp konumlandırıyorum
        self.frame_main.pack(side='top', expand=True, fill='both', padx=10, pady=10)

        #kullanıcıdan input almak icin main frame üzerinde entry içinde bir textvariable tanımlıyorum
        self.textvariable = tk.StringVar()
        self.entry = tk.Entry(self.frame_main, justify='right', font='calibri 12', width=25, textvariable=self.textvariable, state='disabled', disabledbackground='white', disabledforeground='black')
        self.entry.pack(side='top', fill='x', pady=(0, 15))

        #BackSpace ve Clear All butonlarımdan olusan birinci frame'i tanımlayıp main frame'e bağlıyorum
        self.frame1 = tk.Frame(self.frame_main)
        self.button_backspace = tk.Button(self.frame1, text='Back Space', width=10)
        self.frame1.pack(side='top', anchor='w') #anchor parametresiyle w(west) şeklinde hizalıyorum

        self.button_backspace['command'] = lambda: self.button_handler(self.button_backspace) #backspace butonu icin command parametresine lambda yardımıyla handler tanımlıyorum
        self.button_backspace.pack(side='left', padx=(0, 10))

        self.button_clear = tk.Button(self.frame1, text='Clear All', width=10)
        self.button_clear['command'] = lambda: self.button_handler(self.button_clear) #Clear All butonu icin command parametresine lambda yardımıyla handler tanımlıyorum
        self.button_clear.pack(side='left')


        #1.satırda bulunan componentlerim icin frame2 tanımlıyorum
        self.frame2 = tk.Frame(self.frame_main)
        self.frame2.pack(side='top', anchor='w', pady=(10, 5))

        #frame2 uzerinde butonlarımı ve handlerları tanımlıyorum
        self.button_7 = tk.Button(self.frame2, text='7', width=4)
        self.button_7['command'] = lambda: self.button_handler(self.button_7)
        self.button_7.pack(side='left', padx=(0, 5))

        self.button_8 = tk.Button(self.frame2, text='8', width=4)
        self.button_8['command'] = lambda: self.button_handler(self.button_8)
        self.button_8.pack(side='left', padx=(0, 5))

        self.button_9 = tk.Button(self.frame2, text='9', width=4,)
        self.button_9['command'] = lambda: self.button_handler(self.button_9)
        self.button_9.pack(side='left', padx=(0, 5))

        self.button_slash = tk.Button(self.frame2, text='/', width=4)
        self.button_slash['command'] = lambda: self.button_handler(self.button_slash)
        self.button_slash.pack(side='left', padx=(0, 5))

        self.button_sqrt = tk.Button(self.frame2, text='sqrt', width=4)
        self.button_sqrt['command'] = lambda: self.button_handler(self.button_sqrt)
        self.button_sqrt.pack(side='left', padx=(0, 5))



        self.frame3 = tk.Frame(self.frame_main)

        self.button_4 = tk.Button(self.frame3, text='4', width=4)
        self.button_4['command'] = lambda: self.button_handler(self.button_4)
        self.button_4.pack(side='left', padx=(0, 5))

        self.button_5 = tk.Button(self.frame3, text='5', width=4)
        self.button_5['command'] = lambda: self.button_handler(self.button_5)
        self.button_5.pack(side='left', padx=(0, 5))

        self.button_6 = tk.Button(self.frame3, text='6', width=4)
        self.button_6['command'] = lambda: self.button_handler(self.button_6)
        self.button_6.pack(side='left', padx=(0, 5))

        self.button_multiply = tk.Button(self.frame3, text='*', width=4)
        self.button_multiply['command'] = lambda: self.button_handler(self.button_multiply)
        self.button_multiply.pack(side='left', padx=(0, 5))

        self.button_inverse = tk.Button(self.frame3, text='1/x', width=4)
        self.button_inverse['command'] = lambda: self.button_handler(self.button_inverse)
        self.button_inverse.pack(side='left', padx=(0, 5))

        self.frame3.pack(side='top', anchor='w', pady=(10, 5))

        self.frame4 = tk.Frame(self.frame_main)

        self.button_1 = tk.Button(self.frame4, text='1', width=4)
        self.button_1['command'] = lambda: self.button_handler(self.button_1)
        self.button_1.pack(side='left', padx=(0, 5))

        self.button_2 = tk.Button(self.frame4, text='2', width=4)
        self.button_2['command'] = lambda: self.button_handler(self.button_2)
        self.button_2.pack(side='left', padx=(0, 5))

        self.button_3 = tk.Button(self.frame4, text='3', width=4)
        self.button_3['command'] = lambda: self.button_handler(self.button_3)
        self.button_3.pack(side='left', padx=(0, 5))

        self.button_subtract = tk.Button(self.frame4, text='-', width=4)
        self.button_subtract['command'] = lambda: self.button_handler(self.button_subtract)
        self.button_subtract.pack(side='left', padx=(0, 5))

        self.button_pow = tk.Button(self.frame4, text='pow', width=4)
        self.button_pow['command'] = lambda: self.button_handler(self.button_pow)
        self.button_pow.pack(side='left', padx=(0, 5))

        self.frame4.pack(side='top', anchor='w', pady=(10, 5))

        self.frame5 = tk.Frame(self.frame_main)

        self.button_0 = tk.Button(self.frame5, text='0', width=4)
        self.button_0['command'] = lambda: self.button_handler(self.button_0)
        self.button_0.pack(side='left', padx=(0, 5))

        self.button_plusminus = tk.Button(self.frame5, text='+/-', width=4)
        self.button_plusminus['command'] = lambda: self.button_handler(self.button_plusminus)
        self.button_plusminus.pack(side='left', padx=(0, 5))

        self.button_dot = tk.Button(self.frame5, text='.', width=4)
        self.button_dot['command'] = lambda: self.button_handler(self.button_dot)
        self.button_dot.pack(side='left', padx=(0, 5))

        self.button_plus = tk.Button(self.frame5, text='+', width=4)
        self.button_plus['command'] = lambda: self.button_handler(self.button_plus)
        self.button_plus.pack(side='left', padx=(0, 5))

        self.button_equal = tk.Button(self.frame5, text='=', width=4)
        self.button_equal['command'] = lambda: self.button_handler(self.button_equal)
        self.button_equal.pack(side='left', padx=(0, 5))

        self.frame5.pack(side='top', anchor='w', pady=(10, 5))


        self.lastkey_op = False #bayrak degiskenim "islem yapıldıgında true duruma cekiyorumm"
        self.prev_val = 0   #hesap makinasında ilk girilen degeri atadıgım degisken
        self.last_op = None #son yapılan  operasyonu tuttugum degiskenim

                            ##########kodun back end kısmı ################

    def button_handler(self, button):
        #butonların hangisine basıldıgını anlamak icin butonun text parametresinden yararlanıyorum
        if button['text'] in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']:

            if self.lastkey_op: #islem yapılmadıgında last_key_op false durumda
                if self.last_op != '=': # en son operasyon esittir ise
                    self.prev_val = float(self.textvariable.get()) # "=" basıldıgında entrydeki yazan degeri prev_val 'a cekiyorum
                self.textvariable.set('') #entryi bosaltıyorum
                self.lastkey_op = False #bir onceki islem olmadıgı icin last_key_op false durumda oluyor
            self.textvariable.set(self.textvariable.get() + button['text'])

        #islem operatorleri icin yazdıgım blok
        elif button['text'] in ['+', '-', '*', '/'] and not self.lastkey_op:
            if self.last_op != None:
                if self.last_op == '+':
                    result = self.prev_val + float(self.textvariable.get())
                elif self.last_op  == '-':
                    result = self.prev_val - float(self.textvariable.get())
                elif self.last_op == '*':
                    result = self.prev_val * float(self.textvariable.get())
                elif self.last_op == '/':
                    result = self.prev_val / float(self.textvariable.get())

                #eger float bir islem olmamışsa int sayıları tam kımıyla yazıpp .0 seklinde yazmamak icin eklenen blok
                self.textvariable.set(int(result) if int(result) == result else result)

            self.lastkey_op = True
            self.last_op = button['text']

        # '=' butonuna üst üste basılırsa en son islem neyse o islem yapılmaya devam edilir
        elif button['text'] == '=' and self.last_op != None:
            if self.last_op == '+':
                result = self.prev_val + float(self.textvariable.get())
            elif self.last_op == '-':
                result = self.prev_val - float(self.textvariable.get())
            elif self.last_op == '*':
                result = self.prev_val * float(self.textvariable.get())
            elif self.last_op == '/':
                result = self.prev_val / float(self.textvariable.get())

            self.textvariable.set(int(result) if int(result) == result else result)
            self.last_op = None
            self.lastkey_op = True
            self.prev_val = 0
            self.start_flag = False

         #clear all butonuna basıldıgında tum parametreler sıfıra cekiliyor
        elif button['text'] == 'Clear All':
            self.lastkey_op = False
            self.prev_val = 0
            self.last_op = None
            self.textvariable.set('')

         #karekok isleminde sqrt butonu tetikleniyor
        elif button['text'] == 'sqrt':
            result = float(self.textvariable.get()) ** 0.5 #entry icerisindeki degiskene karekok aldırılıyor
            self.textvariable.set(int(result) if int(result) == result else result) #sonucun float olması check edilip entrye deger basılıyor
        elif button['text'] == '1/x':
            result = 1 / float(self.textvariable.get()) #entry icerisindeki degiskene 1/x  islemi uygulanıyor
            self.textvariable.set(int(result) if int(result) == result else result)
        elif button['text'] == 'Back Space':
            self.textvariable.set(self.textvariable.get()[:-1]) #son girilen degerden baslayarak siliyor
        elif button['text'] == '+/-':
            result = float(self.textvariable.get()) * -1  #entry icindeki deger toggle ediliyor
            self.textvariable.set(int(result) if int(result) == result else result)


root = tk.Tk()
gdb = GUI(root)
root.mainloop()