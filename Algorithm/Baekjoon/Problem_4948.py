# https://www.acmicpc.net/problem/4948

prime_list = []
for i in range(2, 246913):
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

while True:
    n = int(input())
    cnt = 0
    if n == 0:
        break
    for m in range(len(prime_list)):
        if prime_list[m] <= n:
            continue
        if prime_list[m] > n * 2:
            break
        cnt = cnt + 1
    print(cnt)
