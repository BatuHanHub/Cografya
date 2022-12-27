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
            os.system(system)
            print('\t=====ÇİZGİLİ ÖLÇEK=====\n')
            olcek = int(input("Ölceğinizi giriniz:"))
            if olcek >= 100000:
                pass
            elif olcek < 100000:
                olcekCizgiHata()
                continue 
            olcekCizgi()
            print(olcek)
            continue
        
        elif olcekTuru == "2":
            input("Kesirli olcek")
            os.system(system)
            print('\t=====KESİRLİ ÖLÇEK=====\n')
            haritaUzunluk = 1
            gercekUzunluk = int(input("Gerçek uzunluğunuzu giriniz:"))
            olcek = gercekUzunluk * 100000
            print(olcek)
            continue
        
        else:
            os.system(system)
            hataOlcekTuru()
            continue
        
        break
    
    elif secim == "2":
        os.system(system)
        input('harita')
        gercekUzunluk = int(input("Gerçek ucunluğunuz kaç kilometre:"))
        haritaUzunluk = int(input("Haritanız kaç cm ile gösterilmiş:"))
        gercekUzunluk = str(gercekUzunluk)
        gercekUzunluk = gercekUzunluk + "00000"
        gercekUzunluk = int(gercekUzunluk)
        
        olcek = haritaUzunluk / gercekUzunluk
        
        #çalışıyor EKLEME YAP
        
        print(olcek)
        break
    
    else:
        os.system(sistem)
        hataHG()
        continue
