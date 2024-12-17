# მომხმარებლის დაბადების წლის შეყვანა
birth_year = input("2012")

# დაბადების წლის integer-ად გადაქცევა
birth_year = int(2012)

# ახსნა
print("თქვენი დაბადების წელი გადავაქციე integer-ად რათა მოქმედებები შევასრულოთ მაგალითად: ასაკის დათვლა.")

# მომხმარებლისგან username-ის შეყვანა
username = input("შეიყვანეთ თქვენი username: ")

# მომხმარებლისთვის მისალმების ბეჭდვა
print(f"Hello, {username}!")


# კონკატენაცია არის ტექსტის (სტრიქონის) შეერთების პროცესი
# ის გამოიყენება ორ ან მეტ string-ს შორის, რომ შექმნას ერთი ტექსტი

# ორი ცალკე string ცვლადი
first_name = "jamal"   # პირველი string
last_name = "king"     # მეორე string

# კონკატენაციის გამოყენება
full_name = first_name + " " + last_name  # "+" აერთებს ტექსტებს და ქმნის სრულ სახელს

# შედეგის დაბეჭდვა
print(full_name)  # შედეგი: "Jamal king"

# დამატებითი მაგალითი: ტექსტის და ცვლადის შერწყმა
age = 24
greeting = "Hello, my name is " + full_name + " and I am " + str(age) + " years old."
print(greeting)
# შედეგი: "Hello, my name is Jamal king and I am 24 years old."


age = 25  # integer

price = 19.99  # float

number = 3 + 4  # complex

name = "Jamal"  # string

fruits = ["apple" "banana" "cherry"]  # list

numbers = range(5)  # range(0, 5)

value = None  # NoneType