#numpyda lineer cebir işlemleri

#dot fonksiynu matris çarpımının yanında birçok özelliğe sahiptir.
import numpy as np
a = np.array([2, 5, 6])
b = np.array([3, 4, 2])
c = np.dot(a, b) #çarpıp toplama işlemi yapacak
print(c)

##satır ve sütun vektörü tanımlayarak dot fonksiyonu kullanımı
a = np.array([[2, 5, 6], [1, 2, 3], [4, 5, 6]])
b = np.array([3, 4, 2])
c = np.dot(a, b)
print(c)
print('-' * 10)
b = np.array([[3], [4], [2]]) #sütun vektörü tanımı yapıp carpma işlemi yaptım
c = np.dot(a, b)
print(c)

#matris tersi alma işlemi:inverse operatörü linalg kütüphanesinin inv işlemini kullanıyorum
a = np.array([[2, 5, 6], [1, 2, 3], [4, 5, 6]])
b = np.linalg.inv(a)
print(b)

#matris tersi yöntemini kullanarak 3 bilinmeyenli denklem çözümü
a = np.array([[2, -1, 3], [1, 1, 1], [-1, 2, 1]], dtype='float64')
b = np.array([4, 6, 5]).reshape(-1, 1) #katsayı matrisini sütun vektörü olarak oluşturuyorum
a_inverse = np.linalg.inv(a)
x = np.dot(a_inverse, b)
print(x)

#solve fonkisyonu ile ters vs kullanmadan direk sonuca ulaşıyoruz
a = np.array([[2, -1, 3], [1, 1, 1], [-1, 2, 1]], dtype='float64')
b = np.array([4, 6, 5]).reshape(-1, 1) #satır vektörü yada boyutsuz da verebiliyoruz
x = np.linalg.solve(a, b)
print(x)

#rand fonksiyonu ile 5X10 luk dizi elde etme
a = np.random.randint(0, 100, (5, 10))
print(a)

#random 5 er sütundan oluşan dizimi görselleştirmek istersem
a = np.random.randint(0, 100000, (2000, 5)) #randint ile int değerler ürettim
result = np.mean(a, axis=1)  #satırların ortalamasını  buluyor
import matplotlib.pyplot as plt
plt.hist(result, bins=20) #bins parametresiyle örneklemi arttırıyorum
plt.show()

#random.random kullanarak 0 ie 1 arasında değerler üretiyorum
a = np.random.random((10, 10))
print(a)

####random bir dizinin birim çember içinde alanını buluyorum
n = int(input('n değerini giriniz:'))
points = np.random.random((n, 2)) #1 ve 0 lardan oluşan 2 indisli random dizi oluşturuyorum
insides = np.sum(np.sqrt(points[:, 0] ** 2 + points[:, 1] ** 2) < 1)
pi = 4 * insides / n
print(pi)

#histogram oluşturma
a = np.random.randn(10000)
plt.hist(a)
plt.show()

#permutation:rastgele sıraya dizmek istersem
a = np.random.permutation(10)
print(a)


