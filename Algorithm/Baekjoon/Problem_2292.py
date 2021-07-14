# https://www.acmicpc.net/problem/2292

number = int(input())

six = []
i = 0
while True:
    num = (i * (i + 1)) * 3
    six.append(num)
    i = i + 1
    if num > 10 ** 9:
        break

result = 0
for j in range(len(six)):
    if number - 1 <= six[j]:
        result = j
        break
result = result + 1

print(result)
