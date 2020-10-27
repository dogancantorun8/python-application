# -*- coding: utf-8 -*-
"""
Created on Wed Oct 28 00:12:59 2020

@author: Dogancan Torun
"""

######################  Python_programlarında komut satırı argümanları #################  

import sys 
if __name__=='__main__':  
# =============================================================================
#     for s in sys.argv: 
#         print(s) 
# =============================================================================
    total=0   
    #sys.argv ile komut  satırından okuduklarıma back endde islem yaptırdım
    for s in sys.argv[1:]:  #ilk elemandan itibaren komut satırından girilenleri dilimleyip topladım
        total += float(s) 
    
    print(total)
     

