#scipy:python üzerine kurulmuş bir kütüphanedir
#scipy ile olasılık hesapları, fourier transform gibi bilimsel işlem yapılır
from scipy.stats import norm
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import linregress

#standart normal dağılımda - sonsuzdan 0 a kadar kalan alanı veriyor
result = norm.cdf(0, loc=0, scale=1)
print(result)

#pdf fonksiyonu kullanımı :ortalaması 0 ve standart sapması 1 olan dağılım örneği
x = np.linspace(-10, 10, 1000)
y = norm.pdf(x)
plt.plot(x, y)
plt.show()

##ppf:cdf nin tersi bizden alanı alıp x değerini veriyor
z = norm.ppf(0.99, loc=0, scale=1)
print(z)

#lineer regresyon yaklaşımı ile eğri çizmek
x = np.array([1, 2, 3, 4, 5, 6])
y = np.array([2, 2.4, 6.7, 9.3, 11.8, 15])

plt.scatter(x, y)
lr = linregress(x, y)
xreg = np.linspace(0, 10, 50)
yreg = lr.slope * xreg + lr.intercept
plt.plot(xreg, yreg, color='red')
plt.show()
result = lr.slope * 4.5 + lr.intercept
print(result)


