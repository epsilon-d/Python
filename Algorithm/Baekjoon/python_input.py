# https://www.acmicpc.net/problem/15552
# 빠르게 입력받기

import sys

T = int(input())

for i in range(T):
    A, B = map(int, sys.stdin.readline().split())
    print(A + B)
