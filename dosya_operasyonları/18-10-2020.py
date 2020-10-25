# -*- coding: utf-8 -*-
"""
Created on Sun Oct 18 17:01:52 2020

@author: Dogancan Torun
"""


#Subject:Dosya islemleri

#sonu jpg olan dosyaları bulma kodum   
#listdir hepsini listeliyor
import os 
for ent in sorted(os.listdir('.'),reverse=True):
    if ent.lower().endswith('.jpg'):
        print(ent)

#walkdir tüm dosyayı dolaşır her dolaşmada 3 lü tuple veriyor 
#dizin-dizin dolaşıp o dizin içindeki dizin ve dosya isimlerini veriyor 

#2 iterasyon gerçekleştirdi
for dirname,dirs,files in os.walk('ali') :
    print(dirname,dirs,files)
    for file in files: #dosyalarıda yazdırdım
        print(file)


#tersten dolaşarak manuel dosya silme 
import os
def remove_tree(dirpath):
    for dirname, dirs, files in os.walk(dirpath, topdown=False):
        for file in files:
           os.remove(dirname + '\\' + file)
            
        for dir in dirs:
            os.rmdir(dirname + '\\' + dir)
    
    os.rmdir(dirpath)
            
remove_tree(r'F:\Dropbox\Kurslar\Python-App\Src\ali')

#os.stat fonksiyonu ile dosya üzerindeki tüm haraketleri görebiliyoruz 
#stat fonksiyonu bana sınıf olarak geri dönüş yapar 
import os  
import time
result=os.stat(r'C:\Users\Asus\Desktop\18-10-2020\dogan.txt') 
print(time.ctime(result.st_size)) 
print(time.ctime(result.st_atime)) 
print(time.ctime(result.st_mtime)) 

#scandir ile bir directorydeki file ve directoryleri buluyorum 
import os
import time

for de in os.scandir('.'):
    print(de.name, 'Directory' if de.is_dir() else 'File')
    s = de.stat()
    print(s.st_size)
#1000 byten buyuk dosyaları bulmak istersem 
import os
import time

for de in os.scandir('.'):
    if not de.is_file():
        continue
    s = de.stat()
    if s.st_size > 1000:
        print(de.name, s.st_size)
