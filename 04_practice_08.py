#연습문제 #8: 숫자 맞추기 문제

inference = int(input("추측 값을 입력하시오: "))

if inference == 50:
    print("축하합니다! 정답입니다.")
elif inference > 50:
    print("아닙니다. 추측 값보다 작습니다.")
else:
    print("아닙니다. 추측 값보다 큽니다.")