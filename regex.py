# -*- coding: utf-8 -*-
"""
Created on Wed Oct 21 16:49:54 2020

@author: Dogancan Torun
"""


#Düzenli ifadeler:(Regular-Expressions(Reg-Ex)) : 
#Komplex aramaları( belli bir kalıba uygun parçaları aramak )için kullanılıyor  
#Bu kavram pythona özgü değildir.Bu tip aramaları yapan modüllere reguler expression engine denir 
#import re modülüyle pythonda bu işlemler yapılır 
#regex karakter listesi +,* vs kullanımı bilinmeli.Kapsamlı aramalarda kullanacağım 
import re
text = 'bugin hava çok güzel. 12/12/2009. Evet çok güzel. 11/12/2009. Falan filan'
pattern = r'\d\d/\d\d/\d\d\d\d'
a = re.findall(pattern, text)  #tarihleri çektiğim kısım 
print(a)

#dosyadanda regex okuyabiliriz 
import re
f = open('test.txt')
text = f.read()
pattern = r'\d\d/\d\d/\d\d\d\d'
a = re.findall(pattern, text)
print(a)

#tüm patterni okuduk
import re
text = 'Eskişehir 26,   İstanbul 34,     İzmir 35'
pattern=r'\w+ \d\d'
a = re.findall(pattern, text)
print(a)

#search fonksiyonu:bize match nesnesi dönüyor:start ve stop ile başlangıç son karakterlerini veriyor 
import re
text = 'aşsdlkasjd ljas dlkasd12/102007sjdlkajsdlkasd10/10/2003'
pattern = r'\d\d/\d\d/\d\d\d\d'
m = re.search(pattern, text)
print(m.start(), m.end())
s = text[m.start():m.end()]
print(s)
#match nesnesi kullanımı ile kontrol mekanizması karakter bulunmazsa aşağıdaki gibi olur 
import re
text = 'aşsdlkasjd ljas dlkasd12/102007sjdlkajsdlkasd10/10/2003'
pattern = r'\d\d/\d\d/\d\d\d\dxxxx'
m = re.search(pattern, text)
if m:
    print(m.start(), m.end())
    s = text[m.start():m.end()]
    print(s)
else:
    print('bulunamadı!')

#gruplayarak arama yapmak istersem  
import re
text = 'ali-veli selami-uğur veli-can'
pattern = r'(\w+)-(\w+)'  #2 li gruplar oluşturdum
a = re.findall(pattern, text)
print(a)

#--yukarıdaki nesnenin patternini gruplamak istersem aşağıdaki çıktı oluşur; 
import re
text = 'ali-veli selami-uğur veli-can'
pattern = r'(\w+)-(\w+)'
a = re.search(pattern, text)
print(a.group(0))
print(a.group(1))
print(a.group(2))
print(a[0]) #collection şeklinde __getitem__  yazılmış bu şekilde de erişirim 

#ilk kırılımı elde etmek istersem 
import re
text = 'ali-veli selami-uğur veli-can'
pattern = r'\w+-\w+'
a = re.search(pattern, text)
print(a[0])
print(text[a.start():a.end()])

#search de pattern,text parametreleri veriyor,fakat aşağıda match fonksiyonu searche benziyor 
#fakat yazının bulunduğu tüm kısmı alıyor
import re
text = 'ayşe-fatma hgjhj hjhh ali-veli selami-uğur veli-can'
pattern = r'\w+-\w+'
a = re.match(pattern, text)
if not a:
    print('bulunamadı!')
else:
    print(a[0])

#matchnesnelerinin ilk indislerine ulaşmak istersem 
import re
text = 'kjhaskjdhkajsdkj10/12/2009ahjgdjhajshdjasdj/12/12/2001gajshgdajshdjas08/09/1998'
pattern = r'\d\d/\d\d/\d\d\d\d'
for m in re.finditer(pattern, text):
    print(m[0])

#regex ile split işlemi:stringin splitinden farklı olarak kalıbı split edecek 
#burada ayıraçların patterni yazılacak bulmak istediklerimizi patterni yazılmayacak 
import re
text = 'ali23423423veli2456564selami23487243678ayşe000012fatma'
pattern = r'\d+'
s = re.split(pattern, text)
print(s)
