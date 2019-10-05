# This program is a program that determines if a given number is prime.

num = int(input("Please input any integer number: "))

for x in range(2, num, 1):
    if num % x == 0:
        print("The number is not prime number.")
        exit()
print("The number is prime number.")
