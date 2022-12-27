#BAŞLANGIÇ

def hosgeldiniz():
    print('''\t=====HOŞGELDİNİZ=====
ne yapmak istersiniz\n
1)Ölçekleri birbirine dönüştürmek için "1"
2)Harita uzunluğunu hesaplamak için "2"
3)Çıkmak için "3" yazınız...\n''')
    
def hataHG():
    print('''HATA:Lütfen yapacağınız işlemi yazınız:\n
1)Ölçekleri birbirine dönüştürmek için "1"
2)Harita uzunluğunu hesaplamak için "2"
3)Çıkmak için "3" yazınız...\n''')

#ÖLÇEK DÖNÜŞTÜRME

def olcekSecim():
    print('''\t=====ÖLÇEK SEÇİMİ=====\n
1)Çizgili Ölçek dönüştürmek için "1"
2)Kesirli Ölçek dönüştürmek için "2" yazınız.''')
    
def hataOlcekTuru():
    print('''HATA:Lütfen işleyeceğiniz ölçek türünü yazınız:\n
1)Çizgili Ölçek dönüştürmek için "1"
2)Kesirli Ölçek dönüştürmek için "2" yazınız''')
    
##ÖLÇEK ÇİZGİ

def olcekCizgiHata():
    print("HATA! Lütfen 10000'den küçük sayı yazmayınız")

def olcekCizgi():
    olcek = str
    olcek = olcek[:5]
    olcek = int
    return olcek

##ÖLÇEK KESİR
    
def olcekKesir():
    haritaUzunluk = 1
    gercekUzunluk = int(input("Gerçek uzunluğunuzu giriniz:")) 
    olcek = gercekUzunluk * 100000
    return olcek

#HARİTA
