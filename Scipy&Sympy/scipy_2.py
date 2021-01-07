
#scipy ile  belirli integral almak
import numpy as np
from scipy.integrate import quad

def f(x): return x **2 - 4

result = quad(f, -4, 4)
print(result)

#olasılık yoğunluk fonksiyonu:eğri altında kalan alan
from scipy.integrate import quad
def f(x, mu, sd):
    return 1 / (sd * np.sqrt(2 * np.pi)) * np.e ** (- 0.5 * ((x - mu) / sd) ** 2)


result = quad(f, -np.inf, np.inf, args=(0, 1))
print(result)

#trapez yöntemiyle integral almak istersem
from scipy.integrate import trapz
def f(x, mu, sd):
    return 1 / (sd * np.sqrt(2 * np.pi)) * np.e ** (- 0.5 * ((x - mu) / sd) ** 2)

x = np.linspace(-10, 10, 100)
y = f(x, 0, 1)
result = trapz(y, x)
print(result)

#enterpolasyon:doğru yada eğriye uydurup kestirimde bulunmak
from scipy.interpolate import interp1d
import matplotlib.pyplot as plt
x = np.array([1, 2, 3, 4, 5])
y = np.array([2.4, 5.6, 5.8, 9.9, 12.3])
plt.scatter(x, y)
f = interp1d(x, y,kind='linear')
result = f(3.5)
print(result)

##enterpolasyon ikinci örneği
from scipy.interpolate import interp1d
x = np.array([1, 2, 3, 4, 5])
y = np.array([2.4, 5.6, 5.8, 9.9, 12.3])
import matplotlib.pyplot as plt
plt.scatter(x, y)
f = interp1d(x, y, kind='quadratic') #quadratic bir enterpolasyon yaptım
xnew = np.linspace(1, 5, 30)
ynew = f(xnew)
plt.plot(xnew, ynew, color='red')
plt.show()

#sinüs eğrisine quadratic enterpolasyon uyguladım
from scipy.interpolate import interp1d
x = np.linspace(-2 * np.pi, 2 * np.pi, 10)
y = np.sin(x)
import matplotlib.pyplot as plt
plt.scatter(x, y) #saçılma diyagramı
f = interp1d(x, y, kind='linear')
xnew = np.linspace(-2 * np.pi, 2 * np.pi, 100)
ynew = f(xnew)
plt.plot(xnew, ynew, color='red')
plt.show()
