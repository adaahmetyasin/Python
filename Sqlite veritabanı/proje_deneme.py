from kütüphane_proje import *

print("""
***********************************

Kütüphane programına hoşgeldiniz..

İşlemler;

1. Kitapları göster

2. Kitap sorgula

3. Kitap ekle

4. Kitap sil

5. Baskı yükselt

Çıkmak için 'q' ya basın.

***********************************
""")

kütüphane = Kütüphane()
while True:
    işlem = input("Yapacağınız İşlem:")

    if (işlem == "q"):
        print("Program sonlandırılıyor...")
        break
    
    elif(işlem == "1"):
        kütüphane.kitapları_göster()
    
    elif(işlem == "2"):
        isim = input("Hangi kitabı arıyorsunuz ?")
        print("Kitap sorgulanıyor")
        time.sleep(1)

        kütüphane.kitap_sorgula(isim)

    
    elif(işlem == "3"):
        
        print("Kitap bilgilerini giriniz\n")
        
        isim = input("İsim:")
        yazar = input("Yazar:")
        yayınevi = input("Yayınevi:")
        tür = input("Tür:")
        baskı = int(input("Baskı:"))

        yeni_kitap = Kitap(isim, yazar, yayınevi, tür, baskı)

        print("Kitap ekleniyor ..")
        time.sleep(1)

        kütüphane.kitap_ekle(yeni_kitap)
        print("Kitap eklendi.")

    elif(işlem == "4"):
        isim = input("Hangi kitabı silmek istiyorsunuz ?")

        cevap = input("Emin misiniz ? (E/H)")
        if(cevap == "E"):
            print("Kitap siliniyor..")
            time.sleep(2)
            kütüphane.kitap_sil(isim)
            print("Kitap silindi.")
    
    elif(işlem == "5"):
        isim = input("Hangi kitabın baskısını yükseltmek istiyorsunuz ?")
        print("Baskı yükseltiliyor")
        time.sleep(1)
        kütüphane.baskı_yükselt(isim)
        print("Baskı yükseltildi.")
    
    else:
        print("Geçersiz işlem")