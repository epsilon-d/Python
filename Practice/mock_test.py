# https://programmers.co.kr/learn/courses/30/lessons/42840

def solution(answers):
    people = [[1, 2, 3, 4, 5], [2, 1, 2, 3, 2, 4, 2, 5], [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]]
    solution_list = [0, 0, 0]
    
    for i in range(len(people)):
        if len(answers) > len(people[i]):
            people[i] = people[i] * ((len(answers) // len(people)) + 1)
        for j in range(len(answers)):
            if answers[j] == people[i][j]:
                solution_list[i] = solution_list[i] + 1

    answer = []

    for k in range(len(people)):
        if solution_list[k] == max(solution_list):
            answer = answer + [k+1]
    return answer
