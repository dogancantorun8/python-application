#Socketlerde amaç:Bir network altında(LAN-INTERNET-WAN) bir makineden diğer makinelere bigi gönderip almaya yarar
#Herhangi iki makina haberleşebilmesi için  bir protokol gereklidir.
#Makinalar arası haberleşmede en yaygın kullanılan IP protokolü.
#Protokol aileleri genelde üst üste yığılarak ilerler
#IEEE OSI kavramından bahsederek 7 katmandan oluşan katmanların birbirinden izole edildiği yapıyı öne sürdü
    #Fiziksel Layer:Kablolar vs olan tamamen fiziksel katman
    #Data link layerda:Fiziksel adresleme vardır.Ethernet kartları bu layerda.Ethernet Protokolü =>Hem fiziksel hem
    #Network Layer:İki LAN'ın haberleştiği layer.Router yardımıyla bu arealar arasında bilgi transferi olur.Evdeki adsl bu işi yapar.Mantıksal adresleme yapılır
    #Transport Layer:İki host arasında bilgi alışverişi paket düzeyinden streame döner.
    #Session Layer:Verilerin gidip gelirken şifreleneceği katman
    #Application Layer:İki programın haberleştiği katmanlar

#IP:OSI'nin 4 katmanını kullanılır
    #1)Ethernet/Wireless >>
    #2)IP protokolü:Hostları belirtmek için mantıksal adresler belirtiliyor(Ipv4 ıpv6) >>
    #3)TCP/UDP:Tcp stream tabanlı haberleşme yaptırır yani byte byte bilgi gönderiyor.Karşı tarafta byte byte okuyr buna stream tabanlı okuma denir
        #IP protokolünde alıcının paketi alıp almadığı kontrol etmezken TCP bunu kontrol eder.TCP de amaç client-server haberleşme temellidir.
        #UDP:Paket tabanlı haberleşme yapıyor.Bilgi akışı byte düzeyinde olmuyor.Daha hızlı fakat güvensiz bir haberleşme oluyor.Bağlantısız bir protokol
        #İki host haberleşirken istediğimiz iki programın haberleşmesini istediğimizde port numarasıyla bunu belirtmeliyiz.Yani ben 2552. porttaki programla konuşmak istiyorum.(TCP-VE UDP her ikiside port numarasını kullanır) >>
    #4)Application Layer:HTTP,TELNET,SSH,FTP bu kısımdaki protokollerdir.

#HTTP:TCP ile herhangi bir web serverın bilgilerini browser yardımıyla görüntüleriz.
#Client-Server bir protokol değil çalışma modelidir.

#Socket kavramı ve socket kütüphanesi:socket kütüphaneleri C dilinde yazılmıştır
#windowsta winsoc kütüphanesiyle socket işlemlerini yapabiliyoruz.Genel bir kütüphane IP ailesine özgü bir kütüphane değil







