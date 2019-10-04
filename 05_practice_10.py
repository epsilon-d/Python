#연습#10: 누적합계가 1000 이상이 되는 시작 시점

num = 0

for x in range(1, 101, 1):
    num = num + x
    if num > 1000:
        print("1~100의 합에서 최초로 1000이 넘는 위치: %d" % x)
        break
