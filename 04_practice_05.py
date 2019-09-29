#연습문제 #5: 인터넷 쇼핑몰

cost = int(input("구입 금액을 입력하시오: "))

if cost > 100000:
    cost2 = cost * 0.95
    print("지불 금액은 ",cost2,"입니다.")
else:
    print("지불 금액은 ",cost,"입니다.")