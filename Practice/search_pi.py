iter_num = int(input("반복할 횟수: "))

pi = 0

for i in range(1, iter_num + 1):
    if i % 2 == 1:
        pi = pi + 1/(2*i-1)
    else:
        pi = pi - 1/(2*i-1)

pi = pi * 4

print(pi)
