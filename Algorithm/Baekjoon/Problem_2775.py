# https://www.acmicpc.net/problem/2775

T = int(input())

for i in range(T):
    k = int(input())
    n = int(input())

    population = []
    for a in range(k):
        population.append([])
        for b in range(n):
            population[a].append([])
#    print(population)

    for j in range(k):
        for m in range(n):
            if j == 0:
                population[j][m] = m + 1
            else:
                population[j][m] = sum(population[j-1][:m+1])
#        print(population)
    number = sum(population[k-1])
    print(number)
