# Copyright 2021 epsilon-d. All rights reserved.
# https://programmers.co.kr/learn/courses/30/lessons/42576
# 프로그래머스 레벨1. 완주하지 못한 선수

def solution(participant, completion):
    participant.sort()
    completion.sort()
    for i in range(len(completion)):
        if participant[i] != completion[i]:
            answer = participant[i]
            return answer
    answer = participant[-1]
    return answer

