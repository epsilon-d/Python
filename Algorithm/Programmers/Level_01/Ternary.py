# Copyright 2021 epsilon-d. All rights reserved.
# https://programmers.co.kr/learn/courses/30/lessons/68935
# 프로그래머스 Level 1. 3진법 뒤집기

def solution(n):
    # 1단계: 3진법으로 바꿔준다.
    n3 = 0
    i = 0
    while True:
        n3 = n3 + (n % 3) * (10 ** i)
        if n == 0:
            break
        i = i + 1
        n = n // 3

    # 2단계: 앞뒤 반전
    r3 = str()
    n3 = str(n3)
    for j in range(len(n3)):
        r3 = r3 + n3[-j - 1]

    # 3단계: 10진법으로 바꿔준다.
    r10 = 0
    for k in range(len(r3)):
        r10 = r10 + (int(r3[-k - 1]) * (3 ** k))

    return r10
