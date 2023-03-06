from os import readlink
from pyexpat import model
from re import A


class Araba():
    model = "Renault Megane"
    renk = "Siyah"
    beygir_gücü = 110
    silindir = 4
    def __init__(self):
        print("init fonk cagrıldı")
 
araba1 = Araba()
araba2 = Araba()

print(araba1.model)
# print(araba2.model)

# for i in dir(araba1):
#     print(i)