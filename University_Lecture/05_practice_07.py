#연습#7: 합계 구하기

num = int(input("어디까지 더할 것인지 입력하시오: "))
i = 0
sum_num = 0

while i <= num:
    sum_num = sum_num + i
    i = i + 1
print("1부터 %d까지의 정수의 합 = %d" % (num, sum_num))
