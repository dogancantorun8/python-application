#csv de date okuma ve split işlemleri
import numpy as np
import datetime


def conv(s):
    k = s.replace(',', '.')
    return float(k)


a = np.loadtxt('şebekeson.csv', delimiter=';', skiprows=2, usecols=(0, 2, 3, 4), converters={2: conv}, encoding='utf-8')
print(a)

#0 lardan oluşan b numparrayine okuduğumu kopyaladım
b = np.zeros((a.shape[0], a.shape[1] + 2))
print(b.shape)

b[:, 0:4] = a[:, :]

a = np.loadtxt('şebekeson.csv', delimiter=';', skiprows=2, usecols=(1), converters={2: conv}, encoding='utf-8',
               dtype='str')

for index, s in enumerate(a):
    d = s[:10].split('.')
    d = '-'.join(d[::-1]) + s[10:]
    dt = datetime.datetime.fromisoformat(d)

    b[index, 4] = dt.date().toordinal()
    b[index, 5] = dt.time().hour * 24 + dt.time().minute

print(b)
