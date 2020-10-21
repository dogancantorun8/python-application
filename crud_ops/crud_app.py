# -*- coding: utf-8 -*-
"""
Created on Tue Oct  6 20:12:28 2020

@author: Doğancan torun
"""

#Console_Crud operations: 

import sqlite3

def get_option():
    print('1) Kayıt Ekle')
    print('2) Kayıt Listele')
    print('3) Kayıt sil')
    print('4) Çık')
    while True:
        try:
            result = int(input('\nSeçiminiz:'))
            if result >= 1 and result <= 4:
                break
            print('Giriş geçersiz!')
        except:
            print('Giriş geçersiz!')
    return result

def add_record(cur):

    while True:
        try:
            no = int(input('No:'))
            break
        except:
            print('Numara geçersiz! Yeniden Numara giriniz:')

    name = input('Adı Soyadı:')
    try:
        cur.execute('CREATE TABLE IF NOT EXISTS student2(student_no INTEGER PRIMARY KEY , student_name TEXT)')
        cur.execute("INSERT INTO student2(student_no, student_name) VALUES(?, ?)", (no, name))
        cur.connection.commit()
        print('Kayıt başarıyla eklendi...\n')
    except:
        print('Ekleme işlemi başarısız!\n')

def list_record(cur):
    cond = input('Koşul cümlesini giriniz:')
    sql = 'SELECT student_no, student_name FROM student2 '
    if cond != '':
        sql += 'WHERE {}'.format(cond)
    try:
        cur.execute(sql)
        print('\n-------------------------')
        print(f"{'No':<10}{'Adı Soyadı'}\n")
        for no, name in cur:
            print(f'{no:<10}{name}')
        print('--------------------------\n')
    except:
        print('Listeleme işlemi başarısız!')

def delete_record(cur):
    cond = input('Koşul cümlesini giriniz:')
    sql = 'DELETE FROM student2 WHERE {}'.format(cond)
    print(sql)

    try:
        cur.execute(sql) #execute komutuna delete sql ifadesini veriyorum
        cur.connection.commit()
        if cur.rowcount > 0:
            print('{} kayıt silindi\n'.format(cur.rowcount))
        else:
            print('Herhangi bir kayıt silinemedi!\n')
    except:
        print('Kayıt silinemedi!..\n')

def main():
    try:
        conn = sqlite3.connect('student2.sqlite')
        cur = conn.cursor()

        while True:
            option = get_option() #option nesnesini oluşturuyorum
            if option == 4:
                break
            {1: add_record, 2: list_record, 3: delete_record}[option](cur)

    finally:
        conn.close()

main() #main fonksiyonu çağrılıp kod başlatıyorum

