# Practice #7: Sum of Digit
# This program calculates the sum of the number of digits of the integer.

num = int(input("Please input any integer number: "))

sum_num = 0

while num > 0:
    x = num % 10
    sum_num = sum_num + x
    num = num // 10

print("Sum of digit is %d." % sum_num)
