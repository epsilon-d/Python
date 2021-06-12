#연습#9: 성적의 평균

i = 0

while i == 0:
    num_1 = int(input("첫 번째 정수를 입력하시오: "))
    if num_1 == 0:
        print("0을 입력해서 반복문을 탈출했습니다.")
        break
    num_2 = int(input("두 번째 정수를 입력하시오: "))
    if num_2 == 0:
        print("0을 입력해서 반복문을 탈출했습니다.")
        break
    sum_num = num_1 + num_2
    print("%d + %d = %d" % (num_1, num_2, sum_num))
