x = input().split()
for a in range(len(x)):
    x[a] = int(x[a])

k = 0

for i in range(1, len(x)):
    b = x[:i]
    c = x[i:]
    d = max(b) - min(b)
    e = max(c) - min(c)
    print(x[:i], x[i:])
    print(d+e)
    if d+e > k:
        k = d+e

print(k)
