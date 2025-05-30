# 1) punqcia aris kodis bloki romelsac aqvs saxeli da shegvidzlia gamoviyenot

# 2) funqciis argumenti aris is romelsac vazlevt funqcias mis shignit dasamushavleblad


# punkciebis argumentebi
#  print()  მიიღებს erti argumentitac
#  int()  მიიღებს 1 arguments da გადაჰყავს mtel ricxvad magram ver sheiyvans striqons romelic ar aris ricxvi
#  float()  მიიღებს 1 arguments da გადაჰყავს atwilad
#  str()  მიიღებს 1 arguments da გადაჰყავს striqonad
#  type()  abrunebs monacemis tipis saxels
#  input()  მიიღებს 1 arguments da abrunebs momxmareblis sheyvanil striqons



start = int(input("enter youre number"))
stop = int(input("enter youre number"))

cube_sum = 0
for i in range(start, stop + 1):
    cube_sum += i ** 3

print("100", cube_sum)

real_password = "The_Sab1a"

user_input = input("enter youre number")

while user_input != real_password:
    print("incorrect password")
    user_input = input("enter youre user")

print("wvdoma mushaobs!")


