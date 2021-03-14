#Server programım:
    #1)İlk önce  socket yaratılıyor
    #2)Socket bind ediliyor(hangi portun acık oldugu bilgisi veriliyor):hosta ip paketi geldiğinde gelen bilginin port numarasına bakıp o programa gelen bilgiyi aktarıyor
                #bind sırasında port numarası ve hangi network  kartı üzerinden geleni dinleyecegimi soyluyorum
    #3)Listen islemi yapılıyor
    #4)Accept=> Gelen baglantılar kabul ediliyor
    #5)Send-Receive
    #6)Shutdown islemi
    #7)Socket close

#İki temel socket türü vardır.(stream tabanlı,paket tabanlı)
#socket=>>AF_INET IPV4 kullanacagım demek

##1-2)Portun yaratılıp baglantı kurulma asaması:soketi yarattık ve portla iliskilendirdik
import socket
SERVER_PORTNO = 50050
try:
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM, socket.IPPROTO_TCP) as server_sock:
        server_sock.bind(('', SERVER_PORTNO))        
except Exception as e:
    print(e)

print('ok')

#3)3.islem olarak soketi dinleme asamasına geciyorum listen islemiyle bize baglanan programları isletim sistemine devrediyorum ve kuyrukluyorum kuruğun eleman sayısını ben belirtiyorum 
import socket
SERVER_PORTNO = 50050
try:
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM, socket.IPPROTO_TCP) as server_sock: #with ile açarsam socket zaten kapanıyor close etme yazmama gerek yok
        server_sock.bind(('', SERVER_PORTNO))
        server_sock.listen(32) #bu socketten yalnızca dinleme olur herhangi bir mesaj gonderemem =pasif socket
                
except Exception as e:
    print(e)

print('ok')

#4)Accepted asamasına geciyorum :Accepted bize ne veriyor =>>Accepted bize her client icin bir socket verir ve clientin ip bilgisini verir.Tuple seklinde socketleri verir.Client tarafında da bir port açıyoruz 

#5)Send-Receive:Bilgi alısverisi baslıyor:
    #Send bytes seklinde gönderiyor;
import socket

SERVER_PORTNO = 50050

try:
    #pasif socket yaratıyor
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM, socket.IPPROTO_TCP) as server_sock:
        server_sock.bind(('', SERVER_PORTNO))
        server_sock.listen(32)

        print('waiting for connection....')
        client_sock, client_addr = server_sock.accept()
        print(f'connected: {client_addr}')

        while True:
            b = client_sock.recv(1024) #en fazla kac byte okuyabiliriz bunu yazıyoruz
            text = b.decode('UTF-8')
            if text == 'quit':
                break
            print(text) 
            #socketler çift taraflı veri alışverişi yapabiliyor server tarafından da send edilebiliyor
            #linux sistemlerde sendden dönünce tüm paket network katmanındadır. fakat receivde böyle bir durum yoktur adamın paketini iki receive ile alabiliriz
            client_sock.send(text[::-1].encode('UTF-8'))
        
except Exception as e:
    print(e)

#Socketi işlem bittikten sonra önce shutdown etmeliyiz ardından kapamalıyız.client_sock.shutdown(socket.Shut_RDWR)



