print("Python" == "Python")       # True
print("Code" == "code")           # False
print("ChatGPT" == "ChatGPT")     # True
print("Hello" == "World")         # False
print("123" == "123")             # True
print("abc" == "ABC")             # False
print("Test" == "Test ")          # False (სივრცე ითვლება)
print("" == "")                   # True
print(" " == "")                  # False
print("OpenAI" == "openai")       # False





print("Python" != "Java")         # True
print("Test" != "test")           # True
print("123" != "1234")            # True
print("ChatGPT" != "ChatGPT")     # False
print("Hello" != "hello")         # True
print(" " != "")                  # True
print("" != "")                   # False
print("apple" != "banana")        # True
print("Code" != "Code ")          # True
print("Equal" != "Equal")         # False







print("banana" > "apple")         # True (ანბანურობის მიხედვით)
print("apple" > "Apple")          # True (რეგისტრი ითვლება)
print("zebra" > "antelope")       # True
print("Hello" > "Hi")             # False
print("Test" > "Tested")          # False
print("Gamma" > "Alpha")          # True
print("a" > "A")                  # True
print("123" > "122")              # True
print("Beta" > "alpha")           # False
print("Python3" > "Python2")      # True





print("apple" < "banana")         # True
print("Apple" < "apple")          # True
print("antelope" < "zebra")       # True
print("Hi" < "Hello")             # False
print("Tested" < "Test")          # False
print("Alpha" < "Gamma")          # True
print("A" < "a")                  # True
print("122" < "123")              # True
print("alpha" < "Beta")           # False
print("Python2" < "Python3")      # True





# ორი ცვლადი ერთნაირი მნიშვნელობით
string1 = "HelloWorld"
string2 = "HelloWorld"

# შედარებები
print(string1 == string2)  # True - ტოლია
print(string1 != string2)  # False - არ არის ტოლი
print(string1 > string2)   # False - არც ერთი არ არის მეტი, რადგან ერთნაირია
print(string1 < string2)   # False - არც ერთი არ არის ნაკლები, რადგან ერთნაირია