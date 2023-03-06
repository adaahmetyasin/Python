def check_password(password):
    import re

    if len(password) < 8:
        raise Exception ("Parola en az 8 karakter icermelidir.")
    elif not re.search("[a-z]",password):
        raise Exception ("Parola kücük harf icermelidir.")
    elif not re.search("[A-Z]",password):
        raise Exception ("Parola büyük harf icermelidir.")
    elif not re.search("[0-9]",password):
        raise Exception ("Parola rakam icermelidir.")
    elif not re.search("[@_*?!'^#]",password):
        raise Exception ("Parola alpha numeric karakter icermelidir.")
    elif  re.search("\s",password):
        raise Exception ("Parola bosluk icermemelidir.")
    else:
        print("Gecerli password.")

password1 = "12345678a*"

try:
    check_password(password1)
except Exception as ex:
    print(ex)
else:
    print("gecerli parola.")
finally:
    print("validation tamamlandi.")