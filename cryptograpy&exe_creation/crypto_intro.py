# -*- coding: utf-8 -*-
"""
Created on Sat Apr 17 18:57:58 2021

@author: dogancan
"""

#cryptografik library 
#büyük bilgiden özet bilgi elde edilmesine hash işlemi denir 
#temel hash fonksiyonu özellikleri : 
    #Kısa bir hash degeri üretmesi 
    #asıl bilgideki değişikliklere adapte olması   
    #hızlı olması 
#bir bilginin doğru iletilip iletilmemesini kontrol etmek için hash bilgisi kullanılır   
#bilgi bozulmuş mu bunun teyidini almak için hash yapısı kullanılır 


import hashlib #çeşitli hash algoritmalarını içeren kütüphane 
print(hashlib.algorithms_guaranteed)
print(hashlib.algorithms_available)


### hash
import hashlib

print(hashlib.algorithms_guaranteed)
print(hashlib.algorithms_available)

print('-------------------------------------')

text = "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum."

sha1 = hashlib.sha1() #hash algoritmasıyla nesneyi yaratıyoruz
sha1.update(text.encode('utf-8')) #byte cinsinden criptografik bilgiyi veriyoruz

hb = sha1.digest() #sha1 ile elde ettiğimiz hashimizi nhb değişkenimize alıyoruz 

ht = sha1.hexdigest() #=>hexadecimal sayıları yazı biçiminde almak için hexdigest diyoruz
print(hb)
print(ht) 

###iki farklı textin hashiinin kıyaslanması: 
import hashlib

print(hashlib.algorithms_guaranteed)
print(hashlib.algorithms_available)

print('-------------------------------------')

text = "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud eiercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla parxatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum."

sha1 = hashlib.sha1()
sha1.update(text.encode('utf-8'))

ht = sha1.hexdigest()
print(ht)

text = "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum."

sha1 = hashlib.sha1()
sha1.update(text.encode('utf-8'))

ht = sha1.hexdigest()
print(ht)