import math

radius = float(input("Enter the radius of the circle: "))
def checkRadius(r):
    if(r < 0):
        print("\nThis radius is not real, please try again: ")

circ = 2 * math.pi * radius
area = (circ /2) * radius
volume = (4.0/3)* math.pi * pow(radius, 3)

print(f"The circumference is {round(circ, 2)}")
print("The area is ", round(area, 2))
print("If this was a 3D sphere, it would have a volume of ", round(volume, 2))