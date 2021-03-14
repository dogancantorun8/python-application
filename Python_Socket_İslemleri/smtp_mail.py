# -*- coding: utf-8 -*-
"""
Created on Sat Mar 13 17:44:02 2021

@author: Asus
"""


import smtplib

msg = '''From: kaan.aslan@gmail.com
To: youtube@csystem.org
Subject:Test
This is a new test
'''

receipants = []

with open('mail.txt') as f:
    for mail in f:
        if mail.strip() != '':
            receipants.append(mail[:-1])
        
print(receipants)
# =============================================================================
# 
# with open('f:\\Mypassword.txt') as f:
#     user_name = f.readline().strip()
#     password = f.readline().strip()
# =============================================================================


server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
server.ehlo()
server.login('dogancan.torun40@gmail.com','Dogancan1903.')
server.sendmail('dogancan.torun40@gmail.com', receipants, msg) 
server.quit()

