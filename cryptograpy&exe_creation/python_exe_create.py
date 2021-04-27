# -*- coding: utf-8 -*-
"""
Created on Sun Apr 18 16:36:02 2021

@author: dogancan torun
"""

#python programlarının exe hale getirilmesi 
#python exe formatı platform bağımlıdır. farklı işletim sistemlerinde çalışamıyor. 
#import için pyinstaller indirmeliyim proje pathine 
#dizinde pyinstaller --onefile pythondosyası.py yaparak exe yaparız 

#Virtual Enviroment Kavramı : Amacı projede paket versiyonların ayrı bir dizinde tutulması. 
#pip exe ve python exe virtual enviroment içinde yoktur. 
#virtualenv yaratırken proje dizininde pip install virtualenv denmeli ardından "virtualenv myenv" denmeli 
#daha sonra yarattığım myenv içinde Scriptsin icinde "activate yazıp dosyasını çalıştıracağım" 
#virtualenv ile amaç aynı makinada birbirinden bağımsız python ortamı kurmak  
