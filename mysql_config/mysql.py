# -*- coding: utf-8 -*-
"""
Created on Sat Oct 17 16:52:06 2020

@author: Dogancan Torun
"""

import mysql.connector as mysqlc

conn = None
try:
    conn = mysqlc.connect(host='localhost', user='root', passwd='123456', database='student')
    cur = conn.cursor()
    while True:
        no = int(input('No:'))
        if no == 0:
            break
        name = input('Adı Soyadı:')
        cur.execute("INSERT INTO student2 VALUES(189, 'Sacit Apaydın')")
        conn.commit()
    cur.execute("SELECT * FROM student")
    for no, name in cur:
        print(no, name)
except mysqlc.Error as e:
    print(e)
finally:
    if conn:
        conn.close()

###yukardaki kodun yer tutucu farklı şekli
import mysql.connector as mysqlc

conn = None
try:
    conn = mysqlc.connect(host='localhost', user='root', passwd='123456', database='student2')
    cur = conn.cursor()
    while True:
        no = int(input('No:'))
        if no == 0:
            break
        name = input('Adı Soyadı:')
        cur.execute("INSERT INTO student VALUES({}, '{}')".format(no, name))
        conn.commit()
    cur.execute("SELECT * FROM student")
    for no, name in cur:
        print(no, name)
except mysqlc.Error as e:
    print(e)
finally:
    if conn:
        conn.close()

#mysql tablo yaratıp insert etme işlemi
import mysql.connector as mysqlc

conn = None
try:
    conn = mysqlc.connect(host='localhost', user='root', passwd='123456')
    cur = conn.cursor()
    cur.execute("CREATE DATABASE IF NOT EXISTS school")
    cur.execute("USE school")
    cur.execute("CREATE TABLE IF NOT EXISTS school(school_id INTEGER PRIMARY KEY AUTO_INCREMENT, school_name VARCHAR(45))")

    while True:
        name = input('Okul İsmi:')
        if name == '':
            break
        cur.execute("INSERT INTO school(school_name) VALUES(%s)", (name,))
        conn.commit()
    cur.execute("SELECT * FROM school")
    for no, name in cur:
        print(no, name)
except mysqlc.Error as e:
    print(e)
finally:
    if conn:
        conn.close()

 

