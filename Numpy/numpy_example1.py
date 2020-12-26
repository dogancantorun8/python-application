#standart sapma islemini numpy ile atma
import numpy as np
a = [3, 4, 7, 3, 2, 4, 1]
a = np.array(a)
#burada a üzerinde yapılan np islemleri vektörel işlemler olduğundan her elemana tek tek yapılıyor
std = np.sqrt(np.sum((a - np.mean(a)) ** 2)) / a.shape[0]
print(std)

#rastgele nd array yaratmak istersem
x = np.ndarray((3, 2), dtype='float32')
print(x)

