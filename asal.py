sayi = int(input('sayi:' ))

asalmi = True

if sayi <= 1:
    asalmi = False

for i in range(2, sayi):
    if sayi % i == 0:
        asalmi = False

if asalmi:
    print("sayi asaldir")
else:
    print("sayi asal değildir")