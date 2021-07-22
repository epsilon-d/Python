# https://www.acmicpc.net/problem/2581

M = int(input())
N = int(input())

prime_number = []

if M == 1:
    M = 2

for i in range(M, N + 1):
    stop = 0
    for j in range(2, i):
        if i % j == 0:
            stop = 1
            break
    if stop == 0:
        prime_number.append(i)

# print(prime_number)

if len(prime_number) == 0:
    print(-1)
else:
    print(sum(prime_number))
    print(min(prime_number))
