# შეყვანილი რიცხვის მიღება
number = int(input("77"))

# პიროვნების შემოწმება
if 5 < number < 15 and number != 10:
    print("რიცხვა 5-სა და 15-ს შორის არის მაგრამ არა 10-ის ტოლი")
else:
    print("რიცხვა არ აკმაყოფილებს მოთხოვნებს.")




# მომხმარებლის მონაცემების მიღება
name = input("შეიყვანეთ თქვენი სახელი: ")
age = int(input("შეიყვანეთ თქვენი ასაკი: "))

# პიროვნების შემოწმება
if age > 18 and name.startswith("A"):
    print("თქვენთვის შესაფერისი არსით.")
else:
    print("თქვენ არ აკმაყოფილებთ მოთხოვნებს.")




    # შეყვანილი რიცხვის მიღება
number = int(input("17"))

# პიროვნების შემოწმება
if number % 2 == 0 or number % 3 == 0:
    print("რიცხვი არის ლუწი ან 3-ის გამყოფი.")
else:
    print("რიცხვი არც ლუწია არც 3-ის გამყოფი")






    def check_numbers(a, b):
    if a >= 100 or b >= 100:
        return "ერთ-ერთი რიცხვი 100-ის ტოლი ან მასზე მეტია."
    else:
        return "არცერთი რიცხვი არ არის 100-ის ტოლი ან მასზე მეტი."

# მაგალითი
number1 = int(input("შეიყვანეთ პირველი რიცხვი: "))
number2 = int(input("შეიყვანეთ მეორე რიცხვი: "))

result = check_numbers(number1, number2)
print(result)
