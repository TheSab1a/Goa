number = int(input("12"))
for i in range(number - 1, 0, -1):
    print(i, end=", ")


odd_numbers = []

for i in range(1, 101):
    if i % 2 != 0:
        odd_numbers.append(i)

print(odd_numbers)


number = int(input("13"))

if number % 2 == 0:
    print("es ricxvi luwia")
else:
    print("es ricxvi kentia")

score = int(input("sheiyvane sheni qula (0-100): "))

if 90 <= score <= 100:
    print("Grade A")
elif 80 <= score <= 89:
    print("Grade B")
elif 70 <= score <= 79:
    print("Grade C")
elif 60 <= score <= 69:
    print("Grade D")
elif 0 <= score <= 59:
    print("Grade F")
else:
    print("arasowri qula sheiyvane!")



num = 16
while num <= 57:
    print(num)
    num += 1


    count = 0
while count < 5:
    print("Hello world")
    count += 1