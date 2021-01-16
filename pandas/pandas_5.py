# -*- coding: utf-8 -*-
"""
Created on Sun Jan 10 17:50:04 2021

@author: Dogancan Torun
"""


import pandas as pd
import numpy as np
    
df = pd.read_csv(r'CoinDatasets\ripple_price.csv')
    
print(df)

#Dataframe indexlenmesi  :
#1)Sütunsal indexleyebilirim ve sütun indexini verip çağırabilirim 

#2)dataframe iloc-loc ile indexlenirse satırın tamamı elde edilir 
#2.1)df.iloc yaparsam tek bir satırı elde edersem series olur,bir grup satırı elde etmek istersem dataframe olur.[Satırlar için iloc kullan,satırın numarasıyla işlem yapar] 
        #df.iloc[5:7] :Data frame alır 
        #df.iloc[5] :series olarak alır  
        #df.iloc[[1,2]]=1 ve 2.satırları alırım 

    #--------------------------
import pandas as pd
import numpy as np
df = pd.read_csv(r'CoinDatasets\ripple_price.csv')
result = df.iloc[10:20]
print(result)


#2.2)df.loc yaparsam tek bir satırı elde edersem series olur,bir grup satırı elde etmek istersem dataframe olur.[index isimleriyle ele geçiriyorum] 
    #df.loc['A'] = label ismini verdim ve eriştim
    
#3)Dataframe nesnesi ile indexleme: Sütunları ele geçiririm bu yöntemle :Sütun ismini ele geçirip işlem yapar
#tek sütun ele geçirilirse series çok sütun ele geçirilirse dataframe olur
    #--------------------------
import pandas as pd
import numpy as np
df = pd.read_csv(r'CoinDatasets\ripple_price.csv')
result = df[['Date', 'Open', 'Close']]
print(result)

#bir satırda herhangi bir kriter uygulamak isterm: 
import pandas as pd
import numpy as np
df = pd.read_csv(r'CoinDatasets\ripple_price.csv')
result = df.iloc[(df['Open'] > 2).values] #open columnda 2 den büyük olanları getirdim
print(result)

#iloc kullanmadan dataframe indexlemesiyle koşul belirtme 
import pandas as pd
import numpy as np
df = pd.read_csv(r'CoinDatasets\ripple_price.csv')
result = df[df['Open'] > 2]
print(result)

#Dataframe den satır ve sütun silme :satırda axis=0 ,sütun silersem axis=1 yazacağım df.drop() fonksiyonu içerisine 
import pandas as pd
import numpy as np
df = pd.DataFrame([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]], columns=['X', 'Y', 'Z'])
result = df.drop('X', axis=1) 
print(result)

#birden fazla sütun silmek istersem liste halinde vereceğim :result = df.drop(['X', 'Y'], axis=1)
#satır silmek istersem aşağıdaki gibi yapabilirim 
import pandas as pd
import numpy as np
df = pd.DataFrame([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]], columns=['X', 'Y', 'Z'])
print(df)
print()
result = df.drop(2) #2.satırı sildim esas nesnemde bir değişiklik yok result nesnemde değişiklik oldu
print(result)

#Dataframe insert yapmak istersem 
import pandas as pd
import numpy as np
df = pd.DataFrame({'X': [1, 2, 3], 'Y': [4, 5, 6], 'Z': [7, 8, 9]}, index=['A', 'B', 'C'])
print(df)
print()
df['K'] = [10, 20, 30] #K sütununu insert ettim df['K']=100 dersem tüm elemanlar 100 oluyor
print(df)

#2.yol insert etme yöntemi 
import pandas as pd
import numpy as np
df = pd.DataFrame({'X': [1, 2, 3], 'Y': [4, 5, 6], 'Z': [7, 8, 9]})
print(df)
print()
df.insert(2, 'K', [10, 20, 30])  #df.insert(3, 'K', [10, 20, 30]) = 3 yaparsam K 3.sütuna geliyor
print(df)

#eğer series veriyorsam indexlerim uyuşmalı 
import pandas as pd
import numpy as np
df = pd.DataFrame({'X': [1, 2, 3], 'Y': [4, 5, 6], 'Z': [7, 8, 9]}, index=['A', 'B', 'C'])
print(df)
print()
s = pd.Series([10, 20, 30], index=['A', 'B', 'C'])
df.insert(3, 'K', s)
print(df)

