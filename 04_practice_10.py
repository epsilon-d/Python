#연습문제 #10: 윤년

year = int(input("연도를 입력하시오: "))

if year%400==0:
    print("윤년입니다.")
elif year%100==0:
    print("평년입니다.")
elif year%4==0:
    print("윤년입니다.")
else:
    print("평년입니다.")