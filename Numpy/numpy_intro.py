#numpy nümerik islemleri yapabilmek icin yazılmıştır.string ve numerik olmayan ifadelerin analizinde numpy kullanılmaz
#Scipy pandas ve keras numpy üzerine kurulmuştur.
#en önemli veri yapısı ndarray :numpy dizisi
#tüm vektörel işlemleri yapmamızı sağlayan ndarray
#numpy üzerindeki tüm fonksiyonlar ndarray ile işlem yapar
#numpy dizileri iterabledır.

import numpy as np

a=np.array([1,2,3,4])
print(type(a))
print(a)
b=np.array([[1,2,3],[4,5,6],[7,8,9]])
print(b)
#kaç satır kaç sütun var onu anlamak istersem    kaça kaç  olduğunu söylüyor  shape her boyutun uzunluğunuda veriyor

print("Satır ve sütun sayısını veriyor =",b.shape)
#len.shape = ndim oluyor shape n dimden daha kullanışlı
print(b.ndim)
print('----------------3 boyut cıktıları---------------')
#3 boyutlu dizi örneğim:
c = np.array([[[1, 2, 3], [4, 5.5, 6], [7, 8, 9]], [[1, 2, 3], [4, 5, 6], [7, 8, 9]]])
print(c)
print(" C nin satır ve sütun sayısını veriyor =",c.shape)
print(c.ndim)
#dtype fonksiyonu ile işlem yapılan arrayın tipini değiştirebiliriz
#dtype arrayin elemanlarının tipine göre dönüş yapar eğer noktalı bir sayı varsa dtype bize float ile dönüş yapar
#dtype in içinde bir eleman floatsa diğerleride float şeklinde tutulur.eğer bir string vara hepsi yazıya dönüşür ve dtype U32 olur.
print("C nump arrayin tipi =",c.dtype)
#np.zeros ile 3 satır 2 sütunluk matris
d=np.zeros((3,2))
print("D zeros matrisim  =")
print(d)
print()
#5x2 lik matris ve dtype int16
e=np.ones((5,2),dtype=np.int16)
print()
print("E ones matrisim  =")
print(e)

#np.full ile istediğim sayılarda oluşan bir array yapabilirim
#her elemanı 3 olan matris yapmak istersem
f=np.full((2,2),3)
print()
print("Her elemanı 3 olan  matrisim  =")
print(f)
print()

#ndarraylerle işlem yapıldığında vektörel işlem yapılır
m=np.array([1,2,3])
n=np.array([16,64,49])
k=m+n #matris toplaması yapılıyor
print("Toplam matrisim  =")
print(k)
print()

#her degerimimin karekökünü alırsam
print(np.sqrt(n))
#her değerimi skaler ile çarpıyorum
print(3*n)
#arange fonksiyonu:
ar=np.arange(10,20,2,dtype='float32')
print(ar)

#linspace:0 ve 10 dahil bu aralığı 11 e bölüyor
g = np.linspace(0, 10, 11)
print(g)

#mathplotlib ve numpy
x = np.linspace(-2.14, 3.14, 100) #önce x leri alıyor -2.14 ve 3.14 arasını 100 parçaya bölüyor
y = np.sin(x) #sonra yukardaki x lerin sinüs değerini buluyor
import matplotlib.pyplot as plt
plt.plot(x, y) #sonra x değerini alıyor sonra sinüs değerini alıyor sonra iki indisten oluşan noktaları birleştiriyor
plt.show()

#empty fonksiyonu ile de ndarray yaratılır.ndarrayı yaratıyor icinde herhangi bir değer yok elemanları buraya atıyoruz
#order='C' şeklindeki dizilim sütunsal şeklinde bir yerleşimi söyler.order='R' olursa satırsal saklama yapılır

a=np.ones((4,3))
b=np.zeros_like(a) # a nın shape ine bakıp onunla aynı shapede zero matrisi yaratıyor

#identy  ile birim matris oluşturuyorum
a = np.identity(5, dtype='int8')
print()
print("Birim matrisim")
print(a)

#eye fonksiyonu:
a = np.eye(5, k=0, dtype='int8')
print(a)
print()
a = np.eye(5, k=-1, dtype='int8')
print(a)

#bir matrisin diagonalini almak istersem  sol köşegenindeki elemanları veriyor
a = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print("Diagonal işlem yapmak istedğim matrisim")
print(a)
b = np.diag(a)
print()
print("Diagonal matrisim")
print(b)
a = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])


































