
import dbm
db=dbm.open('sample.dbm','w') #nesne elde ettim önce sample dbm create ettim

#atayacagım degerler bytes yada string olmalı
db['name']='veli'
db['no']='123'


val=db['name']
print(val) #bytes verdi anahtar deger tabanlı sistemler bu şekilde tutar

keys=db.keys()
print(keys)

#value degerlerine eristim
for val in db.values():
    print(val)

import dbm

#keyleri with ile dosya okur gibi okudum
with dbm.open('sample.dbm', 'c') as db:
    for key in db.keys():
        print(key, '---->', db[key])

#keyleri ve valueleri with ile dosya okur gibi okudum
with dbm.open('sample.dbm', 'c') as db:
    for key, val in db.items():
        print(key, val)

    if 'ali' in db: #key kontrolü
        print('var')
    else:
        print('yok')
