# https://www.acmicpc.net/problem/2839

N = int(input())

result = -1

a = int(N/5)
b = int(N/3)

for i in range(a, -1, -1):
    for j in range(b+1):
        if N == 5 * i + 3 * j:
            result = i + j
            break
        if N < 5 * i + 3 * j:
            break
    if result != -1:
        break

print(result)
