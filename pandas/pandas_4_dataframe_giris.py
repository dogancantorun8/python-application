# -*- coding: utf-8 -*-
"""
Created on Sat Jan  9 20:42:21 2021

@author: Dogancan Torun
"""


#Dataframe:her sütunu farklı dtypedan oluşan yapılardır. Matrissel bir yapıdır ve sütunların her biri series nesnesidir 
#dataframeler genelde dosyalardan okunur. 
#ndarrayden,iterable nesneden veya herhangi bir datframeden okunup yeni bir dataframe oluşturulabilir 

#1)Liste listesinden dataframe oluşturma
import pandas as pd 
import numpy as np
df = pd.DataFrame([['Ali', 20], ['Veli', 30], ['Selami', 40]], columns=['Adı Soyadı', 'No'],index=['X','Y','Z'])
print(df)

#2)numpy arraylerden dataframe yaparsam
import pandas as pd
import numpy as np
df = pd.DataFrame([['Ali', 20], ['Veli', 30], ['Selami', 40]], columns=['Adı Syoadı', 'No'])
print(df)
df = pd.DataFrame(np.random.randint(0, 100, (10, 3)), columns=['One', 'Two', 'Three'])
print(df)

##numpy dizisinden dataframe örneği 2 : 
import pandas as pd
import numpy as np
df = pd.DataFrame(np.arange(15).reshape(5, 3), columns=['A', 'B', 'C'])
print(df)


##3)sözlükten dataframe yaparsam anahtar olarak kolon ismi balue olarak değerler verilmeli
import pandas as pd
import numpy as np
df = pd.DataFrame([['Ali', 20], ['Veli', 30], ['Selami', 40]], columns=['Adı Soyadı', 'No'], index= ['A', 'B', 'C'])
print(df)
print()
df = pd.DataFrame({'Adı Soyadı': ['Ali Serçe', 'Sacit Hiçyılmaz', 'Kaan Aslan'], 'No': [10, 20, 30]})
print(df)

##4)sözlüklerden oluşan bir sözlüklede dataframe yapılabilir 
import pandas as pd
import numpy as np
df = pd.DataFrame({'A': {'X': 1, 'Y': 2, 'Z': 3}, 'B': {'X': 4, 'Y': 5, 'Z': 6}, 'C': {'X': 7, 'Y': 8, 'Z': 9}})
print(df)

#5)Serileri bir araya getirip dataframe yapabilirim
import pandas as pd
import numpy as np
a = pd.Series([1, 2, 3])
b = pd.Series([4, 5, 6])
c = pd.Series([7, 8, 9])
df = pd.DataFrame({'X': a, 'Y': b, 'Z': c})
print(df)

###5.1)series örneği 2: Bu yöntemde her seriyi sütun değil satırlara sırayla yerleştiriyor .satırsal işlem olmuş
import pandas as pd
import numpy as np
a = pd.Series([1, 2, 3])
b = pd.Series([4, 5, 6])
c = pd.Series([7, 8, 9])
df = pd.DataFrame([a, b, c])
print(df)

###5.2)concat ile  sütunsal birleştirebiliriz :
import pandas as pd
import numpy as np
a = pd.Series([1, 2, 3], name='X')
b = pd.Series([4, 5, 6], name='Y')
c = pd.Series([7, 8, 9], name='Z')
df = pd.concat([a, b, c], axis=1)
print(df) 

##5.3)Boş bir dataframe oluşturup yeni seriesler şeklinde eklenebilir (indexleme ve atama yöntemi) 
import pandas as pd
import numpy as np
a = pd.Series([1, 2, 3])
b = pd.Series([4, 5, 6])
c = pd.Series([7, 8, 9])
df = pd.DataFrame()
df['X'] = a
df['Y'] = b
df['Z'] = c
print(df)

################################################################################################################
#Bir dataframe in belirli bir sutununu series olarak alabilirim ve series methodlarını kullanabilirim
import pandas as pd
import numpy as np
df = pd.DataFrame([['Ali', 20], ['Veli', 30], ['Selami', 40]], columns=['Adı Soyadı', 'No'], index= ['A', 'B', 'C'])
s = df['Adı Soyadı']
k = df['No']
print(s)
print()
print(k)

#dtype değiştirebiliriz tüm numerik ifadelerin dtype float32 olur 
import pandas as pd
import numpy as np
df = pd.DataFrame([['Ali', 20, 100], ['Veli', 30, 200], ['Selami', 40, 300]], columns=['Adı Soyadı', 'No', 'Depth'], index= ['A', 'B', 'C'], dtype='float32')
s = df['Adı Soyadı']
k = df['No']
m = df['Depth']
print(s)
print()
print(k)
print()
print(m) 

