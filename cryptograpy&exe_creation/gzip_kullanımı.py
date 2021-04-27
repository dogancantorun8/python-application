# -*- coding: utf-8 -*-
"""
Created on Sun Apr 18 18:36:25 2021

@author: dogancan
"""
#gzip kullanımı 

### 
import gzip
import binascii

text = "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum."

compressed_data = gzip.compress(text.encode('utf-8'))
compressed_data_hex = binascii.hexlify(compressed_data)
print(compressed_data_hex)

decompressed_data = gzip.decompress(compressed_data)
print(decompressed_data.decode('utf-8'))

##
import gzip

with gzip.open('myzip.gzip', 'wb') as z:
    z.write(b'this is a test...')
    z.write(b'Yes this is a test')
    

with gzip.open('myzip.gzip', 'rb') as z:
    b = z.read()
    print(b)
