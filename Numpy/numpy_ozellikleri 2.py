#dizinin belli bir elemanına erişmek istersem
#darrayin içindeki herhangi bir elemana erişmek istersem virgü kulanıyorum
#numpy dizisi farklı tip elemandan oluşamaz


import numpy as np
a = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(a[0,2])
print(a[1,2])
print(a[1]) #1.satırın hepsine erişiyorum

#ndarray nesneleri mutable değiştirilebilir nesnelerdir
a[1,2]=10
print(a[1,2])

#dilimlemek istersem
print(a[0:2])
print()
print(a[:,1:3]) #satırların hepsini sütunlarn 1 ve 3sünü alıyorum

#dilimleme exercise
a = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]]
a=np.array(a)
print('Dilimleme kısmım')
print(a)
print(a[:,1:3])
print(a[1:3,1:3]) #6,7 10 11 elemanlarını almak istiyorum
print(a[3]) #son satırı almak istersem

#listede istenilen kısmı elde etme sartı:bool indeksleme ile 5 ten büyük elemanlara eriştim
a = np.array([3, 6, 9, 3, 7, 10, 9, 8])
b = a[a > 5] #burada true olanları alıp b ye atama yapıyorum
print(b)

#herhangi birer indisteki elemanlara erişmek istersem burada çoklu indeksleme yaptım
a = np.array([3, 6, 9, 3, 7, 10, 9, 8])
b = [1, 6, 4] #a ndarrayde istediğim elemanı b icinde belirtiyorum
c = a[b] #belirttiğim elemanları c ndarraye atıyorum
print(c)
print(type(c))




