#연습문제 #11: 행사 중에 마신 총 우유병 개수

price = int(input("한 병의 가격을 입력하시오: "))
money = int(input("현재 소지하고 있는 금액을 입력하시오: "))

bottle = money // price

sum_num = bottle

while bottle > 0:
    bottle = bottle // 3
    sum_num = sum_num + bottle

print("총 마신 우유병 수: %d" % sum_num)
