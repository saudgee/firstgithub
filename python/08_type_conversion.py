x = 10
y = 10.2
z = "Hello"
print(type(x))
print(type(y))
print(type(z))

# implicit type conversion
x = x + y
print(x, "Type of x is", type(x))

#  explict type conversion
age = input("what is your age? ")
print(age, type(int(age)))
