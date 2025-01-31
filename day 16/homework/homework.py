a = True
b = False

if a or b:
    print("ერთი მაინც მართალია")

a = True
b = True

if a and b:
    print("ორივე მართალია!")

age=8 # შეცვალე ბავშის ასაკით



if 6 <= 12:

    print("ბავშვი 6-დან 12 წლამდეა")


A = True
B = False

# NOT A (De Morgan: A -> (A or A) and (A or A))
not_A = (A or A) and (A or A) and (A or A)  # შედეგი ისევ Aა, ამიტომ ვიყენებთ შემობრუნებას
not_A = not_A or not_A  # ახლა A დარჩება იგივე
not_A = not_A and not_A  # საბოლოოდ მივიღებთ NOT A-ს

# NOT B (იგივე მეთოდით)
not_B = (B or B) and (B or B) and (B or B)
not_B = not_B or not_B
not_B = not_B and not_B

print("A-ის საწინააღმდეგო:", not_A)
print("B-ის საწინააღმდეგო:", not_B)

