# 연습문제 #2: 홀수의 합

sum_num = 0

for x in range(501, 1000, 1):
    if x % 2 == 0:
        continue
    sum_num = sum_num + x
print("500에서 1000까지 홀수의 합: %d" % sum_num)
