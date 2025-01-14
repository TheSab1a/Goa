def check_entry(age, has_license):
    if age >= 18 and has_license:
        return "შეგიძლიათ შეხვიდეთ ქვეყანაში!"
    else:
        return "დაშვება უარყოფილია პირობები არ არის დაკმაყოფილებული"

# მომხმარებლისგან მონაცემების მიღება
try:
    age = int(input("12"))
    has_license = input("გაქვთ მართვის მოწმობა? (დიახ/არა): ").strip().lower()

    if has_license == "დიახ":
        has_license = True
    elif has_license == "არა":
        has_license = False
    else:
        raise ValueError("გთხოვთ, სწორად მიუთითეთ დიახ ან არა.")

    # შედეგის ჩვენება
    result = check_entry(age, has_license)
    print(result)

except ValueError as e:
    print(f"შეცდომა: {e}")







def check_discount(amount, is_vip):
    if amount > 100 or is_vip:
        return "თქვენ მიიღებთ ფასდაკლებას"
    else:
        return "ფასდაკლება არ ვრცელდება."

# მომხმარებლისგან მონაცემების მიღება
try:
    amount = float(input("1742(ლარში): "))
    is_vip = input("ხართ თუ არა VIP მომხმარებელი? (დიახ/არა): ").strip().lower()

    if is_vip == "დიახ":
        is_vip = True
    elif is_vip == "არა":
        is_vip = False
    else:
        raise ValueError("გთხოვთ სწორად მიუთითეთ დიახ ან არა.")

    # შედეგის ჩვენება
    result = check_discount(amount, is_vip)
    print(result)

except ValueError as e:
    print(f"შეცდომა: {e}")




def control_heating(temperature):
    if temperature < 10 or temperature > 30:
        return "გათბობა აქტიურდება!"
    else:
        return "გათბობა გამორთულია."

# მომხმარებლისგან ტემპერატურის შეყვანა
try:
    temperature = float(input("45(°C): "))
    
    # შედეგის ჩვენება
    result = control_heating(temperature)
    print(result)

except ValueError:
    print("45")





def check_access(has_student_card, has_teacher_permission):
    if has_student_card or has_teacher_permission:
        return "შეგიძლიათ სკოლაში შესვლა!"
    else:
        return "შესვლა აკრძალულია!"

# მომხმარებლისგან მონაცემების მიღება
try:
    has_student_card = input("გაქვთ სტუდენტური ბარათი? (დიახ/არა): ").strip().lower()
    has_teacher_permission = input("გაქვთ მასწავლებლის ნებართვა? (დიახ/არა): ").strip().lower()

    # სტრიქონების გარდაქმნა ბულურ მნიშვნელობად
    if has_student_card == "დიახ":
        has_student_card = True
    elif has_student_card == "არა":
        has_student_card = False
    else:
        raise ValueError("გთხოვთ, სწორად მიუთითეთ დიახ ან არა.")

    if has_teacher_permission == "დიახ":
        has_teacher_permission = True
    elif has_teacher_permission == "არა":
        has_teacher_permission = False
    else:
        raise ValueError("გთხოვთ, სწორად მიუთითეთ დიახ ან არა.")

    # შესვლის სტატუსის დადგენა
    result = check_access(has_student_card, has_teacher_permission)
    print(result)

except ValueError as e:
    print(f"შეცდომა: {e}")
