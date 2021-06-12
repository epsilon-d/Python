#연습#3: 합계 구하기

sum_num = 0
num = int(input("어디까지 더할 것인지 입력하시오: "))
for x in range(1, num+1, 1):
    sum_num = sum_num + x
print("1부터 %d까지의 정수의 합 = %d" % (num, sum_num))
