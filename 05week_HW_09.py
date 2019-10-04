#연습문제 #9: Up and Down

import random

random_number = random.randrange(1, 100)

print("1부터 100 사이의 숫자를 맞추시오.")

i = 1

while 1 == 1:
    num = int(input("숫자를 입력하시오: "))
    if num == random_number:
        break
    else:
        if num < random_number:
            print("높음!")
            i = i + 1
        else:
            print("낮음!")
            i = i + 1

print("축하합니다. 시도회수 = %d" % i)
