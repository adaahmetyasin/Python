print("Oyuncu kaydetme programı")
ad = input("Oyuncunun adı:")
soyad = input("Oyuncunun soyadı:")
takım = input("Oyuncunun takımı:\n")

bilgiler = [ad,soyad,takım]

print ("bilgiler kaydediliyor...")

print("Oyuncu adı: {}\nOyuncu soyadı: {}\nOyuncu takımı: {}\n".format(bilgiler[0],bilgiler[1],bilgiler[2]))

print("bilgiler kaydedildi")