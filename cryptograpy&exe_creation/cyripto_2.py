# -*- coding: utf-8 -*-
"""
Created on Sun Apr 18 16:10:30 2021

@author: dogancan torun
"""

#hmac kullanımı 
import hmac

text = "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud eiercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla parxatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum."


hm = hmac.new(b'mavi ay', digestmod='sha1') #mavi ay bizim password
hm.update(text.encode('utf-8'))

bd = hm.digest()
td = hm.hexdigest()
print(td)

# doküman ve digest (hash) karşı atafa iletiliyor 
# aşağıdaki kod karşı tarafın kodu 

text_other_side = text.encode('utf-8') #karsı tarafa iletilmiş yazı 
bd_other_side = bd #karşı tarafa iletilmiş hash 

#alıcı taraf 
hm_other_side = hmac.new(b'mavi ay', digestmod='sha1')
hm_other_side.update(text_other_side)

bd_new_other_side = hm_other_side.digest()
td_other_side = hm_other_side.hexdigest()
print(td_other_side)

print('Değişmemiş' if bd_other_side == bd_new_other_side else 'değişmiş') #iki trafın digest değerini kıyaslıyor 
