# https://code.sasa.hs.kr/problem.php?id=1287

input_number = int(input())
time_list = input().split()

for i in range(len(time_list)):
    time_list[i] = float(time_list[i])    # int()가 아님.

time_list.sort()    # 같은 수 있을 수 있음.

destination = []

result = 0
if input_number == 2:
    print(sum(time_list))
elif input_number == 3:
    print(sum(time_list))
elif input_number == 4:
    if time_list[0] + time_list[2] < time_list[1] * 2:
        print(sum(time_list) + time_list[0])
    else:
        print(time_list[0] + 3 * time_list[1] + time_list[3])
elif input_number == 5:
    if time_list[0] + time_list[-2] < time_list[1] * 2:
        print(sum(time_list) + 2 * time_list[0])
    else:
        print(2 * time_list[0] + 3 * time_list[1] + time_list[2] + time_list[-1])
elif input_number == 6:
    if time_list[0] + time_list[-2] < time_list[1] * 2:
        print(sum(time_list) + 3 * time_list[0])
    else:
        if time_list[0] + time_list[2] < time_list[1] * 2:
            print(3 * time_list[0] + 3 * time_list[1] + time_list[2] + time_list[3] + time_list[-1])
        else:
            print(2 * time_list[0] + 5 * time_list[1] + time_list[3] + time_list[-1])
elif input_number == 7:
    if time_list[0] + time_list[-2] < time_list[1] * 2:
        print(sum(time_list) + 4 * time_list[0])
    else:
        if time_list[0] + time_list[-4] < time_list[1] * 2:
            print(4 * time_list[0] + 3 * time_list[1] + time_list[2] + time_list[3] + time_list[4] + time_list[-1])
        else:
            print(3 * time_list[0] + 5 * time_list[1] + time_list[2] + time_list[-3] + time_list[-1])
