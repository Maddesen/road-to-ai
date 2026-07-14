# Aufgabe: 
# Lege eine Integer-Variable meine-variable mit dem Wert 5 an,
# caste diese in eine Float-Variable und gebe sie aus

# Integer-Variable
my_variable = 5
print("My variable:", my_variable)

my_variable_str = str(my_variable)
print("My Variable as String:", my_variable_str)

my_variable_int = int(my_variable)
print("My variable as Integer:", my_variable_int)

# if-else-query

# variables

x = 1.7
y = 3.5

if x >= y:
    print("x ist größer oder gleich y")
else:
    print("x ist kleiner als y")

# if-else-quere with or/and

# variables

x = 15
y = 5
z = 9

if x >= y and x >= z:
    print("x ist größter oder gleich y und z")

if y < x or y > z:
    print("y ist kleiner als x oder größer als z")

# Loops

for x in range(1, 11):
    print("x=", x)

y = 10
while y > 0:
    print(" y is:", y)
    y -= 1    