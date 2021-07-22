# https://www.acmicpc.net/problem/4948

while True:
    n = int(input())
    if n == 0:
        break
    prime_number = []
    for i in range(n + 1, (2 * n) + 1):
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
            prime_number.append(i)
    print(len(prime_number))
