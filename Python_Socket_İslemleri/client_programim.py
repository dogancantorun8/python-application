#DNS:bu protokol tipiyle bir Ipnin birden fazla domaini yada bir domainin birden fazla ipsi olabilir.
#clientin socketi hep aktiftir pasif socketi yoktur.endpoint=serverin ipsi ve port bilgisinin iikisnin toplamÄ±
#Client program: 
    #1)Once socket yaratÄ±lacak bind yapmazsak da olur isletim sistemi bos port bulur 
# client.py


import socket

#baglanacagım port
SERVER_PORTNO = 50050
#baglanmak istedigim ip
SERVER_NAME = '127.0.0.1'

try:
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_sock:
        client_sock.connect((SERVER_NAME, SERVER_PORTNO))
        print('connected...')

        while True:
            text = input('Bir yazi giriniz:')
            b = text.encode('UTF-8')
            client_sock.send(b)
            if text == 'quit':
                break
            #serverdan gelen bilgiyi receive ile aldım
            b = client_sock.recv(1024) 
            #aldıgım bilgiyi donusturme islemi yaptim
            response = b.decode('UTF-8')
            print(response)

except Exception as e:
    print(e)




