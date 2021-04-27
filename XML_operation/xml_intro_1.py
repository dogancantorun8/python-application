# -*- coding: utf-8 -*-
"""
Created on Thu Apr 15 11:52:01 2021

@author: dogancan
"""

#Xml:Bir dökümanın belirli formatlarda aktarılmasını sağlamak ve iletmek için XML'den yararlanılır.[Rich text dil]
#Xml de bir root elemanı olmalı.
#XML syntaxı; 
    #XML dökümanına başlarken versiyon numarası ile başlanır şu anda en güncel XML version 1.0 
    #Döküman Taglerden oluşuyor ve tagler iç içe olabilir.
    #Tipik bir XML tagında akış ; startTag,Attribute,Content ve EndTag şeklindedir.
    #   <table1>
    #    <student AdıSoyadı="Ali Serçe" No="1234" DoğumTarihi="1990" />
    #    <student AdıSoyadı="Salim Dünbar" No="7272" DoğumTarihi="1950" />
    #   </table1>   
    #Not:XML içerisinde attribute bilgileri tırnak içerisinde yazılırken contente ilişkin bilgiler tırnakla veilmez. 
    #Attributeler arasında virgül kullanılmaz boşluk bırakılır. 

#Yukarıdaki Xml'in 2.alternatifi aşağıdaki gibidir; 
    # <table2>
    #     <student>
    #         <AdıSoyadı>Ali Serçe</AdıSoyadı>
    #         <No>1234</No>
    #         <DoğumTarihi>1990</DoğumTarihi>
    #     </student>
    # 
    #     <student>
    #         <AdıSoyadı>Salim Dündar</AdıSoyadı>
    #         <No>7272</No>
    #         <DoğumTarihi>1950</DoğumTarihi>
    #     </student>
    # </table2>

#Namespace:XML'de aynı isimli çakışmaları önlemek için Namespace yapısı kullanılır 
#     <root>
#     
#     <h:table xmlns:h="http://www.w3.org/TR/html4/">
#       <h:tr>
#         <h:td>Apples</h:td>
#         <h:td>Bananas</h:td>
#       </h:tr>
#     </h:table>
#     
#     <f:table xmlns:f="https://www.w3schools.com/furniture">
#       <f:name>African Coffee Table</f:name>
#       <f:width>80</f:width>
#       <f:length>120</f:length>
#     </f:table>
#     
#     </root>
