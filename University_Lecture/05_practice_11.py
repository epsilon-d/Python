#연습#11: 3의 배수만 건너뛰고 더하기

num = 0

for x in range(1, 101, 1):
    if x % 3 == 0:
        continue
    num = num + x

print("1~100의 합계(3의 배수 제외): %d" % num)
