# https://programmers.co.kr/learn/courses/30/lessons/42748

def solution(array, commands):
    solution_array = list()
    for i in range(len(commands)):
        new_array = array[commands[i][0] - 1:commands[i][1]]
        new_array.sort()
        solution_array.append(new_array[commands[i][2] - 1])
    return solution_array
