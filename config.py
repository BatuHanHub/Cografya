#YAZILAR

def hosgeldiniz():
    print('''\t=====HOŞGELDİNİZ=====
ne yapmak istersiniz\n
1)Ölçekleri birbirine dönüştürmek için "1"
2)Harita uzunluğunu hesaplamak için "2"
3)Çıkmak için "3" yazınız...\n''')

#ÖLÇEK DÖNÜŞTÜRME

def olcekSecim():
    print('''\t=====ÖLÇEK SEÇİMİ=====\n
1)Çizgili Ölçek dönüştürmek için "1"
2)Kesirli Ölçek dönüştürmek için "2" yazınız.''')
    
#HARİTA
def haritaSecim():
    print('''\t=====HARİTA SEÇİMİ=====\n
1)Harita ölçeği bulmak için "1"
2)İki merkez arası km bulmak için "2" yazınız.\n''')
 
#HATALAR

def hataHG():
    print('''HATA:Lütfen yapacağınız işlemi yazınız:\n
1)Ölçekleri birbirine dönüştürmek için "1"
2)Harita uzunluğunu hesaplamak için "2"
3)Çıkmak için "3" yazınız...\n''')

def hataOlcekTuru():
    print('''HATA:Lütfen işleyeceğiniz ölçek türünü yazınız:\n
1)Çizgili Ölçek dönüştürmek için "1"
2)Kesirli Ölçek dönüştürmek için "2" yazınız''')

def hataOlcekCizgi():
    print("HATA! Lütfen 100000'den küçük sayı yazmayınız")
    
def hataHaritaSecim():
    print('''HATA:Lütfen işleyeceğiniz harita türünü yazınız:
1)Harita ölçeği bulmak için "1"
2)İki merkez arası km bulmak için "2" yazınız.''')
