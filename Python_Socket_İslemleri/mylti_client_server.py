# -*- coding: utf-8 -*-
"""
Created on Sat Feb 13 17:31:10 2021

@author: Dogancan Torun
"""

#multiclient server islemleri için IO Modelleri kullanılır
#Select-Paul Modeli=>windows ,unix 
#Thread modeli 

#multi client connection:Birden fazla client bağlansın istersem; 
import socket
import threading

SERVER_PORTNO = 50050

clients = {} #anahtar:Socket value:socket adresi yani baglanan clientin ip si gibi dusunebiliriz
lock = threading.Lock()

def main():
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM, socket.IPPROTO_TCP) as server_sock:
            server_sock.bind(('', SERVER_PORTNO))
            server_sock.listen(32)#isletim sistemini aktif finleme moduna sokuyor
            
            print('waiting for connection....')
            
            while True:
                client_sock, client_addr = server_sock.accept()
                #accept olduktan sonra thread olusturuyor
                thread = threading.Thread(target=client_thread_proc, args=(client_sock, ))
                
                #lock ile saglıklı calısma icin yazdım bu kısmı tam cozemedim 
                lock.acquire()
                clients[client_sock] = (client_addr, thread)
                lock.release()
                
                thread.start()
                
                print('new client connected (total {} client(s)):'.format(len(clients)))
        
    except Exception as e:
         print(e)
             

#aynı kod farklı clientlar konuşuyor her client baglandıhında yeni bir thread olusuyor          
def client_thread_proc(sock):
    while True:       
        b = sock.recv(1024)
        text = b.decode('UTF-8')
        if text == 'quit':
            break
        sock.send(text[::-1].encode('UTF-8'))    
    lock.acquire()
    del clients[sock]            
    lock.release()
    
    print('client disconnected (total {} client(s)):'.format(len(clients)))
     
main()
