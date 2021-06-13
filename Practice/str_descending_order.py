# Arrange strings in descending order
# https://programmers.co.kr/learn/courses/30/lessons/12917

def solution(s):
    answer = str()
    answer_list = list(s)
    answer_list.sort()
    answer_list.reverse()
    for i in range(len(answer_list)):
        answer = answer + answer_list[i]
    return answer
