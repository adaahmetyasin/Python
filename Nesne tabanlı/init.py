from nntplib import NNTPReplyError


class Araba():
    def __init__(self,model,renk,beygir_gücü,silinidir):

        print("init fonksiyonu cagrildi")
        self.model = model
        self.renk = renk
        self.beygir_gücü = beygir_gücü
        self.silindir = silinidir

araba1 = Araba("Renault","Gümüş",110,4)
araba2 = Araba("Mercedes","Siyah",150,4)

class Coin():
    def __init__(self,adı = "Bilgi yok",degeri = 0,sıralaması = 0):
        self.adı = adı
        self.degeri = degeri
        self.sıralaması = sıralaması
coin1 = Coin(degeri=1000)

print(coin1.adı,coin1.degeri,coin1.sıralaması)

