#numpy dizilerinde  axis kavramı :
#0.eksen:satır ekseni
#1.eksen:sütun ekseni
#3.eksen:z ekseni

import numpy as np

#3 boyutlu bir dizide axis işlemi
a = np.arange(24).reshape(3, 4, 2)
print(a)
print('---------')
x = np.sum(a, axis=0)
print(x)

#expand_dims fonksiyonu ile 2 boyutlu bir diziyi 3 boyuta cıkarabiliriz.
#numpy methodları genelde işlem sonuçlarında yeni nesneler verir

#insert methodu:insert işlemlerinde view oluşmaz

#tek boyutlu insert işlemi:
a = np.arange(24)
print(a)
b = np.insert(a, 8, 100)
print(b)

#iki boyutu insert işlemi:axis=0 ile satır eklerim axis=1 ile sütun eklerim
a = np.arange(12).reshape(4, 3)
print(a)
print('---------')
b = np.insert(a, 2, 100, axis=0) #satır insert ettim
print(b)

##2 boyutta aynı satıra farklı elemanlar eklemek istersem
a = np.arange(12).reshape(4, 3)
print(a)
print('------------')
b = np.insert(a, 2, [100, 200, 300], axis=0)
print(b)

###sütun eklemek istersem
a = np.arange(12).reshape(4, 3)
print(a)
print('------------')
b = np.insert(a, 3, 100, axis=1) #tüm sutunları 100 olan bir sütun
print(b)

###bir sütuna farklı elemanlar eklemek istersem
a = np.arange(12).reshape(4, 3)
print(a)
print('------------')
b = np.insert(a, 3, [100, 200, 300, 400], axis=1)
print(b)

#delete islemi:
a = np.arange(12).reshape(4, 3)
print(a)
print('------------')
b = np.delete(a, 2, axis=0) #satır silme yaptım
print(b)
b=np.delete(a,1,axis=1) #sütun sildim
print(b)

#append işlemi:insertten farkı yok
a = np.arange(12)
print(a)
print('------------')
b = np.append(a, 100)
print(b)

####append örneği :insert ie de yaparım bu işlemi ok ta gerekli değil
a = np.arange(12).reshape(4, 3)
print(a)
print('------------')
b = np.append(a, [[100, 200, 300]], axis=0) #eklerken iki boyutlu satır vektörü istiyor
print(b)

#append ile birden fazla satır yada sütun eklemesi yapılmaktadır
###append örneği2:
a = np.arange(12).reshape(4, 3)
print(a)
print('------------')
b = np.append(a, [[100], [200], [300], [400]], axis=1) #kolon insert işlemi yaptım
print(b)

