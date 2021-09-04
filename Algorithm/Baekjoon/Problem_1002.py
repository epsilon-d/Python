# https://www.acmicpc.net/problem/4948
# 터렛

T = int(input())
for i in range(T):
    x1, y1, r1, x2, y2, r2 = map(int, input().split())
    if x1 == x2 and y1 == y2:
        if r1 == r2:
            print(-1)
            continue
        print(0)
        continue
    if x1 == x2:
        if y1 >0 y2:
            y1