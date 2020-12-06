# -*- coding: utf-8 -*-
"""
Created on Sun Oct 25 16:54:49 2020

@author: Dogancan Torun
"""

#Pythonda GUI Uygulamaları 
#WİDGET:Program açıldığında karşımıza çıkan ilk yapıya denir altında sibling windowlar olabilir 
#aynı widget uzerindeki childwindowlar widgetin uzerine cıkamazken owned windowlar widgetin uzerine cıkabilir
import tkinter as tk
import datetime

back_color=None
def button_ok_handler():
    print('pushed the ok button')
    root.config(bg='lightgreen') #arka plan butona basildıgında degisiyor

class button_cancel_handler():
    def __call__(self):
        global back_color
        print('cancel')
        root['bg']= back_color  #eski arkaplan rengine donus sagladım


def button_parameter_handler(msg):
    print(msg)


root=tk.Tk()#ana pencere nesnesini  yaratıyoruz 
root.geometry('600x480') #ana pencere boyutları
root.title('Ana pencerem') #ana pencereme baslık ekledim

#label
dt=datetime.datetime.now() #anlık zaman bilgisi nesnesini yarattım
label=tk.Label(root,text=dt.ctime(),bg='yellow',fg='red',font=('Arial',20,'italic')) #ilk parametre hangi widgetin altında olacaksa onu yazmalıyız,digerleri config parametreleri

label.place(x=100,y=50)
#widgetler   farklı sekilde configure edilebilir

#config methoduyla
''' 
label2=tk.Label(root)
label.config(text='This is a test2',bg='green',fg='red')
label.place(x=30,y=5) 
'''
#dict yardımıyla
'''
label3=tk.Label(root)
label3['text']='this is a new test label'
label3['bg']='yellow'
label3['fg']='red'
label.place(x=70,y=50) 
'''

#button:::::

#butonlara aksiyon oluştururken command parametresine fonk adı verilip tetikleme saglanabilir
button_ok=tk.Button(root,text='okay',command=button_ok_handler)
button_ok.place(x=10,y=100,width=40,height=30)

button_cancel=tk.Button(root,text='cancel',command=button_cancel_handler())
button_cancel.place(x=90,y=100,width=40,height=30)

#butonlara parametreleri olan bir fonk gecirip de cagrilabilir
button_fonk=tk.Button(root,text='prmtr',command=lambda:button_parameter_handler('parametreli butonum')) #lambda ifademe parametre verip cagiriyorum
button_fonk.place(x=150,y=100,width=50,height=30)



root.mainloop() #tum gui akışı main loop icerisindedir bu loop bitince akış sonlanır bir sonraki aşamaya geçer
print('ok') 

import functools
#functolls kullanımı: 
def foo(a,b,c) :
    print(a,b,c) 

p=functools.partial(foo,10,20,30)  #{fonksiyonu ve parametrelerini veriyorsun sınıf nesnesini veriyor
p()

