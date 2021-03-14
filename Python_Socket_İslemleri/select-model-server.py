# -*- coding: utf-8 -*-
"""
Created on Sat Feb 20 18:34:58 2021

@author: Dogancan Torun
"""

#herhangi bir model için oluşturduğumuz client ile bu koda bağlanabiliriz 
#select modelde de herhangi bir thread yaratılmadı  
#işletim sistemine paket gelince bana haber ver diyorum 

import socket
import select

SERVER_PORT = 50050
SERVER_NAME = 'localhost'

def main():
    try:
        with socket.socket(family=socket.AF_INET, type=socket.SOCK_STREAM, proto=socket.IPPROTO_TCP) as server_sock:
            server_sock.bind((SERVER_NAME, SERVER_PORT))
            server_sock.listen(32)
    
            print('Waiting for connection...')
    
            rlist = [server_sock]
            wlist = []
            elist = rlist
            
            while rlist:
                try:
                    readable, writeable, exceptional = select.select(rlist, wlist, elist)
                    for sock in readable:
                        if sock is server_sock:
                            #okuma islemi geldiginde bilgi gelen socketleri ekliyorum
                            client_sock, client_addr = sock.accept()
                            rlist.append(client_sock)
                            print(f'new client connected: {client_addr}')
                        else:
                            b = sock.recv(1024)
                            if not b:
                                rlist.remove(sock)
                                print(f'client socket closed: {sock.getpeername()}')
                                sock.close()
                                
                                continue
                            text = b.decode('UTF-8')
                            if text == 'quit':
                                sock.shutdown(socket.SHUT_RDWR)
                                print(f'client socket disconneted: {sock.getpeername()}')
                                sock.close()
                                rlist.remove(sock)
                                continue
                            print(f'message from client {sock.getpeername()}: {text}')
                            sock.send(text[::-1].encode('UTF-8'))
                            
                    for sock in exceptional:
                        print(f'exception occured on socket: {sock.getpeername()}')
                        sock.close()
                        rlist.remove(sock)
                except:
                    print(f'exception occured on socket: {sock.getpeername()}')
                    sock.close()
                    rlist.remove(sock)
                                 
    except Exception as e:
        print(e)

main()
