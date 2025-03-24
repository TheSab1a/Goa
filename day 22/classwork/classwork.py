for num in range(2, 101, 2):
    print(num)


for num in range(1, 101, 2):
    print(num)

sum_numbers = sum(range(1, 101))
print(sum_numbers)

sum_even = sum(range(2, 101, 2))
print(sum_even)
 
sum_odd = sum(range(1, 101, 2))
print(sum_odd)



num = 1
while num <= 5:
    print(num)
    num += 1


num = 1
total = 0
while num <= 10:
    total += num
    num += 1
print(total)


num = int(input("sheiyvanet ricxvi: "))  # მომხმარებლისგან რიცხვის მიღება
i = 1  # ცვლადი, რომელიც დაიწყებს გადინებას 1-დან
while i <= num:
    print(i)
    i += 1

correct_password = "1234"  # სწორი პაროლი

while True:
    password = input("sheiyvanet paroli: ")  # მომხმარებლისგან პაროლის მიღება
    if password == correct_password:
        print("paroli sworia!")
        break  # პაროლი სწორია, ვასრულებთ ციკლს
    else:
        print("araswori paroli")


