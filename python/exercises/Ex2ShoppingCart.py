##In python, string.empty() is written as 'not string' OR 'len(string) == 0'
## !string.empty() = 'string' or 'len(string) != 0'
## to take off whitespace we do string.strip()



item = input("Welcome to YYY Shop\n What would you like to buy? ")
while not item:
    print(f"That item is not possible to buy at this store!")
    item = input("What would you like to buy? ")

quantity = -1

while quantity < 0 :
    if quantity != -1:
        print("\n That quantity is not possible! Try again")
    quantity = int(input(f"How many {item}(s)? : "))

price = -1.0

while price < 0 :
    if price != -1:
        print("\nThat price is not possible, try again")
    price = float(input(f"How much does that cost? : "))

print("You bought ", quantity, "x", item, "(s)!\n")
print("Your total was ", quantity*price, "€!")