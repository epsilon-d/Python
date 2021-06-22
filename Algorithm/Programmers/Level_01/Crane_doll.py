# https://programmers.co.kr/learn/courses/30/lessons/64061

def solution(board, moves):
    answer = 0
    basket = []

    for a in range(len(moves)):
        for b in range(len(board)):
            c = board[b][(moves[a] - 1)]
            if c != 0:
                basket.append(c)
                board[b][(moves[a] - 1)] = 0
                break
        if len(basket) > 1:
            if basket[-1] == basket[-2]:
                answer += 2
                del(basket[-1])
                del(basket[-1])
    return answer
