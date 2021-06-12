#연습문제 #7: 자리수의 합

num = int(input("정수를 입력하시오: "))
sum_num = 0
i = 1
k = 0

while k < num:
    x = num // 10**i
    y = num - x*(10**i)
    y = y - sum_num
    y = y // (10**(i-1))
    k = k + y*(10**(i-1))
    i = i + 1
    sum_num = sum_num + y

print("자리수의 합은 %d입니다." % sum_num)
