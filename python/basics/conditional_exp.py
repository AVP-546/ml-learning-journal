#Conditional expressions are equivalent to using if-else statement
    #Fomula: X if condition else Y

num = float(input("Enter a number: "))

X = 10 if num > 0 else 2 ###

print(X)
print("Positive" if num > 0 else "Negative") ###

print("Even" if num % 2 == 0 else "Odd") ###