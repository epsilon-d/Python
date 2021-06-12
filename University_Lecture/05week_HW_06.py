#연습문제 #6: 3의 배수의 합

i = 2
sum_num = 0

while i < 100:
    if i % 3 == 0:
        sum_num = sum_num + i
    i = i + 1

print("1부터 100 사이의 모든 3의 배수의 합은 %d입니다." % sum_num)
