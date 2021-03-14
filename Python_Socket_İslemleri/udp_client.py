# -*- coding: utf-8 -*-
"""
Created on Sun Mar  7 18:47:33 2021

@author: Asus
"""


import socket

SERVER_NAME = '127.0.0.1'
SERVER_PORT = 50050

try:
    with socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM) as client_sock:
        while True:
            msg = input('Bir yazı giriniz:')
            if msg == 'quit':
                break
            b = msg.encode('utf-8')
            client_sock.sendto(b, (SERVER_NAME, SERVER_PORT))
            b, addr = client_sock.recvfrom(1024)
            s = b.decode('utf-8')
            print(f'{addr}: {s}')
            
except Exception as e:
    print(e)

