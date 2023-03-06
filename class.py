class UCUS():
    havayolu = "THY"

    def __init__(self, kod, kalkis_yeri, varis_yeri, yolcu_sayisi, koltuk_sayisi):
        self.kod = kod
        self.kalkis = kalkis_yeri
        self.varis = varis_yeri
        self.yolcu = yolcu_sayisi
        self.koltuk = koltuk_sayisi

    def anons(self):
        return "{} seferli yolculugumuz {}-{} arsında {} kisiyle yola cikacaktir.".format(
            self.kod,
            self.kalkis,
            self.varis,
            self.yolcu
        )
    def koltuk_sayisi(self):
        return self.koltuk - self.yolcu

    def bilet_satis(self, satilan_bilet_adedi = 1):
        self.yolcu += satilan_bilet_adedi
        self.koltuk_sayisi()
        print(f"{satilan_bilet_adedi} adet bilet satilmistir, kalan bilet adedi:{self.koltuk_sayisi()}")
    def bilet_iptal(self, iptal_bilet_adedi = 1):
        self.yolcu -= iptal_bilet_adedi
        self.koltuk_sayisi()
        print(f"{iptal_bilet_adedi} adet bilet iptal edilmistir, kalan bilet adedi:{self.koltuk_sayisi()}")



ucus1 = UCUS("THY221", "İstanbul", "Erzurum", 125, 150)
ucus1.bilet_iptal()
