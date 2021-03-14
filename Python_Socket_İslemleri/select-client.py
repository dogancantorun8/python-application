# -*- coding: utf-8 -*-
"""
Created on Sat Feb 20 19:19:48 2021

@author: Asus
"""

import socket

SERVER_PORT = 50050
SERVER_NAME = 'localhost'

try:
    with socket.socket(family=socket.AF_INET, type=socket.SOCK_STREAM, proto=socket.IPPROTO_TCP) as client_sock:
        client_sock.connect((SERVER_NAME, SERVER_PORT))
        print('Connnected...')

        while True:
            text = input('Enter text:')
            b = text.encode('UTF-8') 
            client_sock.send(b)

            if text == 'quit':
                break

            b = client_sock.recv(1024)
            text = b.decode('UTF-8') 
            print(text)
        client_sock.shutdown(socket.SHUT_RDWR)

except Exception as e:
    print(e)
