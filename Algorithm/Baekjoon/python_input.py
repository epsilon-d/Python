# https://www.acmicpc.net/problem/15552
# https://www.acmicpc.net/problem/11021
# https://www.acmicpc.net/problem/11022
# 빠르게 입력받기

import sys

T = int(input())

for i in range(T):
    A, B = map(int, sys.stdin.readline().split())
    print(f"Case #{i + 1}: {A} + {B} = {A + B}")
