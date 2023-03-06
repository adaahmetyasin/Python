from math import *
text = """
1-) Kişi sayısını bulma. 
2-) Duvar sayısını bulma. 
3-) Süreyi hesaplama.
Lütfen yapoacağınız işlem numarasını giriniz:
"""
print(text)
islem = int(input())
while islem < 1 or islem > 3:
    print(text)
    islem = int(input())

if islem == 1:
    print("Duvar sayisini girin:")
    duvar = int(input())
    print("Süreyi girin(dk):")
    süre = int(input())
    kisi = duvar / (15/400*süre)
    kisi = ceil(kisi)  #kisi sayısının kesirli olması mantığa aykırı olduğu için minimun sayıyı alıyoruz
    print("Gereken minimum kisi sayısı:" + str(kisi))

if islem == 2:
    print("Kisi sayisini girin:")
    kisi = int(input())
    print("Süreyi girin(dk):")
    süre = int(input())
    duvar = (15/400*süre) * kisi
    duvar = floor(duvar) #duvar sayısının kesirli olması mantığa aykırı olduğu için maksimum sayıyı alıyoruz
    print("Yapılabilecek maksimum duvar sayısı:" + str(duvar))

if islem == 3:
    print("Kisi sayisini girin:")
    kisi = int(input())
    print("Duvar sayisini girin:")
    duvar = int(input())
    süre = (400/15) * (duvar/kisi)
    print("İşin bitme süresi: " + str(süre) + " dk.")