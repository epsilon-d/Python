# This program is a program that print prime number less than a given number.

# The reason importing math is calculating square root.
import math

num: int = int(input("Please input any integer number: "))
num = num + 1
y = 2
print(2)

for x in range(2, num, 1):
    for y in range(2, int(math.sqrt(x) + 1), 1):
        if x % y == 0:
            break
    if x % y != 0:
        print("%d" % x)
