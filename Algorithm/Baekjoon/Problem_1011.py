# https://www.acmicpc.net/problem/1011

T = int(input())

result = 0

for i in range(T):
    x, y = map(int, input().split())
    distance = y - x
    j = 1
    sum_number = 0
    while True:
        sum_number += j
        if distance <= sum_number * 2:
            # result = (j * 2) - 1 or result = j * 2
            if (sum_number * 2) - distance < j:
                result = j * 2
            else:
                result = (j * 2) - 1
            break
        j = j + 1
    print(result)
