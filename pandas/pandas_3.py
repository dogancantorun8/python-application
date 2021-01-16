#read_csv olarak okursam dataframe olarak okurum dosyamı
#iki tırnaklı olanlarda read_csv olarak oku
import pandas as pd
import numpy as np 
import matplotlib.pyplot as plt

btc = pd.read_csv('bitcoin_price.csv', delimiter=',')

date = btc['Date']
max_price = btc['High']
max_price.index = date.values 
max_price = max_price.sort_values(ascending=True)
x = max_price.index
y = max_price.values #numpy series nesnemi arraye çevirdim 
plt.plot(x, y)

eth =  pd.read_csv('ethereum_price.csv', delimiter=',')
eth_date = eth['Date']
eth_max_price = eth['High'][::-1] #ters çevirdim 

#iki series toplanırken indexleri aynı olan toplanır. 
#a ve b toplanmak istenirse eşleşmeyen indexleride toplamak istersem a.add(b,fiil_value=0) yaparsam eşleşmeyenleride toplama getiririm 

import pandas as pd
import numpy as np
btc = pd.read_csv('bitcoin_price.csv', delimiter=',')

btc_date = btc['Date']
btc_max_price = btc['High']
eth =  pd.read_csv('ethereum_price.csv', delimiter=',')
eth_date = eth['Date']
eth_max_price = eth['High']

result = btc_max_price / eth_max_price
result.dropna(inplace=True)
result.plot()


#--------------------------------------- 
import pandas as pd
import numpy as np

btc = pd.read_csv('bitcoin_price.csv', delimiter=',')

btc_date = btc['Date']
btc_max_price = btc['High']

eth =  pd.read_csv('ethereum_price.csv', delimiter=',')
eth_date = eth['Date']
eth_max_price = eth['High']

result = btc_max_price / eth_max_price
result.dropna(inplace=True)

result.index = range(result.size - 1, -1, -1)
result.plot()

#-------------------
import pandas as pd
import numpy as np

alcohol = pd.read_csv('dring2.csv', delimiter=',')
country = alcohol['country']

total_alcohol = alcohol['total_litres_of_pure_alcohol']
total_alcohol.index = country.values

#items ile değerleri ve indexleri dolaşabilirim 
import pandas as pd
import numpy as np
alcohol = pd.read_csv('dring2.csv', delimiter=',')
country = alcohol['country']

total_alcohol = alcohol['total_litres_of_pure_alcohol'].astype('float64')
total_alcohol.index = country.values
for t in total_alcohol.items():
    print(t)

#################mask function :Karmaşık koşullar fonksiyonlar alıp işlem yapabiliriz
#df.mask(lamda s: s=='-','nan')  #ile  - yazan ifadeyi nan ile yer değiştirmiş oldum 
    
    




