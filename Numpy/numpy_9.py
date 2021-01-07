#csv dosyamı string olarak almak istersem ve string operasyonları yaparsam
#buradsa np array üzerinde string işlemleri yapıyorum

import numpy as np
import datetime

a = np.loadtxt('rossman-train.csv', skiprows=1, max_rows=100, dtype='str', delimiter=',')
print(a)

b = np.zeros_like(a, dtype='float32')
b[:, 0] = a[:, 0].astype('float32')

b[:, 1] = a[:, 1].astype('float32')

b[:, 7] = np.char.strip(a[:, 7], '"').astype('float32')
b[:, 8] = np.char.strip(a[:, 8], '"').astype('float32')
print(b)



