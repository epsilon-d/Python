#연습#5: 주사위의 합

num = 0

for x in range(1, 7, 1):
    for y in range(6, 0, -1):
        if x+y == 6:
            print("%d %d" % (x,y))
            num = num + 1
print("2개의 주사위 합이 6이 되는 경우의 수: %d개" % num)
