class Yazilimci():
    def __init__(self,isim,soyisim,numara,maas,diller):
        self.isim = isim
        self.soyisim = soyisim
        self.numara = numara
        self.maas = maas
        self.diller = diller
    
    def bilgileri_goster(self):
        print("""
        Yazılımcının bilgileri

        Adı : {}

        Soyadı : {}

        Numarasi : {}

        Maasi : {}

        Bildigi diller : {}

        """.format(self.isim, self.soyisim, self.numara, self.maas, self.diller))

    def zam_yap(self,zam_miktari):
        self.zam_miktari = zam_miktari

        print("\tZam yapiliyor .. \n")

        self.maas += zam_miktari

        print("""
        Yazilimcinin yeni maasi : {}
        """.format(self.maas))
    
    def zam_orani_hesapla(self):
        oran = (self.zam_miktari*100)/(self.maas-self.zam_miktari)
        print(oran)

    def dil_ekle(self,yeni_dil):
        self.yeni_dil = yeni_dil
        print("Diller ekleniyor")
        self.diller.append(yeni_dil)
        print("""
        Bildigi diller : {}

        """.format(self.diller))


yazilimci1 = Yazilimci("Ahmet Yasin","Ada",1306200018,2000,["C","C++","Python","Javascript"])

yazilimci1.bilgileri_goster()
# yazilimci1.zam_yap(1000)
# print(yazilimci1.maas)
# yazilimci1.zam_orani_hesapla()
yazilimci1.dil_ekle("Java")

print(yazilimci1)