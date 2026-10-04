name = input("Enter your name: ")

#The input function returns data under the datatype of string
age = int(input("How old are you: "))

print(f"Hello {name}, who is {age} years old")
birthday = -3
while birthday != 0 and birthday != 1:
    birthday = int(input(f"Is it your bithday today? (0/1): "))
if birthday:
    age += 1
    print(f"You are now {age} years old")