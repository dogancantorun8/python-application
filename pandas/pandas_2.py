
#Kazanımlar:Series methodlarım ;
#value methodu 
#isna()  isnull() 
#sum() 
#count()
#shape()
#fillna(x)  
#dropna()  
#s.std() =>standart sapma
#s.var() => varyans alıyor
#s.median() => medyanı verir 
#mode() => serinin modunu verir 
#unique() => serinin unique değerlerini veriyor 
#pop() => belirli bir indexi silmek için kullanır  
#hist() => değerlerin olasılık yoğunluk fonk çizilir 
#describe() => bu method ile serinin özelliklerini bulup istediğimi çekebilirim 
#nsmallest() => en küçük n tane değeri verir
#nlargerst() => en büyük n tane değeri verir 
#sortvalue() ve sortindex() ile sort işlemini yapabiliriz  
#cumsum() ile toplayarak kümülatif olarak elemanları toplar  
#nesneadi.filter(regex='^tur') istediğim kriterde  getirebilirim 
#idmax() ve idmin() ile en büyük veya en küçük elemanın indexine ulaşabiliriz 
#todict ile değerleri sözlüğe cast edebiliriz 
#tolist() ile değerleri listeye cast edebiliriz   
#toexcel() yaparsam excele çeviririm datalarımı 
#to_csv() yaparsam istediğim veriyi csv kaydederim  



#######s.loc ve s.iloc tanımları ile indexleme  
#s.loc=sadece label indexlemede kullanılır 
#s.iloc=sırasal klasik indexlemede kullanılıyor => numara ile indexlemede kullanılıyor.
#s[] şeklinde yaparsam loc ve iloc ile yapılanların ikisinide yapabilirim 

import numpy as np
import pandas as pd
drings = np.loadtxt('dring.csv', delimiter=',', dtype='str', encoding='utf-8', skiprows=1)
beer_servings = drings[:, 1].astype('float32')
s = pd.Series(beer_servings, index=drings[:, 0],name='Beer Servings') #name parametresi ile dataframe'e isim verdim 
#s.index=index=drings[:,0] şeklinde de atama yapılabilir

#print(s) 
#print(s[s>100]) #100 den büyük değerleri getirmek istersem 
print(s[s>100].index) #100 den büyük olan elemanların indexlerine erişmek istersem

#shape fonksiyonu s.shape =>> tek boyutlu oluyor s.sizean farkı yok 

###Bir series nesnesini bir skaler ile işleme sokarsam hereleman üzerinde işlem yapılır s=s+2 dersem her elemana  2 eklenir 
#seriesler tek boyutludur bunu asla atlamamalıyım 


#isna() fonksiyonu:s.isna() =>> boş olan değerlerde true ,dolu değerlerde false dönüyor benzeri isnull() methodudur bu methodların tersi notnull dir 
#s.sum() ile tüm serie elemanlarını toplarım 
#s.count() bu method ile seri içindeki none olmayan elemanların sayısını buluruz
#s[s.isnull()] => bu method ile nan olanları çekebilirim 
#s.fillna(100) =>na değerlerini 100 ile doldurmak istersem kullanırım, s.fillna(s.mean()) dersem na lar ortalama ile dolar
#s.dropna() => nan olan elemanlardan kurtulmak için kullanılır
#iki series nesnesi toplanırken aynı index isimleri toplanır farklı indexler için none yazılır 
