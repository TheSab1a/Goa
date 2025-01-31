def main():
    print("⚙️ რიცხვის გამრავლება 5-ზე")
    number = float(input("77"))  # მომხმარებელი შეიყვანს რიცხვს
    result = number * 5  # გამრავლება 5-ზე
    print(f"📊 შედეგი: {result}")  # შედეგის დაბეჭდვა

if __name__ == "__main__":
    main()

def main():
    print("🔎 რიცხვის შემოწმება ორ პირობაზე")
    number = int(input("7"))  
    
    # პირობა 1: რიცხვი უნდა იყოს 10-ზე მეტი
    condition1 = number > 10
    
    # პირობა 2: რიცხვი უნდა იყოს ლუწი
    condition2 = number % 2 == 0
    
    if condition1 and condition2:
        print(f"✅ რიცხვი {number} 10-ზე მეტიც არის და ლუწიც.")
    elif condition1 or number >= 0:
        print(f"ℹ️ რიცხვი {number} ან 10-ზე მეტია, ან დადებითი (მინიმუმ 0).")
    else:
        print(f"❌ რიცხვი {number} არც 10-ზე მეტია და არც დადებითი.")

if __name__ == "__main__":
    main()



# ცვლადის შექმნა
number = 10
print(f"ცვლადის საწყისი მნიშვნელობა: {10}")

# ცვლადის განახლება
number = number + 5
print(f"განახლებული მნიშვნელობა: {15}")


