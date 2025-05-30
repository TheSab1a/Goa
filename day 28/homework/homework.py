list1 = [2, 51, 11, 13, 51, 100]
positive_index = list1[:]  
print("positive index", positive_index)

negative_index = list1[-len(list1):]
print("negative index:", negative_index)


list1[-1] = 999
print("last element is different:", list1)

list1[4] = 777
print("5th element different", list1)


list2 = [
    0, 
    10, 
    20, 
    30, 
    40, 
    50,
    60, 
    70, 
    80, 
    90  
]
print("10 element list", list2)

first_three = list1[0:3]
last_three = list1[-3:]
middle_four = list1[1:5]  

print("first three:", first_three)
print("first three", last_three)
print("middle four", middle_four)


first_three_negative = list1[-6:-3]
last_three_negative = list1[-3:]
middle_four_negative = list1[-5:-1]

print("first three(negative three):", first_three_negative)
print("last three (negative index):", last_three_negative)
print("middle four (negative index):", middle_four_negative)


text = "Hello"
reversed_text = text[::-1]
print("reversed text", reversed_text)

