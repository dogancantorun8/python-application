import tkinter as tk
class GUI:
    def __init__(self,master):
        self.master=master #penceremin ustundeki configler icin master tanımımı kullandım

        self.label_name=tk.Label(master,text='Adı soyadı:',font=('Arial',10))
        self.label_name.place(x=10,y=10)


        #text fieldlerdan  tkinter uygulamalarında gui olarak bahsedilir
        self.entry_name=tk.Entry(master,font=('Arial',10),justify=tk.CENTER) #inputları almak icin kullanıyorum
        self.entry_name.place(x=10,y=32 ,width=200)

        self.button_ok=tk.Button(self.master,text='ok',command=self.button_ok_handler)
        self.button_ok.place(x=10,y=70,width=60,height=60)

        self.button_cancel = tk.Button(self.master, text='cancel', command=self.button_cancel_handler)
        self.button_cancel.place(x=160, y=70, width=60, height=60)

    def button_ok_handler(self):
        #print('ok')
        self.master['bg']='yellow'  #arkaplan rengimi degistirdim
        print(self.entry_name.get()) #textfieldda yazan bilgiyi get ile alıp backende bastım
        self.entry_name.delete(0,tk.END) #textfielda giris olduktan sonra fieldi temizler


    def button_cancel_handler(self):
        print('cancel')
        self.master['bg'] = 'lightblue'


root=tk.Tk() #rootu  yarattım
root.geometry('600x480')
root.title('Sample TK ')

gui=GUI(root) #burada rootu gui classına vererek root üzerinde yapacağım tüm configleri mastere vermiş oldum
root.mainloop()