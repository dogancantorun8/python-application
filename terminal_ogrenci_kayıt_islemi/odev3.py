# -*- coding: utf-8 -*-
"""
Created on Sat Oct 17 08:48:21 2020
@author: Dogancan Torun
"""


import sqlite3 
conn = None 

conn = sqlite3.connect('uygulama.sqlite') 
cur = conn.cursor()
cur.execute( "CREATE TABLE IF NOT EXISTS student(student_no INTEGER PRIMARY KEY AUTOINCREMENT, student_name VARCHAR(64),student_photo BLOB)") 
cur.execute( "CREATE TABLE IF NOT EXISTS class(class_id INTEGER PRIMARY KEY AUTOINCREMENT, class_name VARCHAR(64),class_week_hours INTEGER )") 
cur.execute( "CREATE TABLE IF NOT EXISTS grade(student_no INTEGER , class_id INTEGER,class_exam_no INTEGER , class_grade INTEGER, FOREIGN KEY (student_no)  REFERENCES student(student_no) ) ") 
#conn.commit()
conn.close()

 


#giris menümün tasarımı
def get_option():
    print('1) Ders Girisi')
    print('2) Öğrenci Girisi')
    print('3) Not Girişi')
    print('4) Numaraya göre tüm kayıtları getirme ') 
    print('5) Çık')
    while True:
        try:
            result = int(input('\nSeçiminiz:'))
            if result >= 1 and result <= 5:
                break
            print('Giriş geçersiz!')
        except:
            print('Giriş geçersiz!')
    return result 


#ders girisi fonksiyonu 
def ders_girisi (cur) : 
    ders_adi, ders_no= input("Dersin ismini ve haftalık ders saatini giriniz:").split(',')   
    try:
        cur.execute("INSERT INTO class(class_name, class_week_hours) VALUES(?, ?)", (ders_adi, ders_no))
        cur.connection.commit()
        print('Kayıt başarıyla eklendi...\n')
    except:
        print('Ekleme işlemi başarısız!\n') 

#ogrenci girisi fonksiyonu 
def ogr_girisi (cur) : #cur nesnemi veriyorum  
    ogr_adi, ogr_path= input("Öğrencinin adı soyadını, numarasını ve fotoğrafına ilişkin dosyanın yol ifadesini giriniz:").split(',')   
    
    with open(ogr_path, 'rb') as f: #fotografı binary modda okudum
             photo = f.read()

    try:
        cur.execute("INSERT INTO student(student_name,student_photo ) VALUES(?, ?)", (ogr_adi, photo))
        cur.connection.commit()
        print('Kayıt başarıyla eklendi...\n')
    except:
        print('Ekleme işlemi başarısız!\n')   


#not girisi fonksiyonu 
def not_girisi (cur) : 
    ogr_no, ders_adi, sınav_no , ogr_not = input("Öğrencinin numarası, ders ismi, sınav numarası ve not bilgisini giriniz: ").split(',')   
    try:
        cur.execute("INSERT INTO grade(student_no, class_id ,class_exam_no , class_grade ) VALUES(?, ?,?,?)", (ogr_no, ders_adi,sınav_no ,ogr_not ))
        cur.connection.commit()
        print('Kayıt başarıyla eklendi...\n')
    except:
        print('Ekleme işlemi başarısız!\n') 


#tum ogrenci kayıtlarını getirme 
def list_record(cur):
    sql='SELECT student.student_no,student.student_name,grade.class_id , grade.class_exam_no, grade.class_grade,class.class_name,class.class_week_hours FROM student,grade,class WHERE student.student_no=grade.student_no AND grade.class_id=class.class_id'
    cur.execute(sql) 
    for no,name,class_id,class_exam_no,class_grade,class_name,class_week_hours in cur: #cur nesnesini unpack ettim
            print('No: {} ----->>> ,Name= {}, Ders-No= {} , Sınav-No= {} , Not = {} , Dersadi= {} , Ders-saati = {}  \n' .format(no,name,class_id,class_exam_no,class_grade,class_name,class_week_hours)) 
                  
    conn.close()
    


#main fonksiyonum
def main():
    try:
        conn = sqlite3.connect('uygulama.sqlite')
        cur = conn.cursor()

        while True:
            option = get_option() 
            if option == 5: #cıkısı sagladım
                break
            {1: ders_girisi , 2: ogr_girisi , 3: not_girisi ,4: list_record  }[option](cur) #switch case olmadığı için anahtarın değerine göre fonk çagırdım
            #{1: ders_girisi, 2: ogrenci_girisi, 3: not_girisi 4: list_record}[option](cur)

    finally:
        conn.close()

main() #main fonksiyonu çağrılıp kod başlatıyorum  




