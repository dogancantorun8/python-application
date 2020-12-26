import numpy as np

a = np.array([[1, 2, 3, 4], [4, 5, 6, 7], [8, 9, 10, 11], [12, 13, 14, 15]])
print(a)
print()
#numpy elemanlarıma erişiyorum
b = a[1:3, 1:4] #1.satır ve 3.satır al ve 1. satır ve 4.sütunu al
print(b)
print()
c = a[3, :]
print(c)

# 1)list index
a = np.arange(12)
print(a)
b = a[[2, 5, 7]]  #2,5 ve 7. indisteki elemanları bu şekilde alabilirim burayı bir tuple olarak da verebilirdim a[(1,2,3)]
print(b)

#list indexiyle generic olarak elemanları çekmek istersem
a = np.arange(12)
print(a)
i = np.array([2, 5, 7, 9])
b = a[i]
print(b)
#2)elipsis indexleme:Sütunların hepsini almak istersem elipsis kullanabilirim ve birden fazla boyut varsa elipsis kullanmam uygun olacaktır
#3)bool indexleme:elimizdeki bir np arrayin elemanları aynı eleman sayısındaki bir true false listeye indexleyip işlem yapabiliriz
a = np.array([10, 20, 30, 40, 50])
b = np.array([True, True, False, True, False], dtype='bool')
c = a[b]
print(c)

#Not:Bir numpy dizisini karşılaştırma operatörüyle kullanırsam numpy dizisinin her elemanı işleme sokulur ve sonuç alınır
a = np.array([18, 40, 20, 80, 50])
b = a[a > 30] #bool indeksleme cok yaygın bir kullanım
print(b)

#iki numpy dizisi yardımıyla öğrenciler ve notlarını tutuyorum notu 50 den büyük öğrencilerimi çekiyorum
a = np.array(['ali', 'veli', 'selami', 'ayşe', 'fatma'])
b = np.array([10, 79, 20, 45, 70])
c = a[b >= 50] # notu 50 den büyük öğrenciler koşulu
print(c)

#bool vektörü sum işlemine sokulursa true değer 1 false değer 0 olur
import numpy as np
a = np.array([10, 79, 20, 45, 70, 91, 68])
result = np.sum(a > 30)
print(result)

#ortalamadan büyük değerleri  almak istersem
a = np.array([10, 79, 20, 45, 70, 91, 68])
result = a[a >= np.mean(a)]
print(result)

#belirli bir aralıktaki degerleri almak istersem
a = np.array([10, 79, 20, 45, 70, 91, 68])
result = a[(a > 30) & (a < 80)]
print(result)
""""
a = np.array([10, 79, 20, 45, 70, 91, 68])

result = a[np.logical_and(a > 30, a < 80)]
print(result)
"""
#view:dilimleme ile yaptığımız gibi asıl diziden bir kısım alıp başka bir nesne oluşturmuyoruz.
#b nesnesi asıl dizideki değişikliklerden etkilenen ve kendisindeki değişiliklerle asıl diziyi etkileyebilecek bir nesne
#ek olarak yalnızca numpy da dilimleme işlemlerinde view oluşur.Diğer operasyonlarda view nesnesi oluşmaz
a = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(a)
print()
b = a[1:3, 0:2]
print(b)
print()
a[1, 1] = 100
print(b)
b[0, 0] = 50
print(a)

#ndarray boyut değiştirme nasıl yapılır;
a = np.arange(12)
b = np.reshape(a, (4, 3)) #4 satır 3 sütundan oluşan bir matris elde ettim reshape bağımsız bir nesne vermez view nesnesi verir
print(a)
print()
print(b)

""" boyut değiştirme işleminin global fonk ile yazımı
a = np.arange(12)
b = a.reshape((2, 6))

print(a)
print(b)

"""
#np array oluşturdum ve reshape ettim method ile
a = np.arange(12).reshape(3, 4)
print(a)
#reshape edilmiş bir matrisi başka bir boyuta almak istersem,ilk önce tek boyutmuş gibi düşüneceğiz ardından tek boyutlu matrisimizi yeni boyutlarda reshape ediyoruz


#resize  global methodu ve resize fonksiyonu:esize view oluşturmadan direk copy yoluyla yeni nesne elde ediyoruz
a = np.array([10, 20, 30, 40, 50, 60])
b = np.resize(a, (3, 2))
print(a)
print('-----------')
print(b)
a[0] = 100
print('-----------')
print(a)
print('-----------')
print(b)
#resize aynı zamanda ndarrayin methodu olarakta kullanılıyor burada mevcut nesne kullanılıyor kopya oluşturulmuyor
a = np.array([10, 20, 30, 40, 50, 60])
a.resize(3, 2)
print(a)
print('-----------')

#flatten reshape edilmiş arrayi tek boyutlu hale getiriyor sütunları yan yana getiriyor
a = np.array([[10, 20, 30], [40, 50, 60]])
b = a.flatten()
print(b)

#transpoz global fonksiyonu ve methodu vardır.bu işlemde view nesnesi ile olur yani b deki değişim a yı etkiler
a = np.arange(12).reshape(4, 3)
print(a)
print('------')
b = np.transpose(a)
print(b)
print('------')
c = b.transpose()
print(c)
print('------')

#global vstack ve hstack fonksiyonları :
#1)vstack:n tane satır vektöründen bir tane yeni nesne oluşturuyor:3 bağımsız ndarray birleştirdim
x = np.array([1, 2, 3])
y = np.array([10, 20, 30])
z = np.array([100, 200, 300])
a = np.vstack((x, y, z))
print(a)
#2)hstack:horizontal yığılma yapıyor :hstackte sütun sütun işlem yapabilmek için sütun vektörü olmalı
x = np.array([[1], [2], [3]])
y = np.array([[10], [20], [30]]) #bu şekilde bir yazım ile sütun vektörü oluyor
z = np.array([[100], [200], [300]])

a = np.hstack((x, y, z))
print(a)

"""alternatif hstack yapma 
x = np.array([1, 2, 3]).reshape(3, 1)
y = np.array([4, 5, 6]).reshape(3, 1)
z = np.array([7, 8, 9]).reshape(3, 1)

a = np.hstack((x, y, z))
print(a)


"""

#numpy nesnesine  a.base dersek sonuc none  değil ise view nesnesi oluyor.eşitse view nesnesi oluyor











