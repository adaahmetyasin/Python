from errno import ESHLIBVERS
import sqlite3
from tkinter.tix import Select # Sqlite'yı dahil ediyoruz

con = sqlite3.connect("kütüphane.db") # Tabloya bağlanıyoruz.

cursor = con.cursor() # cursor isimli değişken veritabanı üzerinde işlem yapmak için kullanacağımız imleç olacak.

def tablo_oluştur():
    cursor.execute("CREATE TABLE IF NOT EXISTS kitaplık (İsim TEXT, Yazar TEXT, Yayınevi TEXT, Sayfa_Sayısı INT)") # Sorguyu çalıştırıyoruz.
    con.commit() # Sorgunun veritabanı üzerinde geçerli olması için commit işlemi gerekli.
#tablo_oluştur()

def deger_ekle(İsim,Yazar,Yayınevi,Sayfa_Sayısı):
    cursor.execute("INSERT INTO kitaplık VALUES('Olasılıksız','Adam Fawer','April',627)")
    con.commit()

#deger_ekle('İsim', 'Yazar', 'Yayınevi', 'Sayfa_Sayısı')


def kullanıcıdan_veri_al(isim,yazar,kitapevi,sayfa_sayısı):
    cursor.execute("INSERT INTO kitaplık VALUES(?,?,?,?)",(isim,yazar,kitapevi,sayfa_sayısı))
    con.commit()

# isim = input("İsim:")
# yazar = input("Yazar:")
# kitapevi = input("Kitapevi:")
# sayfa_sayısı = int(input("Sayfa sayısı:"))

# kullanıcıdan_veri_al(isim,yazar,kitapevi,sayfa_sayısı)

def  veri_al():
    cursor.execute("Select * from kitaplık")
    liste  = cursor.fetchall()
    print("Kitaplık tablosunun bilgileri..")
    for i in liste:
        print(i)
#veri_al()

def veri_al2():
    cursor.execute("Select İsim,Yazar from kitaplık")
    liste = cursor.fetchall()
    print("Kitaplık tablosunun bilgileri..")
    for i in liste:
        print(i)
#veri_al2()

def veri_al3(yayınevi):
    cursor.execute("Select * from kitaplık where Yayınevi = ?",(yayınevi,))
    liste = cursor.fetchall()    
    print("Kitaplık tablosunun bilgileri..")
    for i in liste:
        print(i)
#veri_al3('Everest')

def verileri_guncelle(eski_yayınevi,yeni_yayınevi):
    cursor.execute("update kitaplık set Yayınevi = ? where Yayınevi = ?",(yeni_yayınevi,eski_yayınevi))
    con.commit()
#verileri_guncelle("İŞ BAnkası","İŞ BANKASI")

def verileri_guncelle2(eski_kitapadı,yeni_kitapadı):
    cursor.execute("update kitaplık set İsim = ? where İsim = ?",(yeni_kitapadı,eski_kitapadı))
    con.commit()
#verileri_guncelle2("İnsan Ne İLe Yaşar","İnsan Neyle Yaşar")

def veri_sil(yazar):
    cursor.execute("delete from kitaplık where Yazar = ?",(yazar,))
    con.commit()
#veri_sil("oscar wilde")

def verileri_getir():
    cursor.execute("Select * from kitaplık")
    liste = cursor.fetchall()
    for i in liste:
        print(i)
verileri_getir()

con.close() # Bağlantıyı koparıyoruz.    