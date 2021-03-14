# -*- coding: utf-8 -*-
"""
Created on Sun Feb 14 17:12:58 2021

@author: Dogancan Torun
"""

import socket

SERVER_NAME = '127.0.0.1'
SERVER_PORT = 50050

class Client:
    def __init__(self, server_name, server_port):
        self.server_name = server_name
        self.server_port = server_port
        
    def run(self):
        try:
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_sock:
                client_sock.connect((self.server_name, self.server_port))
                print('Connected...')
                #yazma ve okuma socketi olmak uzere iki socket acıyorum 
                fr_sock = client_sock.makefile('r', encoding='UTF-8')
                fw_sock = client_sock.makefile('w', encoding='UTF-8')
                                
                while True:
                    cmd = input('CALC>').strip()
                    if cmd == 'quit':
                        break
                    #yazıyı servera bir satır olarak ekliyor
                    fw_sock.write(cmd + '\n')
                    fw_sock.flush()
                    response = fr_sock.readline()
                    if not response:
                        break
                    print(response)  
                #disconnect yazarsam client bagantısı kesiliyor
                fw_sock.write('DISCONNECT\n')  
                fw_sock.flush()
                
                client_sock.shutdown(socket.SHUT_RDWR)
                        
        except Exception as e:
            print(e)
            
            
client = Client(SERVER_NAME, SERVER_PORT)
client.run()
