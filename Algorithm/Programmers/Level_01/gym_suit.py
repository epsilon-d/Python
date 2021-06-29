# Copyright 2021 epsilon-d. All rights reserved.
# https://programmers.co.kr/learn/courses/30/lessons/42862
# 프로그래머스 Level 1. 체육복

def solution(n, lost, reserve):
    for i in range(len(lost)):
        for j in range(len(reserve)):
            if lost[i] == reserve[j]:
                lost[i] = -1
                reserve[j] = -3
    for k in range(len(lost)):
        for a in range(len(reserve)):
            if lost[k] - 1 == reserve[a]:
                lost[k] = -1
                reserve[a] = -3
            elif lost[k] + 1 == reserve[a]:
                lost[k] = -1
                reserve[a] = -3
    lost_number = 0
    for m in range(len(lost)):
        if lost[m] == -1:
            lost_number = lost_number + 1
    answer = n - len(lost) + lost_number
    return answer
