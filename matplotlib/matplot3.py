# -*- coding: utf-8 -*-
"""
Created on Sun Jan 17 17:12:38 2021

@author: Dogancan Torun
"""


#birden fazla veri setinin histogramını çizmek istersem :
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv(r'Covid-19-Datasets\covid_19_data.csv')
x = np.random.randn(2000).reshape(1000, 2)
plt.title('Normal Random Numbers Histogram', fontsize=15)
plt.xlabel('x', fontsize=12)
plt.ylabel('frequency', fontsize=12)
plt.xticks(np.arange(-10, 10, 0.5))
plt.hist(x, bins=20, color=['green', 'blue'])


#histogram grafik özelliklerinden edge colour kullanırsam
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv(r'Covid-19-Datasets\covid_19_data.csv')
x = np.random.randn(2000)
plt.title('Normal Random Numbers Histogram', fontsize=15)
plt.xlabel('x', fontsize=12)
plt.ylabel('frequency', fontsize=12)
plt.xticks(np.arange(-10, 10, 0.5))
plt.hist(x, rwidth=1, edgecolor='red', color='yellow')

#pasta grafiği çizimi 
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
x = [360, 500, 180, 900, 1300]
labels = ['XRP', 'BTC', 'Avax', 'NEO', 'BTG']
plt.pie(x, labels=labels)

#pastanın renklerini değişmek istersem 
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
#df = pd.read_csv(r'Covid-19-Datasets\covid_19_data.csv')
x = [360, 500, 180, 900, 1300]
labels = ['XRP', 'BTC', 'Avax', 'NEO', 'BTG']
plt.pie(x, labels=labels, colors=['red', 'green', 'blue', 'yellow', 'magenta'])

#pasta grafiğinde explode methodu ile istediğimiz dilimi pastadan koparabiliriz 
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
#df = pd.read_csv(r'Covid-19-Datasets\covid_19_data.csv')
x = [360, 500, 180, 900, 1300]
labels = ['XRP', 'BTC', 'Avax', 'NEO', 'BTG']
plt.pie(x, labels=labels, colors=['red', 'green', 'blue', 'yellow', 'magenta'], explode=[0.1, 0, 0, 0, 0])

#pasta dilimlerin üzerinde yüzdeler olsun istersem autopct kullanabilirim
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
x = [664812242762, 141428512203, 24330211680, 15364089757, 12576793068]
labels = ['BTC', 'ETH', 'USDT', 'DOT', 'XRP']
plt.pie(x, labels=labels, explode=[0, 0, 0, 0, 0], autopct='%%%.0f')

#pastanın yarıçapını değiştirip grafiği büyütebilirim :matplotta birimler pixel değil inç cinsindedendir
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
x = [664812242762, 141428512203, 24330211680, 15364089757, 12576793068]
labels = ['BTC', 'ETH', 'USDT', 'DOT', 'XRP']
plt.pie(x, labels=labels, explode=[0, 0, 0, 0, 0], autopct='%%%.0f',radius=2)

#bir figure boyutunu inç cinsinden değiştirebiliriz 
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
x = [664812242762, 141428512203, 24330211680, 15364089757, 12576793068]
labels = ['BTC', 'ETH', 'USDT', 'DOT', 'XRP']
plt.figure(figsize=(10, 10)) #figure parametresiyle config yaptım
plt.pie(x, labels=labels, explode=[0, 0, 0, 0, 0], autopct='%%%.0f')














