# https://www.acmicpc.net/problem/4153
# 직각삼각형

while True:
    length = list(map(int, input().split()))
    if length[0] == 0:
        break
    length.sort()
    if length[0] ** 2 + length[1] ** 2 == length[2] ** 2:
        print("right")
    else:
        print("wrong")
