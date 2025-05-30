

# len() – აბრუნებს სტრინგის სიგრძეს
len("hello")  # ➜ 5

# lower() – გარდაქმნის სტრინგს პატარა ასოებად
"HELLO".lower()  # ➜ "hello"

# upper() – გარდაქმნის სტრინგს დიდ ასოებად
"hello".upper()  # ➜ "HELLO"




# len() – აბრუნებს სიის ელემენტების რაოდენობას
len([1, 2, 3])  # ➜ 3

# append() – ამატებს ელემენტს სიის ბოლოს
my_list = []
my_list.append("item")  # ➜ ["item"]

# pop() – შლის ბოლო ელემენტს და აბრუნებს მას
my_list.pop()  # ➜ "item", სია გახდა []

# insert() – ამატებს ელემენტს კონკრეტულ პოზიციაზე
my_list.insert(0, "start")  # ➜ ["start"]

# remove() – შლის კონკრეტულ ელემენტს სიიდან
my_list.remove("start")  # ➜ []

# sort() – აწყობს სიას ზრდადობით
[3, 1, 2].sort()  # ➜ [1, 2, 3]

# reverse() – აბრუნებს სიას უკუღმა
[1, 2, 3].reverse()  # ➜ [3, 2, 1]

# index() – აბრუნებს ელემენტის ინდექსს სიაში
["a", "b", "c"].index("b")  # ➜ 1

# count() – ითვლის რამდენჯერ გვხვდება ელემენტი
["a", "b", "a"].count("a")  # ➜ 2





my_surname = "khurtsidze" 
user_surname = input("Enter your surname: ")  


if my_surname.lower() == user_surname.lower():
    print("our surnames are similar.")
else:
    print("We have different surnames.")



food = ["burger", "fries", "pizza", "soda"] 

food.pop()

food.append("salad")
food.append("fruit")

print(food)  # შედეგი: ['burger', 'fries', 'pizza', 'salad', 'fruit']



my_name = "Nika"  # ჩემი სახელი
user_name = input("Enter your name: ")  


my_first = my_name[0].lower()
my_last = my_name[-1].lower()
user_first = user_name[0].lower()
user_last = user_name[-1].lower()

if my_first == user_first and my_last == user_last:
    print(2)
elif my_first == user_first or my_last == user_last:
    print(1)
else:
    print(0)
