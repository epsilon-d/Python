#연습#4: 팩토리얼 계산

fac_num = 1

num = int(input("정수를 입력하시오: "))
for x in range(1, num+1, 1):
    fac_num = fac_num * x
print("%d! = %d" % (num, fac_num))
