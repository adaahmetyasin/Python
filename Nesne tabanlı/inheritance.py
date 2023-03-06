from email.errors import MissingHeaderBodySeparatorDefect
from tkinter import Y


class Calisan():
    def __init__(self,isim,maas,departman):
        print("calisan init fonksiyonu")

        self.isim = isim
        self.maas = maas
        self.departman = departman
    
    def bilgileri_göster(self):
        print("Calisan sınıfının bilgileri ...")
        print("İsim :{}\nMaaş:{}\nDepartman:{}".format(self.isim, self.maas, self.departman))

    def departman_degis(self,yeni_deparman):
        self.departman = yeni_deparman



class Yönetici(Calisan):
    def __init__(self,isim,maas,departman,kisi_sayisi):
        print("yönetici init fonksiyonu")

        # self.isim = isim
        # self.maas = maas
        # self.departman = departman
        super().__init__(isim,maas,departman)
        self.kisi_sayisi = kisi_sayisi
    def bilgileri_göster(self):
        print("""Yönetici sınıfının bilgileri ...
        İsim :{}
        Maaş:{}
        Departman:{}
        Sorumlu olduğu kisi sayisi:{}""".format(self.isim, self.maas, self.departman, self.kisi_sayisi))

    def zam(self, zam_miktari):
        self.zam_miktari = zam_miktari
        self.maas += zam_miktari


#calisan = Calisan("Araç",1000,"Game developer")
yönetici = Yönetici("Ada",3000,"Cyber security",5)

#calisan.bilgileri_göster()
yönetici.bilgileri_göster()

print(yönetici)
del yönetici
print(yönetici)
