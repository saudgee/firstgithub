# Logical operators
# Equal to                          ==
# Not equal to                      !=
# Less than                         <
# Less than and equal to            <=
# Greater than                      >
# Greater than and equal to         >=

print(4==4)
print(4!=4)
print(4>3)
print(3>6)
print(4<=5)
print(5>=4)


#  application of logical operators

hammad_age = 4
age_at_school = 5
print(hammad_age == age_at_school)

# input function and logical operator

age_at_school = 5
hammad_age = input("How old is Hammad? ")
print(type(hammad_age))
hammad_age = int(hammad_age)
print("Type of hammad_age is ", type(hammad_age))
print(hammad_age >= age_at_school)