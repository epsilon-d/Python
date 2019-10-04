#연습문제 #1: 카운트다운

num = int(input("숫자를 입력하시오: "))

for x in range(num, -1, -1):
    print("Count %d" % x)