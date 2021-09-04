# https://www.acmicpc.net/problem/9020

T = int(input())

prime_list = []
for i in range(2, 10000):
    stop = 0
    if i < 100:
        k = i
    else:
        k = int(i ** (1/2)) + 1
    for j in range(2, k):
        if i % j == 0:
            stop = 1
            break
    if stop == 0:
        prime_list.append(i)
print(prime_list)

for i in range(T):
    n = int(input())
    print(n)