#dropna: na olan tüm satırları atıyor
import pandas as pd
import numpy as np
df = pd.DataFrame({'X': [1, None, 3], 'Y': [4, 5, 6], 'Z': [7, 8, None]}, index=['A', 'B', 'C'])
print(df)
print()
result = df.dropna()
print(result)

#açılış fiyatı sütununda  ortalamadan büyük olanları bulmak istersem: 
import pandas as pd
import numpy as np
df = pd.read_csv(r'CoinDatasets\ripple_price.csv')
result = df[df['Open'] > df['Open'].mean()]
print(result)

#iki sutunun ortalamasını almak istersem 
import pandas as pd
import numpy as np
df = pd.read_csv(r'CoinDatasets\ripple_price.csv')
result = df[['Open', 'Close']].mean(axis=0)
print(result)

#Not:dataframede transpoz vb işlemler yapmak istersek numpy arraye dönüp(cast edip) işlem yapabiliriz  

#dataframe iterate edersem: 
import pandas as pd
import numpy as np
df = pd.DataFrame(np.arange(15).reshape(5, 3), index=list('ABCDE'), columns=list('XYZ'))
print(df) 
print()
for col, row in df.items(): #her dolaşımda items fonksiyonu bize bir tuple verir.
    print(row)

#dataframe iterrows ile iterate etmek :burada iterate ederken satırlara erişirim 
import pandas as pd
import numpy as np
df = pd.DataFrame(np.arange(15).reshape(5, 3), index=list('ABCDE'), columns=list('XYZ'))

for t in df.iterrows():
    print(t)

#pandasın herhangi bir sutunununda datetime methodu ile date formatına cast edebilirim 
import pandas as pd
import numpy as np
df = pd.read_csv(r'CoinDatasets\ripple_price.csv')
result = df[['Open', 'Close']].mean(axis=0) 
result=pd.to_datetime(df['Open']) #datetime pandasın bir fonksiyonu
print(result)

#herhangi bir df üzerinde bir sütunu stringe çevirmek istersem 
import pandas as pd
import numpy as np
df = pd.read_csv(r'CoinDatasets\ripple_price.csv') 
#volume sütunlarında virgüllerden kurtuldum
df = df[df['Volume'].str.find('-') != 0] #find fonksiyonu boolen dönüyor eğer 0 olursa istedğimiz işlemi preprocess yapıyoruz
#string operasyonları yapabilirim replace gibi ardından astype ile tekrardan float32 formata çevirdim 
#volume ve marketcap sütunlarında işlem yaptım 

df['Volume'] = df['Volume'].str.replace(',', '').astype('float32')
df['Market Cap'] = df['Market Cap'].str.replace(',', '').astype('float32')
print(df)

#5.kolon üzerinde bir lambda fonksiyonuyla işlem yaptım
import pandas as pd
import numpy as np
df = pd.read_csv(r'CoinDatasets\ripple_price.csv', converters= {5: lambda s: None if s == '-' else s}) 
df.dropna(axis=0, inplace=True) #dropna ile noneolan satırları atıyorum 
df['Volume'] = df['Volume'].str.replace(',', '').astype('float32') # df['Volume'].str dedikten sonra yeni bir sınıf elde ediyorum bu bilinen stringden farklı pandasın string fonksiyonları0000
df['Market Cap'] = df['Market Cap'].str.replace(',', '').astype('float32')
print(df)

#bir dataframede axis=0 ile satırlar üzerinde axis=1  dersek sütunlar üzerinde işlem yapabiliriz
#df.iloc(5) dersem 5.satıra erişirim.df in iloc fonksiyonunda satırlarla işlem yapabilirim
#dataframe in tek bir indexi olur ve o da satırlar içindir.
#df['item-3' : 'item-5'] =>> bu şekilde yaparsam 3.satır ve 5.satır arasındaki değerleri getirir.

#df.iloc[3,5] => 3.satır 5.spesifik elemana erişirim
#df.loc['item-3','Open'] =>3.satırın open olan sütunu gelsin istersem yazarım






