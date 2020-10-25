# -*- coding: utf-8 -*-
"""
Created on Sat Oct 17 08:48:21 2020
@author: Dogancan Torun
"""


import sqlite3  
import re 
import PIL
import IPython
import io
import statistics

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
    s=input('Dersin ismini ve haftalık ders saatini giriniz:')
    ders_adi, ders_no= re.split(' *, *', s.strip()) 
    try:
        cur.execute("INSERT INTO class(class_name, class_week_hours) VALUES(?, ?)", (ders_adi, ders_no))
        cur.connection.commit()
        print('Kayıt başarıyla eklendi...\n')
    except:
        print('Ekleme işlemi başarısız!\n') 

#ogrenci girisi fonksiyonu 
def ogr_girisi (cur) : #cur nesnemi veriyorum  
    s=input("Öğrencinin adı soyadını, numarasını ve fotoğrafına ilişkin dosyanın yol ifadesini giriniz:")
    ogr_adi, ogr_path= re.split(' *, *', s.strip())
    
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
    s = input("Öğrencinin adı soyadı, ders ismi, sınav numarası ve not bilgisini giriniz: ").split(',')   
    try:
        
        #cur.execute("INSERT INTO grade(student_no, class_id ,class_exam_no , class_grade ) VALUES(?, ?,?,?)", (ogr_no, ders_adi,sınav_no ,ogr_not ))
        ogr_adi,ders_adi, sınav_no , ogr_not=re.split(' *, *', s.strip()) 
        
        cur.execute("SELECT student_no FROM student WHERE student_name = ?", (ogr_adi,))
        ogr_no = cur.fetchone()   
        
        cur.execute("SELECT class_id FROM class WHERE class_name = ?", (ders_adi,))
        class_id, = cur.fetchone()

        cur.execute("INSERT INTO grade(student_no, class_id ,class_exam_no , class_grade ) VALUES(?, ?,?,?)", (ogr_no, ders_adi,sınav_no ,ogr_not ))
        cur.connection.commit() 
        
        print('Kayıt başarıyla eklendi...\n')
    except:
        print('Ekleme işlemi başarısız!\n') 


#tum ogrenci kayıtlarını getirme 
def list_record(cur):
# =============================================================================
#     sql='SELECT student.student_no,student.student_name,grade.class_id , grade.class_exam_no, grade.class_grade,class.class_name,class.class_week_hours FROM student,grade,class WHERE student.student_no=grade.student_no AND grade.class_id=class.class_id'
#     cur.execute(sql) 
#     for no,name,class_id,class_exam_no,class_grade,class_name,class_week_hours in cur: #cur nesnesini unpack ettim
#             print('No: {} ----->>> ,Name= {}, Ders-No= {} , Sınav-No= {} , Not = {} , Dersadi= {} , Ders-saati = {}  \n' .format(no,name,class_id,class_exam_no,class_grade,class_name,class_week_hours)) 
#                   
#     conn.close()
# =============================================================================
    try:
        s = input('Öğrencinin numarasını giriniz:')
        if s == '':
            cur.execute("SELECT * FROM student")
        else:
            no = int(s)
            cur.execute("SELECT * FROM student WHERE student_no = ?", (no,))

        students = cur.fetchall()

        cur.execute("SELECT * FROM class")
        classes = cur.fetchall()
        for student_no, student_name, student_photo in students:
            print()
            print(f'Adı Soyadı: {student_name}')
            print(f'Numarası: {student_no}')
            print()

            weighted_total = 0
            total_week_hours = 0
            for class_id, class_name, class_week_hours in classes:
                cur.execute("SELECT class_grade FROM grade WHERE student_no = ? and class_id = ? ORDER BY class_exam_no", (student_no, class_id))

                grades = [t[0] for t in cur]
                if len(grades) != 0:
                    print(f'{class_name}: ', end='')
                    print(*grades, sep=', ')
                    weighted_total += statistics.mean(grades) * class_week_hours
                    total_week_hours += class_week_hours


            print()
            bio = io.BytesIO(student_photo)
            image = PIL.Image.open(bio)
            image.thumbnail((200, 300))
            IPython.display.display(image)
            print()

            print(f'Ağırlıklı Not Ortalaması: {weighted_total / total_week_hours:.2f} ')

    except:
        print('Yanlış giriş, Kayıt bulunamadı!')
    print()




#main fonksiyonum
def main():
    conn=None
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




