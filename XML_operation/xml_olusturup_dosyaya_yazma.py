# -*- coding: utf-8 -*-
"""
Created on Sat Apr 17 18:07:22 2021

@author: dogancan 
"""

##xmlden bir dosyayı okuyup başka bir dosyaya yazmak istersek; 
import xml.etree.ElementTree as ET

et = ET.parse('sample.xml')
root = et.getroot()
ET.dump(root)
print('-----------------------------------')
root.set('test', '150')
ET.dump(root)
print('-----------------------------------')

et.write('sample2.xml') #yeni bir dosyaya yazıyoruz. 

