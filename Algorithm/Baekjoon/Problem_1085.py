# https://www.acmicpc.net/problem/1085
# 직사각형에서 탈출

x, y, w, h = map(int, input().split())

if x < w/2:
    length_x = x
else:
    length_x = w - x

if y < h/2:
    length_y = y
else:
    length_y = h - y

print(min(length_x, length_y))
