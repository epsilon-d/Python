#연습문제 #7: 사과구입

apple = input("사과의 상태를 입력하시오: ")
if apple == "신선":
    cost = int(input("사과 1개의 가격을 입력하시오: "))
    if cost < 1000:
        print("사과를 10개 산다.")
    else:
        print("사과를 5개 산다.")
else:
    print("사과를 사지 않는다.")