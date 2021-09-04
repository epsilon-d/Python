# https://www.acmicpc.net/problem/3009
# 네 번째 점

answer = []
spot = []
for i in range(3):
    spot.append(list(map(int, input().split())))

if spot[0][0] == spot[1][0]:
    answer.append(spot[2][0])
elif spot[0][0] == spot[2][0]:
    answer.append(spot[1][0])
else:
    answer.append(spot[0][0])

if spot[0][1] == spot[1][1]:
    answer.append(spot[2][1])
elif spot[0][1] == spot[2][1]:
    answer.append(spot[1][1])
else:
    answer.append(spot[0][1])

print(answer[0], answer[1])
