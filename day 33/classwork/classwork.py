# 1) კომენტარის სახით ახსენით რა არის ფუნქცია და რაში გამოიყენება იგი.

# ფუნქცია არის კოდის ბლოკი რომელსაც აქვს კონკრეტული ამოცანა


def miisalme(name):
    print(f"gamarjoba, {name}!")

# ფუნქციის გამოსაძახებლად:
miisalme("saba")


saxelebi = ["vano", "mevludi", "saba", "luka", "dachi"]


def damateba_siaze():
    axali_saxeli = input("enter youre name ")
    saxelebi.append(axali_saxeli)
    print("sia:", saxelebi)



saxelebi2 = ["vano", "mevludi", "saba", "luka", "dachi"]

def damateba_indeksit():
    saxeli = input("enter youre name")
indeks = int(input("enter indeksis "))
if indeks > len(saxelebi2):
print("indeksi agemateba siis zomas!")
else:
saxelebi2.insert(indeks, saxeli)
print("sia", saxelebi2)



