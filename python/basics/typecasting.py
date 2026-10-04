name = "AVP"
is_student = True
gpa = 3.2
age = 45

print(type(is_student), type(name), type(gpa), type(age))

gpa = int(gpa)
age = float(age)
print(gpa) #Truncation of gpa
print(age) #Extension of age

##Typecasting a string into a boolean variable, the boolean will only be 0 if the string is empty. May be useful for checking input

