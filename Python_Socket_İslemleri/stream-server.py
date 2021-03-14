# -*- coding: utf-8 -*-
"""
Created on Sun Feb 21 17:55:08 2021

@author: Doğancan
"""


import socket
import asyncio

SERVER_PORT = 50050
SERVER_NAME = 'localhost'

# for bug patch with Spyder
import nest_asyncio

nest_asyncio.apply()

async def client_proc(reader, writer):
    peername = writer.get_extra_info('peername') #bağlantı sağlandığında karşı tarafın ip si ve portunu veriyor
    print(f'new client connected: {peername}')
    while True:
        b = await reader.readline()
        if not b:
            break
        s = b[:-1].decode('UTF-8')
        if s == 'quit':
            break
        print(f'message from client {peername}: {s}')
        writer.write((s[::-1] + '\n').encode('UTF-8'))
        await writer.drain()
                
    writer.close()
    await writer.wait_closed()
    print(f'client disconnected: {peername}')

loop = asyncio.get_event_loop()
print('waiting for connection...')
server = asyncio.start_server(client_proc, SERVER_NAME, SERVER_PORT)
loop.run_until_complete(server)
loop.run_forever()

