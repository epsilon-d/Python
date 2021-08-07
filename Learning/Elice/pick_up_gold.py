# 2번 금 줍기 문제

def pick_up():
    N = int(input())
    gold = list(map(int, input().split()))
    gold_3 = []
    for i in range(N - 2):
        gold_3.append(sum(gold[i:i + 3]))

    result = max(gold_3)
    max_idx = gold_3.index(max(gold_3))
    gold_3[max_idx] = 0

    # 만약 최대값과 두 번째로 큰 세 수의 합의 인덱스가 이미 3칸 이상 떨어진 경우, 굳이 모든 경우의 수를 나열할 필요 없이 두 묶음의 합을 출력
    if abs(gold_3.index(max(gold_3)) - max_idx) >= 3:
        print(result + max(gold_3))
    #        print(gold_3.index(max(gold_3)))
    else:  # 만약 최대값과 두 번째로 큰 세 수의 합의 인덱스가 3칸 미만으로 떨어져있는 경우,
        # 모든 경우의 수를 나열하여 왼 손과 오른 손의 합 중 최대값 출력
        gold_3[max_idx] = result
#        print(gold_3)
        sum_left_right = []
        for j in range(len(gold_3) - 3):
            for k in range(j + 3, len(gold_3)):
                sum_left_right.append(gold_3[j] + gold_3[k])
        print(max(sum_left_right))


#    print(gold)
#    print(gold_3)

pick_up()
