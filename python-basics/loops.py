# Loops in Python

# for-loop: interact list
numbers = [1, 2, 3, 4, 5]
for number in numbers:
    print("Number from List:", number)

# for-loop: interact range

for i in range(1, 6):
    print("Aktueller Wert von i:", i)

# while-loop: as long as a condition is true

count = 0
while count < 5:
    print("count is:", count)
    count = count + 1 # or: count += 1 / zählt hoch

# while-loop: with one condition
n = 10
while n > 0:
    print("n is:", n)
    n -= 2 # n um 2 verringern zählt runter
