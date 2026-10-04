import math

a = float(input("Please enter the a side: "))
b = float(input("Please enter the b side: "))

c = math.sqrt((a**2) + (b**2))

print(f"The hypothenuse is {round(c,2)}")