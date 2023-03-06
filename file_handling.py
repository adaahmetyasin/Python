def not_hesapla(satir):
    satir = satir[:-1]
    liste = satir.split(":")
    ögrenciAdi = liste[0]
    notlar = liste[1].split(',')

    not1 = int(notlar[0])
    not2 = int(notlar[1])
    not3 = int(notlar[2])

    ortalama = (not1 + not2 + not3) / 3

    if ortalama >= 90 and ortalama <= 100:
        harf = "AA"
    elif ortalama >= 80 and ortalama <= 89:
        harf = "BA"
    elif ortalama >= 70 and ortalama <= 79:
        harf = "BB"
    elif ortalama >= 60 and ortalama <= 69:
        harf = "CB"
    elif ortalama >= 50 and ortalama <= 59:
        harf = "CC"
    else:
        harf = "FF"
    
    return ögrenciAdi + ":" + harf + "\n"

def notlari_oku():
    with open("sinav_notlari.txt","r",encoding="utf-8") as file:
        for satir in file:
            print(not_hesapla(satir))

def not_gir():
    ad = input('Ogrenci adi: ')
    soyad = input('Ogrenci soyadi: ')
    not1 = input('not 1:')
    not2 = input('not 2:')
    not3 = input('not 3:')

    with open("sinav_notlari.txt","a",encoding="utf-8") as file:
        file.write(ad + ' ' + soyad + ':' + not1 + ',' + not2 + ',' + not3 + '\n')

def not_kayitet():
    with open("sinav_notlari.txt","r",encoding="utf-8") as file:
        liste =[]

        for i in file:
            liste.append(not_hesapla(i))
        
        with open("sonuclar.txt","w",encoding="utf-8") as file2:
            for i in liste:
                file2.write(i)

while True:
    islem = input("1- Notlari oku\n2- Not gir\n3- Notlari kayit et\n4- Exit\n")

    if islem == "1":
        notlari_oku()
    elif islem == "2":
        not_gir()
    elif islem == "3":
        not_kayitet()
    else:
        break