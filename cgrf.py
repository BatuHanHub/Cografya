from config import *
import os

sistem = os.name

if sistem == "nt":
    system = "cls"

elif sistem == "poxit":
    system = "clear"

hosgeldiniz()

while True:
    secim = str(input(">>>"))
    
    if secim == "3":
        input("çıkış")
        break
    
    elif secim == "1":
        os.system(system)
        olcekSecim()
        olcekTuru = str(input(">>>"))
        
        if olcekTuru == "1":
            input("Çizgili Olcek")
            pass
        
        elif olcekTuru == "2":
            input("Kesirli olcek")
            pass
        
        else:
            os.system(system)
            hataOlcekTuru()
            continue
        
        break
    
    elif secim == "2":
        os.system(system)
        input('harita')
        break
    
    else:
        os.system(sistem)
        hataHG()
        continue