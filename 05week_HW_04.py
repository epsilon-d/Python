#연습문제 #4: 화면에 다각형 그리기

import turtle as t

num_1 = int(input("다각형의 면의 수를 입력하시오: "))
num_2 = int(input("다각형의 한 변의 길이를 입력하시오: "))

angle = 360/num_1

for x in range(0, num_1, 1):
    t.forward(num_2)
    t.right(angle)
