#csv dosyası okurken numpy dizisi şeklinde okumalıyım
#numpy.loadtxt ile csv dosyasını okuyabiliriz


import numpy as np
import datetime
import matplotlib.pyplot as plt

#usecols: parametresiyle okuyacağımız sütunları veriyoruz
#csv nin başlığından kurtulmak istiyorsam(özelliklerin açıklandığı satırlar vs.) skiprows parametresinde belirtmeliyim
#dtype:object olursa hepsini string şeklinde okurum
#converters parametresi:Sözlük içerisinde  anahtar olarak verdiğimiz değerler sütunlar

#2.sütunu datetime ile tarihi okumak için lambda fonksiyonunu yazdık
a = np.loadtxt('rossman-train.csv', delimiter=',', skiprows=1, usecols=(0, 1, 3, 4, 5, 6, 7), converters={7: lambda s: float(s[1]), 8: lambda s: float(s[1]), 2: lambda s: datetime.datetime.fromisoformat(str(s)[2:12]).timestamp()}, max_rows=100,encoding='utf-8')
#print(a)








