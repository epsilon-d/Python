# https://www.acmicpc.net/problem/1193

x = int(input())

num_list = []
i = 1
while True:
    num = int(i * (i + 1) / 2)
    num_list.append(num)
    i = i + 1
    if num > 10 ** 7:
        break

for j in range(len(num_list)):
    if x <= num_list[j]:
        temp = j + 2  # temp = 분모, 분자의 합
        temp2 = x - num_list[j - 1]  # temp2 = 그 대각선에서 몇 번째인지
        break

if x == 1:
    print("1/1")
elif temp % 2 == 0:
    # 큰 수에서 점점 작아짐.
    if temp2 == 0:
        print(f"{temp - 1}/{1}")
    else:
        print(f"{temp - temp2}/{temp2}")
else:
    # 작은 수에서 점점 커짐.
    if temp2 == 0:
        print(f"{1}/{temp - 1}")
    else:
        print(f"{temp2}/{temp - temp2}")
