# class Kitap():
#     pass

# kitap = Kitap() #__init__ metodu
# print(kitap) #__str__ metodu   <__main__.Kitap object at 0x7fb063e3df70>
# len(kitap) #__len__ metodu
# del kitap #__del__ metodu

class Kitap():
    
    def __init__(self,adı,yazarı,sayfa_sayisi,tür):
        print("init fonksiyonu")
        self.adı = adı
        self.yazarı = yazarı
        self.sayfa_sayisi = sayfa_sayisi
        self.tür = tür
    
    def __str__(self):
        return "İsim: {}\nYazar: {}\nSayfa sayisi: {}\nTürü: {}".format(self.adı, self.yazarı, self.sayfa_sayisi, self.tür)
    
    def __len__(self):
        return self.sayfa_sayisi
    
    def __del__(self):
        print("kitap objesi silindi.")

kitap = Kitap("İstanbul Hatırası","AHMET ÜMİT",561,"POLİSİYE")
print(kitap)
print(len(kitap))
del(kitap)