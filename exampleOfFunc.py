def again(word, number):
    for i in range(0, number):
        print(word)
again('merhaba', 12)


def donustur(*params):
    liste = []

    for param in params:
        liste.append(param)
    return liste

listem = donustur(12,24,54,26,"Ahmet","Ada",".")
print(listem)


def asalbul(x, y):
    for sayi in range(x, y+1):
        if sayi > 1:
            for i in range(2, sayi):
                if (sayi % i == 0):
                    break
            else:
                print(sayi)
sayi1 = int(input("1. sayıyı girin: "))
sayi2 = int(input("2. sayiyi girin: "))

asalbul(sayi1, sayi2)


def tambolen(x):
    tambolenler = []
    for i in range(1,x + 1):
        if x % i == 0:
            tambolenler.append(i)
    return tambolenler
print(tambolen(20))