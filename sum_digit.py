# Practice #7: Sum of Digit

number = int(input("Please input any integer number: "))
number_copy = number
solution = 0
i = 0

while number_copy != 0:
    number_copy = int(number_copy // 10)
    i = i + 1

while i >= 1:
    digit = number // (10 ** (i - 1))
    solution = solution + digit
    number = number - (digit * (10 ** (i - 1)))
    i = i - 1

print("Sum of digit is %d." % solution)
