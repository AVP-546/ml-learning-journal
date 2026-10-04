height = -1.0
length = -1.0

while height <= 0:
    height = float(input("Enter the rectangle's height: "))

while length <= 0:
    length = float(input("Enter the rectangle's length: "))

area = length * height

print(f"The rectangle's area is {area} units ")