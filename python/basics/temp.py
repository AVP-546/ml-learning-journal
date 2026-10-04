unit = input("Enter your unit of temperature measurement(C/F): ")
temp = float(input("Enter you temperature: "))

if(unit == 'F'):
    temp = (temp - 32)*(5/9)
    print(f"Your temperature in Fahrenheit is equivalent to {round(temp, 2)} degrees Celsius")
elif(unit == 'C'):
    temp = (temp * 9 / 5) + 32
    print(f"Your temperature in Celsius is equivalent to {round(temp, 2)} degrees Fahrenheit")
else:
    print("Your unit is not considered in this program")