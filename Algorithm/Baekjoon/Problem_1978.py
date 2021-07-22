# https://www.acmicpc.net/problem/1978

N = int(input())
number = list(map(int, input().split()))

prime_number = []

result = 0

for a in range(2, 1001):
    stop = 0
    for b in range(2, a):
        if a % b == 0:
            stop = 1
            break
    if stop == 0:
        prime_number.append(a)

for i in number:
    if i in prime_number:
        result += 1

print(result)
