# -*- coding: utf-8 -*-
"""
Created on Sat Feb 13 19:31:32 2021

@author: Dogancan
"""

#Bir dosya uzerinden_client ile haberlesmek icin yazdıgım server kodu  
#dosyadan satır satır okuyor 
#makefile client ile senkron çalışıyor
import socket
import threading

SERVER_PORTNO = 50050

clients = {}

def main():
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM, socket.IPPROTO_TCP) as server_sock:
            server_sock.bind(('', SERVER_PORTNO))
            server_sock.listen(32)
            server_sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
            
            print('waiting for connection....')
            
            while True:
                client_sock, client_addr = server_sock.accept()
                thread = threading.Thread(target=client_thread_proc, args=(client_sock, ))
                
                clients[client_sock] = (client_addr, thread)
               
                thread.start()
                
                print('new client connected (total {} client(s)):'.format(len(clients)))
        
    except Exception as e:
         print(e)
             
def client_thread_proc(sock):
    try:
        f = sock.makefile('r', encoding='UTF-8')
        while True:       
            s = f.readline()[:-1]
            if not s:
                break
            print(s)
    except:
        pass
    
    sock.close()
    del clients[sock]                
    
    print('client disconnected (total {} client(s)):'.format(len(clients)))
 
main()

