# -*- coding: utf-8 -*-
"""
Created on Sat Feb 13 19:34:39 2021

@author: Dogancan
"""


#dosya uzerinden okuma saglayan clientim   
#makefile server kodu ile senkron calisiyor

import socket

SERVER_PORTNO = 50050
SERVER_NAME = '127.0.0.1'

try:
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_sock:
        client_sock.connect((SERVER_NAME, SERVER_PORTNO))
        print('connected...')
        
        f = client_sock.makefile('w', encoding='UTF-8')
        while True:
            text = input('Bir yazı giriniz:')
            f.write(text + '\n') 
            f.flush()
            
        client_sock.shutdown(socket.SHUT_RDWR)
                        
except Exception as e:
    print(e)