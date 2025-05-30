# Slicing გამოიყენება სტრიქონის ან სიების ნაწილებად დაჭრისთვის
# vwert striqons[start:end] da igebt im nawils rac iwyeba start-idan da mtavrdeba end-indeqsamde


surname = input("khurtsidze")

if surname.endswith("tsidze"):
    print("Hello")
elif surname.endswith("dze"):
    print("Bye")

surname = "khurtsidze"
print(surname[:])



age = 13  
counter = age

while counter <= age * 3:
    print( "counter"  "year")
    counter += 1



my_list = [13, 29, 38, 47, 56, 64, 77, 81, 92, 103]

even_index_elements = my_list[0::2]
print("1:3", even_index_elements)
