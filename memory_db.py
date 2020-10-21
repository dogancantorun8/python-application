# -*- coding: utf-8 -*-
"""
Created on Sat Oct 10 17:01:13 2020

@author: Dogancan Torun 
"""


#executescript soru işaretleriyle kullanılamaz 
import sqlite3

conn = None
try:
    conn = sqlite3.connect('student3.sqlite')
    cur = conn.cursor()
    cur.executescript("""
        CREATE TABLE IF NOT EXISTS student(student_no INTEGER PRIMARY KEY, student_name VARCHAR(64), school_id INTEGER);
        CREATE TABLE IF NOT EXISTS school(school_id INTEGER PRIMARY KEY AUTOINCREMENT, school_name VARCHAR(64));
    """)
    
    conn.commit()
    
    no = int(input('Öğrencinin numarasını giriniz:'))
    student_name = input('Öğrencinin adını ve soyadını giriniz:')
    school_name = input('Okulun adını ve soyadını giriniz:')
    
    cur.execute("INSERT INTO school(school_name) VALUES(?)", (school_name,))
    cur.execute("INSERT INTO student(student_no, student_name, school_id) VALUES(?, ?, (SELECT school_id FROM school WHERE school_name = ?))", (no, student_name, school_name))
    
    conn.commit()
                
except sqlite3.Error as e:
    print('Error', e)
finally:  
    if conn:
        conn.close() 
        

#yukarıdaki kodun revize edilmiş hali 
import sqlite3

conn = None
try:
    conn = sqlite3.connect('student3.sqlite')
    cur = conn.cursor()
    cur.executescript("""
        CREATE TABLE IF NOT EXISTS student(student_no INTEGER PRIMARY KEY, student_name VARCHAR(64), school_id INTEGER);
        CREATE TABLE IF NOT EXISTS school(school_id INTEGER PRIMARY KEY AUTOINCREMENT, school_name VARCHAR(64), UNIQUE(school_name));
    """)
    
    conn.commit()
    
    no = int(input('Öğrencinin numarasını giriniz:'))
    student_name = input('Öğrencinin adını ve soyadını giriniz:')
    school_name = input('Okulun adını giriniz:')
    
    cur.execute("INSERT OR IGNORE INTO school(school_name) VALUES(?)", (school_name,))
    cur.execute("INSERT INTO student(student_no, student_name, school_id) VALUES(?, ?, (SELECT school_id FROM school WHERE school_name = ?))", (no, student_name, school_name))
    
    conn.commit()
                
except sqlite3.Error as e:
    print('Error', e)
finally:  
    if conn:
        conn.close() 

#memorydatabase örneği 
import sqlite3

conn = None
try:
    conn = sqlite3.connect(':memory:') #memory db yptık
    cur = conn.cursor()
    cur.executescript("""
        CREATE TABLE IF NOT EXISTS student(student_no INTEGER PRIMARY KEY, student_name VARCHAR(64), school_id INTEGER);
        CREATE TABLE IF NOT EXISTS school(school_id INTEGER PRIMARY KEY AUTOINCREMENT, school_name VARCHAR(64), UNIQUE(school_name));
    """)
    
    conn.commit()
    
    while True:
        no = int(input('Öğrencinin numarasını giriniz:'))
        if not no:
            break     
        student_name = input('Öğrencinin adını ve soyadını giriniz:')
        school_name = input('Okulun adını giriniz:')
    
        cur.execute("INSERT OR IGNORE INTO school(school_name) VALUES(?)", (school_name,))
        cur.execute("INSERT INTO student(student_no, student_name, school_id) VALUES(?, ?, (SELECT school_id FROM school WHERE school_name = ?))", (no, student_name, school_name))
        conn.commit()
    
    cur.execute("SELECT student.student_no, student.student_name, school.school_name FROM student, school WHERE student.school_id = school.school_id")
    
    for no, student_name, school_name in cur:
        print(f'{no}, {student_name}, {school_name}')
              
except sqlite3.Error as e:
    print('Error', e)
finally:  
    if conn:
        conn.close()


#memorydatabase örneği 
import sqlite3

conn = None
try:
    conn = sqlite3.connect(':memory:')
    cur = conn.cursor()
    cur.execute("CREATE TABLE student(student_no INTEGER, student_name VARCHAR(64), student_bdate DATE)")
    
    cur.execute("INSERT INTO student VALUES(123, 'Hasan Bal', '2005-12-23')")
    cur.execute("INSERT INTO student VALUES(456, 'Sadık Dursun', '2004-11-22')")
    cur.execute("INSERT INTO student VALUES(768, 'Ayşe Er', '2003-08-17')")
    conn.commit()
    cur.execute("SELECT * FROM student")
    
    for no, name, bdate in cur:
        print(no, name, bdate, sep=', ')
                      
except sqlite3.Error as e:
    print('Error', e)
finally:  
    if conn:
        conn.close()


#database date uygulaması 
import sqlite3

conn = None
try:
    conn = sqlite3.connect(':memory:')
    cur = conn.cursor()
    cur.execute("CREATE TABLE student(student_no INTEGER, student_name VARCHAR(64), student_bdate DATE)")
    
    cur.execute("INSERT INTO student VALUES(123, 'Hasan Bal', '2005-12-23')")
    cur.execute("INSERT INTO student VALUES(456, 'Sadık Dursun', '2004-11-22')")
    cur.execute("INSERT INTO student VALUES(768, 'Ayşe Er', '2003-08-17')")
    conn.commit()
    
    cur.execute("SELECT * FROM student")
    
    
    import datetime
    
    days = ['Pazartesi', 'Salı', 'Çarşamba', 'Perşembe', 'Cuma', 'Cumartesi', 'Pazar']
    
    for no, name, bdate in cur:
       date = datetime.date.fromisoformat(bdate)
       print(no, name, date, date, days[date.weekday()], sep=', ')
        
                      
except sqlite3.Error as e:
    print('Error', e)
finally:  
    if conn:
        conn.close()

#connection nesnesinin icinde text factory ve row factory var.Bu fonksiyonarın kullanımını bize kolayıklar sağlıyor 

