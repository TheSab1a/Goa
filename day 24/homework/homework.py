for num in range(101):  
    if num in [15, 27, 67, 32, 99, 93]:  
        continue  
    print(num)


num = 0  # ცვლადი, რომელიც იწყება 0-დან

while True: 
    num += 1 

    if num == 23: 
        break  

print("cikli dasrulda num =", num)


my_list = [10, 20, 30, 40, 50]  

my_list.append(60)  
my_list.append(70)  

print(my_list)  

matrix = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12]
]

value = matrix[1][2]

print("ამოღებული მნიშვნელობა:", value)
