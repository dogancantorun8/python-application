#numpy dizileri üzerinde vektörel işlemler  :işleme girerken karşılıklı elemanlar işleme giriyor
#her elemana aynı skaler işlemleri yap ak istersem np array ierisinde işlem yaptırmalıyım

#numpy mantığı:veri setini al sütunlar feature olsun satırlar item olsun bu şekilde analiz et. ####

import numpy as np
import matplotlib.pyplot as plt
#her matris
a = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
b = np.array([[10], [20], [30]])

c = a + b
print(c)

#matris çarpımı yapmak istersem dot fonksiyonunu kullanmalıyım
a = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
b = np.array([[1], [2], [3]])
c = np.dot(a, b)
print(c)

#broadcasting islemi ile satır satır toplama satır ve sütun uyumuna bakmadan işlem yapılabilir.satırlar işlem yaptırılıyor
a = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
b = np.array([10, 20, 30])
c = a + b
print(c)

#yukarıdaki örneğe benzemesine rağmen farklı bir output oluşturur:sütunlar işleme sokuluyor
a = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
b = np.array([[10], [20], [30]])
c = a + b
print(c)

#linspace fonksiyonu ile grafik çizdirme
import numpy as np
import matplotlib.pyplot as plt
x = np.linspace(-6.28, 6.28, 100) #100'er tane x ve y noktası elde edip grafik çizdireceğim
y = np.sin(x)
plt.plot(x, y) #grafiği shown etme işlemi yapıyorum

#x**2 -4 parabolünü çizdirmek istersem
x = np.linspace(-10, 10, 100)
y = x ** 2 - 4
plt.plot(x, y)

#max fonksiyonu ile en büyük elemana erişmek istersem
import numpy as np
a = np.array([[23, 4, 5], [17, 7, 8], [9, 4, 4]])
result = np.max(a)
print(result) #23 ekran çıktısı oluşuyor

#bir nparrayde ve bir sutunda en büyük değeri bulmak istersem
a = np.array([[23, 4, 5], [17, 7, 8], [9, 15, 4]])
print(a)
print('-----------')
result = np.max(a, axis=0) #sütunlardaki en büyük değerleri buluyor
result2 = np.max(a, axis=1) #satırlardaki en büyük değeri bulmak istersem
print(result)
print(result2)

#sort fonksiyonu:view oluşturmaz
a = np.array([23, 4, 5, 17, 7, 8, 9, 4, 4])
b = np.sort(a) # a yı sort edip yeni bir b nesnesi oluşturuyor
print(b)
print('-' * 10)
a.sort() #a dizisini kendi icinde srt ediyor
print(a)

#satırları da kendi aralarında sort edebilirim
a = np.array([[23, 4, 5], [17, 7, 8], [9, 4, 4]])
b = np.sort(a, axis=1) #satır sorting islemi yaptım
print(b)

#argsort fonksiyonu:indisleri sıraya diziyor sortta ise elemanlar sıraya diziliyordu
a = np.array([23, 4, 5, 17])
b = np.argsort(a)
print(a)
print(b)

#argsort yardımıyla sorting yapma örneği:
a = np.array([23, 4, 5, 17])
b = np.argsort(a)
print(a)
print('-' * 10)
print(a[b])

#argmax fonksiyonu:
a = np.array([23, 4, 50, 17])
b = np.argmax(a)
print(a)
print(b)

#fromiter fonksiyonu:iterable bir nesneyi alıyor nparray elde ediyor np.array fonksiyonu ile  de bu işlem yapılabiliyordu fakat
#np.array fonksiyonuna sadece tuple,list gibi iterable nesneler veriliyor
b = np.fromiter((i * i for i in range(10)), dtype='float32')
print(b)

#asarray fonksiyonu:içeriği aynı kalsın dtype değişsin istersem kullanıyorum typecast işlemi yapmış gibi oluyorum
a = np.array([1, 2.9, 3.2, 4.3], dtype='float32')
b = np.asarray(a, dtype='int32')







