4.# Name, surname, and age input
name = input("saba")
surname = input("khurtsidze")
age = input("12")

# Printing name, surname, and age in a sentence
print(f"{name} {surname} is {age} years old.")

# Two numbers input from the user
num1 = float((77))
num2 = float((69))

# Mathematical operations
sum_result = num1 + num2
difference = num1 - num2
product = num1 * num2
if num2 != 0:
    division = num1 / num2
else:
    division = "Undefined (division by zero is not allowed)"

# Printing the results of the mathematical operations
print(f"\nThe numbers you entered are: {num1} and {num2}")
print(f"Their sum is: {sum_result}")
print(f"Their difference is: {difference}")
print(f"Their product is: {product}")
print(f"Their division result is: {division}")

# Email and password input
email = input("khurtsidze.saba@gmail.com")
password = input("SABAluka1405")

# Printing the email and password entered
print(f"khurtsidze.saba@gmail.com {email}")
print(f"SABAluka1405 {password}")


2.# მომხმარებლისგან სახლის, გვარის და ასაკის შეყვანა
name = input("saba")
surname = input("khurtsidze")
age = input("12")
# სახელი, გვარი და ასაკი წინადადებაში
print(f"{name} {surname} {age}")

num1 = float(("12"))
num2 = float(("77"))

# მათემატიკური ოპერაციები
sum_result = num1 + num2        # ჯამი
difference = num1 - num2        # სხვაობა
product = num1 * num2           # ნამრავლი
if num2 != 0:
    division = num1 / num2      # გაყოფა
else:
    division = "განუსაზღვრელია (ნულის გაყოფა არ შეიძლება)"  # ნულის გაყოფა

# შედეგების გამოტანა
print(f"\nშეყვანილი რიცხვებია: {num1} და {num2}")
print(f"მათი ჯამი: {sum_result}")
print(f"მათი სხვაობა: {difference}")
print(f"მათი ნამრავლი: {product}")
print(f"მათი განაყოფი: {division}")

5.# პირველი რიცხვის შეყვანა მომხმარებლისგან
num1 = float(("69"))  # input() იღებს მომხმარებლის მონაცემებს, ხოლო float() აქცევს მათ რიცხვად
# მეორე რიცხვის შეყვანა მომხმარებლისგან
num2 = float(("7"))  # იგივე, მაგრამ მეორე რიცხვისთვის

# მათემატიკური ოპერაციები

sum_result = num1 + num2        # ჯამი: პირველი რიცხვი და მეორე რიცხვი ერთმანეთს დაემატება
difference = num1 - num2        # სხვაობა: პირველი რიცხვი მეორედან გამოიჭრება
product = num1 * num2           # ნამრავლი: პირველი რიცხვი და მეორე რიცხვი ერთმანეთთან გამრავლდება

# თუ მეორე რიცხვი არ არის ნული, მაშინ გაყოფა იქნება. თუ მეორე რიცხვი ნულია, გამოვხატავთ შეტყობინებას.
if num2 != 0:
    division = num1 / num2      # გაყოფა: პირველი რიცხვი დაიყოფა მეორე რიცხვზე
else:
    division = "განუსაზღვრელია (ნულის გაყოფა არ შეიძლება)"  # თუ num2 = 0, მაშინ გაყოფა შეუძლებელია

# შედეგების გამოტანა
# გამოგვაქვს თითოეული მათემატიკური ოპერაციის შედეგი.
print(f"\nშეყვანილი რიცხვებია: {num1} და {num2}")  # აჩვენებს ორი შეყვანილი რიცხვი
print(f"მათი ჯამი: {sum_result}")  # აჩვენებს რიცხვების ჯამს
print(f"მათი სხვაობა: {difference}")  # აჩვენებს რიცხვების სხვაობას
print(f"მათი ნამრავლი: {product}")  # აჩვენებს რიცხვების ნამრავლს
print(f"მათი განაყოფი: {division}")  # აჩვენებს რიცხვების განაყოფს, თუ გაყოფა შესაძლებელია