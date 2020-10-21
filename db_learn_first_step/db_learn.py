

#db connection ve python ile querry oluşturma 

import sqlite3
conn = sqlite3.connect("student.db") #projeyle aynı dizinde oldugundan yalnızca db adının yazdım
cur = conn.cursor()
cur.execute("INSERT INTO ogr VALUES (1081,'süleyman Torun');") #querry bu kısım içinde olacak
conn.commit()  # veritabanında değişiklik yapan insert update gibi komutlar kullanıldığında yazılır
conn.close()

###update işlemi gerçekleştirelim
import sqlite3
conn=sqlite3.connect("student.db")
cur=conn.cursor()
cur.execute("UPDATE ogr SET id=1515 WHERE id=990 ;")
conn.commit()
conn.close()

#Select ile tüm dbdeki kayıtlara_eriştim
import sqlite3
conn = sqlite3.connect("student.db")
cur=conn.cursor()
cur.execute("SELECT* FROM ogr")
result=cur.fetchall() #bir liste dönüyor ve listenin elemanları demetlerden oluşuyor  
print(result)
conn.commit()
conn.close()  


#school tabloma erismek istersem 
import sqlite3
conn = sqlite3.connect("student.db")
cur=conn.cursor()
cur.execute("SELECT* FROM okul")
result=cur.fetchall() #bir liste dönüyor ve listenin elemanları demetlerden oluşuyor  
print(result)
conn.commit()
conn.close() 

#selecti for ile yazarsak;
import sqlite3
conn = sqlite3.connect("student.db")
cur=conn.cursor()
cur.execute("SELECT id,name FROM ogr")
for i,t in  cur.fetchall(): #liste seklinde donus sağlıyor
     print(i,t)
conn.commit()
conn.close()  

#inner join işlemi 
import sqlite3
conn = sqlite3.connect("student.db")
cur=conn.cursor() 
cur.execute("SELECT ogr.id, ogr.name ,okul.type FROM ogr, okul WHERE ogr.id = okul.id")
result = cur.fetchall()
print(result)
conn.close() 

#where ile sorgu yapma 
import sqlite3
conn = sqlite3.connect("student.db")
cur=conn.cursor()
cur.execute("SELECT * FROM okul  WHERE okul.type='mevlana'")
result=cur.fetchall()
print(result)
conn.close() 

#Secılen kaydı dogrudan rowcount diye bır ınstance attributetan alabılırız. Bu cursor nesnesiin bir elemanıdır.rowcountta -1 ın ozel bır anlamı vardır. 2 tane onemlı id var. 


#cur.fetchone() ==>Sadece bir kayıt elde eder. Fetchone bıze ılgılı kayıtları teker teker verır. Listenin sonuna geldiğimiz zaman NONE'a geri doner. Yanı fetchone() select kayıtlarını teker teker almamızı saglar. 
#fetchall() ile tum kayıtları tek hamlede alırken fetchone()'da ılgılı kayıtları teker  teker alırız. 
import sqlite3

conn = sqlite3.connect("student.db")
cur=conn.cursor()
cur.execute("SELECT* FROM okul")

result=cur.fetchone()  #sorgu sonucunda gelen ilk kayıt için atama işlemi yaptım
print(result)

result=cur.fetchone() #sorgu sonucunda gelen ikinci kayıt için atama işlemi yaptım
print(result) 
result=cur.fetchone() #sorgu sonucunda gelen üçüncü kayıt için atama işlemi yaptım
print(result) 
conn.close() 


#fetchmany() ==>bu da select ettıklerımızı n'er n'er verır. Yanı mesela 100 kayıt select ettık o kayıtları 5'er 5'er almak ıstersek. Parametre olarak kacar kacar gelsın sayısını alır
import sqlite3
conn = sqlite3.connect("student.db")
cur=conn.cursor()
cur.execute("SELECT* FROM ogr")
result=cur.fetchmany(5)
print(result)

result=cur.fetchmany(5)
print(result)
conn.close() 



#klavyeden alınan degeri dbye insert etme islemi: 
import sqlite3

conn = sqlite3.connect("student.db") #bu sekilde bir db yaratılmış
cur = conn.cursor() 

#eger tablo yaratılmamışsa bu satırı yazıyorum 
#cur.execute('CREATE TABLE IF NOT EXISTS ogr(id INTEGER PRIMARY KEY , name TEXT)')
while True:
    no = int(input('Numarayı giriniz:'))
    if no == 0: #0 girildiğinde db de ki kaıtlar listeleniyor
        break
    name = input('Ad soyad giriniz:')
    cur.execute("INSERT INTO ogr(id, name) VALUES({}, '{}')".format(no, name)) 
    #cur.execute("INSERT INTO student(student_no, student_name) VALUES(?, ?)", (no, name)) =>bu şekildede insert işlemi yapılabilirdi 
    #dict ile ikinci parametre verilip işlem yaptırdım 
    #cur.execute("INSERT INTO student(student_no, student_name) VALUES(:no, :name)", {'no': no, 'name': name}) => insert işleminin bir diğer opsiyonu
    conn.commit()

cur.execute('SELECT * FROM ogr')
for no, name in cur:
    print(no, name) 
conn.close() 

#try-catch bloklarıyla kodumuzdaki exception kontrolü aşağıdaki şekilde yapılabilir 
import sqlite3
conn = None
try:
    conn = sqlite3.connect("student.db") #bu sekilde bir db yaratılmış
    cur = conn.cursor()
    
    cur.execute('CREATE TABLE IF NOT EXISTS student(student_no INTEGER PRIMARY KEY , student_name TEXT)')
    
    while True:
        no = int(input('Numarayı giriniz:'))
        if no == 0:
            break
        name = input('Ad soyad giriniz:')
        cur.execute("INSERT INTO ogr(id, name) VALUES({}, '{}')".format(no, name)) 
        conn.commit()

    cur.execute('SELECT * FROM ogr')
    for no, name in cur:    
        print(no, name)
    
except sqlite3.Error as e:
    print('Error:', e)
finally:
    if conn:
        conn.close() 

#Notlar::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::: 
#commit işlevi:Atomikliği sağlamak için düşünülmüş bir yapı  
#yani bir insert ve bir select bağlantılıysa bunu aynı da yaparsak bütünlüğü sağlama işlemi transaction olarak adlandırılır 
#iki tane update işlemini beraber yapıp tutarsızlıkları ortadan kaldırmak için transaction işlem yapılır 
#biz şu ana kadar sql komutlarını cursor sınıfının execute methoduyla yaptık.  
#bundan sonra executemany komutu ile işlem yapacağız .tek sorgu yazıp birden fazla parametre veriyoruz buraya dikkat iki sql yok !! 
#executemanyde dictler ile de insert yapabiliriz.  
#executescript : ile birden fazla sql sorgusunu yazıyoruz 

#executemany örnek: 
import sqlite3
conn = None
try:
    conn = sqlite3.connect("student.db") 
    cur = conn.cursor()
    #toplu halde bir bilgi varsa tercih edilmektedir.bir csv yi okuyup veri tabanına ekleyebiliriz
    cur.executemany("INSERT INTO okul VALUES(?, ?)", [(251, 'John Lennon'), (252, 'Paul McCartney')])
    conn.commit()
    
except sqlite3.Error as e:
    print('Error', e)
finally:
    if conn:
        conn.close()
        





