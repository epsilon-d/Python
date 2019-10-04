#연습문제 #3: 구구단 출력

num = int(input("출력할 단을 입력하시오: "))

for x in range(1, 10, 1):
    print("%d * %d = %d" % (num, x, num*x))
