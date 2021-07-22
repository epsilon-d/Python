# https://www.acmicpc.net/problem/1929

M, N = map(int, input().split())

if M == 1:
    M = 2

for i in range(M, N + 1):
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
        print(i)
