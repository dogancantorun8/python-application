# -*- coding: utf-8 -*-
"""
Created on Sun Feb 21 17:55:27 2021

@author: Doğancan
"""

# stream client


# stream client

import asyncio

# for bug patch with Spyder

import nest_asyncio

nest_asyncio.apply()

SERVER_NAME = 'localhost'
SERVER_PORT = 50050

async def client_proc(server_name, server_port, loop):
    try:
        reader, writer = await asyncio.open_connection(server_name, server_port, loop=loop)
    
        while True:
            s = input('Bir yazı giriniz:')
            b = (s + '\n').encode('UTF-8')
            writer.write(b)
            await writer.drain()
            
            if s == 'quit':
                break
            
            b = await reader.readline()
            s = b.decode('UTF-8')
            s = s[:-1]
            print(s)
        
        writer.close()
        await writer.wait_closed()
        
    except Exception as e:
        print(e)

loop = asyncio.get_event_loop()
loop.run_until_complete(client_proc(SERVER_NAME, SERVER_PORT, loop))



