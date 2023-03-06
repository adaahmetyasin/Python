from cgitb import reset
from turtle import turtles


liste = ["1","2","5a","10b","abc","10","50"]
#1-) listedeki sayısal değerleri yazdırınız.
"""
 for i in liste:
     try:
         result = int(i)
         print(result)
     except ValueError:
         continue
"""

#2-)Kullanıcı 'q' değerini girmedikçe aldığınız her inputun
# sayı olması gerekir yoksa hata mesajı verin.
"""
while True:
    sayi = input("sayi: ")
    if sayi == 'q':
        break
    try:
        result = float(sayi)
        print("girdiğiniz sayi: ",result)
    except:
        print("lütfen sayi giriniz:")
        continue
"""

#3-) Girilen parola içinde türkce karakter hatası veriniz.

"""
parola = input("parola: ")
turkish_character = 'şçğüöıİ'

for i in parola:
    if i in turkish_character:
        raise TypeError('Parola turkce karakter iceremez.')
    else:
        pass

print("gecerli parola")
"""

#4-) Faktoriyel fonksiyonu oluşturup fonksiyona gelen
#değer için hata mesajı verin.
"""
def faktoriyel(x):
    x = int(x)

    if x < 0:
        raise ValueError('Negatif Deger')

    result = 1

    for i in range(1, x + 1):
        result *= i
    
    return result

for x in [5, 10, 20, '3a', '-10']:
    try:
        y = faktoriyel(x)
        
    except ValueError as err:
        print(err)
        continue
    print(y)
"""

