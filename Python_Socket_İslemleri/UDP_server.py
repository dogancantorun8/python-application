# -*- coding: utf-8 -*-
"""
Created on Sun Mar  7 18:46:52 2021

@author: Asus
"""

#server Program

import socket
import threading
import queue

SERVER_PORT = 50050
NTHREADS = 5

def main():
    try:
        with socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM, proto=socket.IPPROTO_UDP) as server_sock:
            server_sock.bind(('', SERVER_PORT))
            
            q = queue.Queue()
            for i in range(NTHREADS):
                thread = threading.Thread(target=thread_proc, args=(server_sock, q), daemon=True) 
                thread.start()
                        
            print('waiting for data...')
            while True:
                b, addr = server_sock.recvfrom(1024)
                q.put((b, addr))
              
                
    except Exception as e:
        print(e)
    
def thread_proc(sock, q):
    while True:
        b, addr = q.get()
        s = b.decode('utf-8')
        print(f'{addr}: {s}')
        b = s[::-1].encode('utf-8')
        sock.sendto(b, addr)
        
main()

