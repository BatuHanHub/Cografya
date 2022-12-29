from config import *
import os

sistem = os.name

if sistem == "nt":
    system = "cls"

elif sistem == "posix":
    system = "clear"

hosgeldiniz()

while True:
    secim = str(input(">>>"))
    
    # ÇIKIŞ +
    if secim == "3": 
        break
    
    #ÖLÇEKLER+
    elif secim == "1":
        os.system(system)
        olcekSecim()
        olcekTuru = str(input(">>>"))
        
        if olcekTuru == "1": 
            os.system(system)
            print('\t=====ÇİZGİLİ ÖLÇEK=====\n')
            print("FORMÜL: 1/x x'den 5 tane 0 silinir.\n")
            olcek = int(input("Ölceğinizi giriniz:"))
            if olcek >= 100000:
                pass
            elif olcek < 100000:
                hataOlcekCizgi()
                continue 
            olcek = olcek / 100000
            
            print(f'SONUÇ:\n1km={olcek}km')
            input("\nÇıkmak için bir tuşa basınız...")
            break
        
        elif olcekTuru == "2":
            os.system(system)
            print('\t=====KESİRLİ ÖLÇEK=====\n')
            print("FORMÜL: x KM ye 5 tane 0 eklenir.\n")
            haritaUzunluk = 1
            gercekUzunluk = int(input("Gerçek uzunluğunuzu giriniz:"))
            olcek = gercekUzunluk * 100000
            print(f'SONUÇ:\n1/{olcek}')
            input("\nÇıkmak için bir tuşa basınız...")
            continue
        
        else:
            hataOlcekTuru()
            continue
    
    #HARİTA +
    elif secim == "2":
        os.system(system)
        haritaSecim()
        haritaTuru = str(input(">>>"))
        if haritaTuru == "1":
            os.system(system)
            print('\t=====HARİTA ÖLÇEĞİ=====\n')
            print('FORMÜL: gerçek uzunluğa 5 tane 0 eklenir. gerçek uzunluk/harita uzunluk\n')
            gercekUzunluk = int(input("Gerçek uzunluğunuz kaç kilometre:"))
            haritaUzunluk = int(input("Haritanız kaç cm ile gösterilmiş:"))
            gercekUzunluk = gercekUzunluk * 100000
        
            olcek = gercekUzunluk / haritaUzunluk
        
            print(f'SONUÇ:\n1/{olcek}')
            input("\nÇıkmak için bir tuşa basınız...")
            break
            
        elif haritaTuru == "2":
            os.system(system)
            print('\t=====İKİ MERKEZ ARASI KM BULMA=====\n')
            print('FORMÜL: Ölçeğe 5 tane 0 eklenir. Harita uzunluğu*Ölçek')
            haritaUzunluk = int(input("Haritanız kaç cm ile gösterilmiş:"))
            olcek = int(input("Ölçeğinizi giriniz:"))
            
            olcek = olcek * 100000
            gercekUzunluk = haritaUzunluk * olcek
            
            print(f'SONUÇ:\n{gercekUzunluk}KM')
            input("\nÇıkmak için bir tuşa basınız...")
            break
    
        else: 
            hataHaritaSecim()
            continue
    
    else:
        os.system(sistem)
        hataHG()
        continue
