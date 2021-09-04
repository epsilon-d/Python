# https://www.acmicpc.net/problem/9020

T = int(input())

prime_list = []
for i in range(2, 10000):
    stop = 0
    if i < 100:
        k = i
    else:
        k = int(i ** (1/2)) + 1
    for j in range(2, k):
        if i % j == 0:
            stop = 1
            break
    if stop == 0:
        prime_list.append(i)
prime_list.remove(2)

even_number = dict()
for j in range(len(prime_list)):
    if prime_list[j] > 5000:
        break
    for k in range(j, len(prime_list)):
        a = prime_list[j]
        b = prime_list[k]
        if a + b > 10000:
            break
        even_number[a + b] = [a, b]

for i in range(T):
    n = int(input())
    if n == 4:
        print(2, 2)
        continue
    print(even_number[n][0], even_number[n][1])
