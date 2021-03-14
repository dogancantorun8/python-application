# -*- coding: utf-8 -*-
"""
Created on Sun Feb 14 17:12:35 2021

@author: Dogancan Torun
"""


#write islemlerden sonra flusch yapmalıyız 
#flusch dersekbuffer dolmadan karşıya göndermemizi saglıyor 
#@statick method sınıf içinde olmasına rağmen selfe bağlı olmayan method 

import socket
import threading

DEF_SERVER_PORT = 50050

class Client:
    def __init__(self, sock, addr):
        self.sock = sock
        self.addr = addr
        self.nick = None
        self.thread = None
        
class Server:
    def __init__(self, port):
        self.clients = {}
        self.port = port
        
    def run(self):
        try:
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM, socket.IPPROTO_TCP) as server_sock:
                server_sock.bind(('', self.port))
                server_sock.listen(32)
                server_sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
                
                print('waiting for connection....')
            
                while True:
                    client_sock, client_addr = server_sock.accept()
                    client = Client(client_sock, client_addr)
                    thread = threading.Thread(target=self.thread_proc, args=(client,))
                    client.thread = thread
                    self.clients[client_sock] = client
                    thread.start()
                    print('new client connected (total {} client(s)):'.format(len(self.clients)))
        
        except Exception as e:
            print(e)
                   
    def thread_proc(self, client):
        try:
            fr_sock = client.sock.makefile('r', encoding='UTF-8')
            fw_sock = client.sock.makefile('w', encoding='UTF-8')
            while True:       
                cmd = fr_sock.readline()[:-1]
                if not cmd:
                    break
                print(f'{cmd} command received from {client.addr}')
                Server.process_cmd(cmd, fw_sock)
        except:
            pass
    
        client.sock.close()
        del self.clients[client.sock]                
    
        print('client disconnected (total {} client(s)):'.format(len(self.clients)))
             
    @staticmethod
    def process_cmd(cmd, fw_sock):
        #bosluklardan ayırdım 
        cmd_params = cmd.split()
        
        #ilgili operasyon icin yapacagım islemin fonksiyonunu cagırıyorum
        cmd_dict = {'ADD': Server.process_cmd_basic, 'SUB': Server.process_cmd_basic, 'MUL': Server.process_cmd_basic, 'DIV': Server.process_cmd_basic, 'SQRT': Server.process_cmd_sqrt, 'DISCONNECT': Server.disconnect_proc}
        #splitin sıfırıncı elemanı operasyonun adını veriyr
        f = cmd_dict.get(cmd_params[0])
        if not f:
            fw_sock.write(f'ERROR Invalid command: {cmd_params[0]}\n')
            fw_sock.flush()
            return
        
        f(fw_sock, cmd_params)
        
    @staticmethod
    def process_cmd_basic(fw_sock, params):
        if len(params) != 3:
            fw_sock.write(f'ERROR Wrong number of arguments\n')
            fw_sock.flush()
            return
        try:
            if params[0] == 'ADD':
                result = float(params[1]) + float(params[2])
            elif params[0] == 'SUB':
                result = float(params[1]) - float(params[2])
            elif params[0] == 'MUL':
                result = float(params[1]) * float(params[2])
            elif params[0] == 'DIV':
                result = float(params[1]) / float(params[2])
            fw_sock.write(f'RESULT {result}\n')

        except:
            fw_sock.write(f'ERROR invalid parameters for ADD command\n')
            
        fw_sock.flush()
    
    @staticmethod
    def process_cmd_sqrt(fw_sock, params):
        if len(params) != 2:
            fw_sock.write(f'ERROR Wrong number of arguments\n')
            fw_sock.flush()
            return
        try:
             result = float(params[1]) ** 0.5
             fw_sock.write(f'RESULT {result}\n')
        except:
             fw_sock.write(f'ERROR invalid parameters for ADD command\n')
             
        fw_sock.flush()
        
    @staticmethod
    def disconnect_proc(fw_sock, params):
        if len(params) != 1:
            fw_sock.write(f'ERROR Wrong number of arguments\n')
            fw_sock.flush()
            return 
        
        raise Exception()
        

server = Server(DEF_SERVER_PORT)
server.run()