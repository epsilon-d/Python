#연습문제 #9: 임금계산

time = int(input("근무 시간을 입력하시오: "))
wage = int(input("시간 당 임금을 입력하시오: "))

if time > 40:
    time2 = time - 40
    total_wage = 40 * wage + time2 * 1.5 * wage
    print("총 임금은 ",total_wage+"원 입니다.")
else:
    total_wage = time * wage
    print("총 임금은 ",total_wage,"원 입니다.")
