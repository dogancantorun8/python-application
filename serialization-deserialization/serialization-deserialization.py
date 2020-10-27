# -*- coding: utf-8 -*-
"""
Created on Sat Oct 24 17:01:11 2020

@author: Dogancan Torun
"""

#Subject:Serialization-Deserialization


#Nesnelerin seri hale getirilmesi:Object serialization 
#bir nesnenin içindeki herbilginin bir diske veya sockete yazıp tekrardan geri alınmasına serialization denir 
#object serialization pickle modülüyle yapılıyor. 
#seri hale getirme işlemi default olarak binary olarak serileştirir 
#herhangi bir yerden çektiğim datayı dbde saklamadan herhangi bir veri tabanında saklamadan hızlı bir sekildeerismek için bunu kullanıyorum
import pickle

a = [10, ['ali', 'veli', 'selami'], 12.3]


#bir nesnenin fotoğrafını çekip dosyaya aktarmak için pickle modülünün dump fonk kullanılır 
with open('test.dat', 'w+b') as f: #testdat binary file 
    pickle.dump(a, f) 

#pickle modülünün load fonk ile dosyaya yazılmış nesnem okunabilir. 
with open('test.dat','rb') as f: 
    a = pickle.load(f)

print(a) #okudugum nesnemi a ya atadım. 

#W moduyla pickle modülü kullanımı 
import pickle
a = [('Dogancan Torun', 123, 'Murat Atılgan'), ('Ali Serçe', 765, 'Şehremini Lisesi'), ('Ayşe Er', 745, 'Demiryolu Lisesi')]
with open('test.dat', 'w+b') as f:
    pickle.dump(a, f)

with open('test.dat','rb') as f: 
    a = pickle.load(f)
print(a) #okudugum nesnemi a ya atadım. 
    
#pickle modülünün diğer önemli iki fonksiyonu loads ve dumpstur. 
a = [('Dogancan Torun', 123, 'Murat Atılgan'), ('Ali Serçe', 765, 'Şehremini Lisesi'), ('Ayşe Er', 745, 'Demiryolu Lisesi')] 

#pickle dumps dosyaya yazmadan direk bize binary nesneyi veriyor istersek sockete vs verebiliriz 
#pickle loads ile de binary hale gelen nesnmi okuyorum dosyaya yazmadan 
import pickle
a = [('Kaan Aslan', 123, 'Murat Atılgan'), ('Ali Serçe', 765, 'Şehremini Lisesi'), ('Ayşe Er', 745, 'Demiryolu Lisesi')]
x = pickle.dumps(a)
print('X nesnesi = {}'.format(x)) #x nesnesi binary nesnedir
print('\n')
y = pickle.loads(x)
print('Y nesnesi = {}'.format(y)) 

#sözlük nesnesini serileştirme örneği 
import pickle
a = {'Ali Serçe': ['Fizik', 'Kimya', 'Biyoloji'], 'Kaan Aslan': ['Matematik', 'Coğrafya', 'Edebiyat']}
x = pickle.dumps(a)
print(x)
y = pickle.loads(x)
print('Y nesnesi = {}'.format(y)) 
y = pickle.loads(x)
print(y)

#sınıfı serileştirme: 
import pickle
class Person:
    def __init__(self, name, no):
        self.name = name
        self.no = no

    def __str__(self):
        return f'{self.name}, {self.no}'

per = Person('Ali Serçe', 123)
x = pickle.dumps(per)
y = pickle.loads(x)
print(y)

#türemiş sınıfı serileştirme örneği date sınıfını kullandım
import pickle
import datetime
class Person:
    def __init__(self, name, no, bdate):
        self.name = name
        self.no = no
        self.bdate = bdate

    def __str__(self):
        return f'{self.name}, {self.no}, {self.bdate}'
    
per = Person('Ali Serçe', 123, datetime.date(1990, 12, 5))
x = pickle.dumps(per)
y = pickle.loads(x)
print(y) 

#gerekirse pickler sınıfıda serialization işlemlerinde kullanılabilir 

#dumpın işlem yaparken protokol parametreside mevcuttur.
#sadece ascı karakterler kullanılsın istersek protocol olarak '0' kullanılır 
import pickle
a = [1, 2, 3]
x = pickle.dumps(a, 0)
print(x)
y = pickle.loads(x)
print(y)

#not:dbmlerde veri saklarken key ve valuelerın veri tipi bytes veya string olmalı

#python programlarının sonlandırılması :sys.exit ,le bu işlemi yapabiliriz  
#isletim sistemlerinde her prosesin bitiminde exit code üretir. 
#eger programda hiç sys.exit kullanmamışsak dosya sonunda kod bittiğinde exit code 0 olur
import sys
a = int(input('Bir değer giriniz:'))

if a == 0:
   sys.exit()

for i in range(a):
   print(i)
#exit code none zero deger atadım ve proses sonlandı
import sys
a = int(input('Bir değer giriniz:'))

if a == 0:
   sys.exit(1)
for i in range(a):
   print(i)

#shelve modülü kullanımı : bu modülde dbmden farkı valueler bytes olmak zorunda değil,anahtar hala buytes veyastribg olmalıs ... 
import shelve
sh = shelve.open('myshelv', 'c')
sh['ali'] = 123
sh['veli'] = 68
result = sh['ali']
print(result) 



