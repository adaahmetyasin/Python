from operator import truediv
import random
import time

class Kumanda():

    def __init__(self, tv_durum = "Kapalı", tv_ses = 0, kanal_listesi = ["Trt"], kanal = "Trt"):
        
        self.tv_ses =  tv_ses

        self.tv_durum = tv_durum

        self.kanal_listesi = kanal_listesi

        self.kanal = kanal

    def tv_ac(self):
        if(self.tv_durum == "Açık"):
            print("Televizyonunuz zaten açık")
        else:
            print("Televizyonunuz açılıyor ..")
            self.tv_durum = "Açık"

    def tv_kapa(self):
        if(self.tv_durum == "Kapalı"):
            print("Televizyonunuz zaten kapalı")
        else:
            print("Televizyonunuz kapanıyor ..")
            self.tv_durum = "Kapalı"
    
    def ses_ayarları(self):

        while True:
            karakter = input("Azaltmak için: '<' \nArtırmak İçin: '>' \nÇıkış iiçin: 'q' ya basın\n")

            if (karakter == "<"):
                if (self.tv_ses != 0):
                    self.tv_ses -= 1
                    print("Ses:",self.tv_ses)
            elif (karakter == ">"):
                if (self.tv_ses != 32):
                    self.tv_ses += 1
                    print("Ses:",self.tv_ses)
            else:
                print("Ses Güncellendi:",self.tv_ses)
                break
    
    def kanal_ekle(self,kanal_ismi):
        print("Kanal ekleniyor")
        time.sleep(1)

        self.kanal_listesi.append(kanal_ismi)
        print("Kanal eklendi")
    
    def rastgele_kanal(self):
        
        rastgele = random.randint(0,len(self.kanal_listesi)-1)

        self.kanal = self.kanal_listesi[rastgele]

        print("Şu anki kanal:" ,self.kanal)
    
    def __len__(self):
        return len(self.kanal_listesi)

    def __str__(self):
        return ("""
        TV durumu:{}
        TV ses:{}
        Kanal listesi:{}
        Şu anki kanal:{}
        """.format(self.tv_durum, self.tv_ses, self.kanal_listesi, self.kanal))


kumanda = Kumanda()
print("""*******************

Televizyon Uygulaması

İşlemler ;

1. Televizyonu Aç

2. Televizyonu Kapat

3. Ses ayarları

4. Kanal Ekle

5. Kanal Sayısını Öğrenme

6. Rastgele Kanal'a Geç

7. Televizyon Bilgileri

Çıkmak için 'q' ya basın.
*******************""")

while True:

    işlem = input("İşlemi seçiniz:")

    if (işlem == "q"):
        print("Program sonlandırılıyor")
        break

    if(işlem == "1"):
        kumanda.tv_ac()
    
    elif(işlem == "2"):
        kumanda.tv_kapa()
    
    elif(işlem == "3"):
        kumanda.ses_ayarları()
    
    elif(işlem == "4"):
        kanal_isimleri = input("Kanal isimlerini ',' ile ayırarak girin:")
        kanal_listesi = kanal_isimleri.split(",")
        for eklencekler in kanal_listesi:
            kumanda.kanal_ekle(eklencekler)
    
    elif(işlem == "5"):
        print("Kanal sayısı:", len(kumanda))
    
    elif(işlem == "6"):
        kumanda.rastgele_kanal()
    
    elif(işlem == "7"):
        print(kumanda)
    
    else:
        print("Geçersiz işlem....")
        



