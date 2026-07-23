# If-Else query

# Variables
x = 10
y = 5

# simple if-condition
if x > y:
    print("x ist größer als y")

# if-else-query
if x <= y:
    print("x ist kleiner als y")
else:
    print("x ist nicht kleiner als y")

# if-elif-else query
if x == y:
    print("x ist gleixh y")
elif x > y:
    print("x ist größer als y")
else:
    print("y ist kleiner als y")

# new varibale
z = 15

# if-and link: both must be true
if x > y and x < z:
    print("x ist größer als y und kleiner als z")

# if-or link: one must be true
if x < y or x < z:
    print("x ist entweder kleiner als y oder kleiner als z")
    