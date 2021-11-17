k = int(input())

x = input().split()
for a in range(len(x)):
    x[a] = int(x[a])

y = input().split()
for b in range(len(y)):
    y[b] = int(y[b])

for i in range(k):
    for j in range(len(x)):
        x[j] + y