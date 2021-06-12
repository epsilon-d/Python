#연습문제 #8: 성적의 평균

print("종료하려면 음수를 입력하시오")

i = 0
sum_num = 0
grade = 0

while grade >= 0:
    grade = int(input("성적을 입력하시오: "))
    if grade < 0:
        break
    sum_num = sum_num + grade
    i = i + 1

aver = sum_num / i

print("성적의 평균은 %.2f입니다." % aver)
