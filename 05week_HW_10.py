#연습문제 #10: 도깨비 방망이

cost = int(input("주머니 사용료는? "))
multi = int(input("한 번 두드리면 불어나는 돈의 배수는? "))
times = int(input("방망이를 치려는 횟수는? "))
need = int(input("필요한 돈은 얼마? "))

initial = 0

for x in range(0, times, 1):
    initial = need + cost
    initial = initial / multi
    need = initial

print("처음에 넣어야 할 돈: %d" % initial)
