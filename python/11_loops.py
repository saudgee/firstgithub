# While loop

x = 0
while (x <= 15):
    print(x)
    x = x + 1

for x in range(5,10):
    print(x)

# Array
days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
for d in days:
    if (d == "Fri"):continue # Skips d
    print(d)

for d in days:
    if (d == "Fri"):break # loop stops
    print(d)