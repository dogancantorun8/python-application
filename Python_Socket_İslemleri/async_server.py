# -*- coding: utf-8 -*-
"""
Created on Sat Feb 20 17:14:13 2021

@author:Doğancan
"""

#asyncio server modeli:loop adında bir global nesne alıp accepted await ile alıyoruz ve bir sonrakine geçiyoruz 
#main fonksiyonumuzu loop nesnemiz içerisine veriyoruz 
#burada thread vs açılmadan hallediyoruz

import socket
import asyncio

SERVER_PORT = 50050
SERVER_NAME = 'localhost'

async def main():   
    with socket.socket(family=socket.AF_INET, type=socket.SOCK_STREAM, proto=socket.IPPROTO_TCP) as server_sock:
        server_sock.bind((SERVER_NAME, SERVER_PORT))
        server_sock.listen(32)
        server_sock.setblocking(False)
    
        print('Waiting for connection...')
        while True:
            client_sock, client_addr =  await loop.sock_accept(server_sock)
            print(f'Connected: {client_addr}')
            loop.create_task(client_proc(client_sock))

async def client_proc(client_sock): #async fonksiyonu eğer bir fonksiyon blokeyse diğerine g
    while True:
        b = await loop.sock_recv(client_sock, 1024) 
        text = b.decode('UTF-8') 
        if text == "quit":
            break
        print(text)
        
        await loop.sock_sendall(client_sock, text[::-1].encode('UTF-8'))
        
    client_sock.shutdown(socket.SHUT_RDWR)
#event loop oluşturuyor ve sırayla işliyor cooperatif bir yapı oluşturuluyor
loop = asyncio.get_event_loop()
loop.run_until_complete(main())


