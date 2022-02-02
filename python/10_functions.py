# Defining a function
# 1
def print_codanics():
    print("We are learning Python on Codanics YouTube channel")
    print("We are learning Python on Codanics YouTube channel")
    print("We are learning Python on Codanics YouTube channel")
    print("We are learning Python on Codanics YouTube channel")

print_codanics()

# 2
def print_codanics():
    text = ("We are learning Python on Codanics YouTube channel")
    print(text)
    print(text)
    print(text)
    print(text)
    print(text)

print_codanics()

# 3
def print_codanics(text):
    print(text)
    print(text)
    print(text)
    print(text)
    print(text)

print_codanics("We are learning Python on Codanics YouTube channel!")    

# 4
def print_codanics():
    text = input("Type something I will repeat it 5 times!")
    print(text)
    print(text)
    print(text)
    print(text)
    print(text)

print_codanics()

# 5
def school_calculator():
    name = input("What is the name of student? ")
    age = int(input("What is the age of student? "))
    age_for_school = 5
    if age == age_for_school:
        print(name, "can join the school")
    elif age > age_for_school:
        print(name, "can join the school in the class according to his age group")
    elif age <= 3:
        print(name, "is too young to join the school")
    else:
        print(name,"can not join the school")

school_calculator()

# 6 Defining a function of future

def future_age(age):
    new_age = age + 20
    return new_age

your_age = int(input("Type your age "))
future_predicted_age = future_age(your_age)
print("After 20 years your age will be", future_predicted_age, "years")
