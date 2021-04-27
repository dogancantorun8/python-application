# -*- coding: utf-8 -*-
"""
Created on Thu Apr 15 13:10:49 2021

@author: dogancan torun
"""

#getitem,setitem,iter ,find finall ile xml

#1)basic parse operation
import xml.etree.ElementTree as ET

et = ET.parse('sample.xml') #dosya adını veriyoruz
root = et.getroot() #element  tree 

print(root.tag)
print(root.attrib) #xmle ait elemanları alıyoruz
print(root.get('a')) #spesifik bir elemanı alabiliyoruz

####2)contenti almak istersem;  
import xml.etree.ElementTree as ET

et = ET.parse('test.xml')
root = et.getroot()

print(root.tag)
print(root.attrib)
print(root.get('no'))
print(repr(root.text))
print('---------------')

    #content içeriğini represent ile yazdırırsam 
for text in root.itertext(): #iteratör (tüm contentleri sub elemanlarla beraber almak istersek kullanıyoruz)
    print(repr(text)) 

##3)Alt elemanlarını elde etmek istersek : 
import xml.etree.ElementTree as ET

et = ET.parse('test.xml') #tree elde ediyorum
root = et.getroot() #roota ilişkin element nesnesi elde ediyorum

print(root.tag)
print(root.attrib) #sözlük olarak attributeları alıyorum 
print(root.get('no')) #spesifik bir elemanı almak istersem 
print('---------------')

for e in root.iter():#bunun içine root.iter('class'): dersem spesifik bir elemanın taglerini alabiliyorum
    print(e.tag) #tagi itere sokarsak tüm alt taglerini dolaşabiliyoruz.

print('---------------')

for i in range(len(root)):
    e = root[i] #sub elemanları alabiliyoruz 
    print(e.tag, e.text) #child elemanlarında contentlerini elde etmek istersem

##alt elemanların spesifik özelliklerini parse etmek istersem 
#iter komutu tüm ağacı tarar. 
#spesifik özellikleri ararken find komutu kullanılır. 
#findall alt ağaçtaki tüm elemanları buluyor. 
import xml.etree.ElementTree as ET

et = ET.parse('sample.xml')
root = et.getroot()

print(root.tag)
print(root.attrib)
print(root.get('no'))
print('---------------')

for e in root.iter():
    print(e.tag)
    
print('-----------------------------------')

for food in root.iter('food'):
    name = food.find('name')
    price = food.find('price')
    
    print(name.text, price.text)
    
print('-----------------------------------')

for food in root.iter('food'):
    name = food.find('name')
    print(name.text, ':', sep='', end= ' ')
    print(*[price.text for price in food.findall('price')], sep=', ')
    