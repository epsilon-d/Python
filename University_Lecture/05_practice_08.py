#연습#8: 팩토리얼 계산

num = int(input("정수를 입력하시오: "))
fac_num = 1
i = 1

while i <= num:
    fac_num = fac_num * i
    i = i + 1

print("%d! = %d" % (num, fac_num))
