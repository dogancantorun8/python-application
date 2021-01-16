#pandas:sütunlu veri tablosu oluşturabilmesi,numpydan daha gelişmiş bir kütüphanedir
#pandasta sütunlara series nesneleri deniyor.
#pandasta sütunlar ayrı birer nesnedir, serieslar birleşerek dataframe oluşturur.
#pandas seriese nesneleri nump array şeklinde verilebilirken liste olarakta verilebilir
#series=tek boyutlu vektörlerdir bir araya gelince =>> dataframe oluşur
#numpydan farklı olarak pandasta her sütun elemanı faklı br dtypedadır.

#Kazanımlar: 
#Seri oluşturma 
#İndex kavramı 
#Size özniteliği 
#Name özniteliği 
#Sıra numarasıyla indexleme  ve dilimleme
#Label ile indexleme ve dilimleme

#pandas series nesnesi tanımını liste şeklinde veriyorum
import pandas as pd
import numpy as np
s = pd.Series([10, 20, 30, 40, 50])
print(s)

#pandas series nesnesi tanımını np.array şeklinde veriyorum
a = np.array([10, 20, 30, 40, 50], dtype='float32')
s = pd.Series(a)
print(type(s))
print(s)
print()
#series nesneleri indexlere sahiptir.İndexler farklı tiplerden olabilirler elemana erişimi indexler kolaylaştırır.
#string tipinde index tanımı
a = np.array([10, 20, 30, 40, 50], dtype='float32')
s = pd.Series(a, dtype='float64', index=['Ali', 'Veli', 'Selami', 'Ayşe', 'Fatma'])
print(s)
print()

#bir csv dosyasını loadtxt ile okuyup np seriese atama yaparsam
a = np.loadtxt('dring.csv', delimiter=',', dtype='str', encoding='utf-8', skiprows=1)
beer_servings = a[:, 1].astype('float32') #dtype float32 ye çevirdim
s = pd.Series(beer_servings)
print(s)

#bir csv dosyasını loadtxt ile okuyup indexini ilk sütunu yapmak istersem
import pandas as pd
import numpy as np
drings = np.loadtxt('dring.csv', delimiter=',', dtype='str', encoding='utf-8', skiprows=1)
beer_servings = drings[:, 1].astype('float32')
s = pd.Series(beer_servings, index=drings[:, 0],name='Beer Servings') #name parametresi ile dataframe'e isim verdim 
#s.index=index=drings[:,0] şeklindede atama yapılabilir
print(s)

#############pandas series ile ilgili methodlar ################################ 
#s.size() ve len(s) =>>> kaç tane kayıt olduğunu görürüm 
#s.tail => sondan 5 kayıt  listele
#s.head => baştan 5 kayıt s.head(10)= bastan 10 kayıt görmek istersem  
#s.index[3] diyerek indexlerimin 3.elemanına erişebilirim 
#s[5] diyerek seriesin 5. elemanına ulaşabilirim 
#Dilimlemek istersem s[3:10] derse 3.elemandan 10.elemana kadar erişebilirim 
#s[3:10:2] dersem 2'şer arttırarak dilimlerim 
#indexi veripte elemana ulaşabilirim s['argentina'] dersem indexi argentina olan elemana erişirim  
#s['algeria':'bolivia] dersem algeria indexinden bolivia indexine kadar dilimlerim  
#s.algeria dersem labeli örnek özniteliğiymiş gibi çağırabilirim  
#s.values dersem series nesnelerini numpy dizisi şeklinde alabilirim
#series methodları pandasta işlem yapabilmek için kritik

