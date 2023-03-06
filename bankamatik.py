AhmetHesap = {
    'ad': 'Ahmet Ada',
    'hesapNo': '12345678',
    'bakiye': 2500,
    'kredi': 1000
}

def paraCek(hesap, miktar):
    print(f"Merhaba {hesap['ad']}")

    if (hesap['bakiye'] >= miktar):
        hesap['bakiye'] -= miktar
        print("Paranizi alabilirsiniz.")
        print(f"Kalan bakiyeniz {hesap['bakiye']} TL'dir ve {hesap['kredi']} tl kredi bulunmaktadir.")
    else:
        toplam = hesap['bakiye'] + hesap['kredi']

        if (toplam >= miktar):
            krediKullanimi = input('Krediden kullanilsin mi?(e/h)')

            if krediKullanimi == 'e':
                krediKullanimi = miktar - hesap['bakiye']
                hesap['bakiye'] = 0
                hesap['kredi'] -= krediKullanimi 
                print("Paranizi alabilirsiniz")
                print(f"Kalan bakiyeniz {hesap['bakiye']} ve kalan krediniz {hesap['kredi']}")
            else:
                print(f"{hesap['hesapNo']} nolu hesabinizda {hesap['bakiye']} tl bakiye ve {hesap['kredi']} tl kredi bulunmaktadir.")
        else:
            print("Bakiyeniz yetersiz")
            print(f"{hesap['hesapNo']} nolu hesabinizda {hesap['bakiye']} tl bakiye ve {hesap['kredi']} tl kredi bulunmaktadir.")

paraCek(AhmetHesap, 200)
paraCek(AhmetHesap, 2100)
paraCek(AhmetHesap, 300)
paraCek(AhmetHesap, 200)
paraCek(AhmetHesap, 2000)
