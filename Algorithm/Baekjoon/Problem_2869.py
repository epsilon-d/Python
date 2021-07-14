# https://www.acmicpc.net/problem/2869

A, B, V = map(int, input().split())
result = (V - B) / (A - B)
if result == int(result):
    result = int(result)
else:
    result = int(result) + 1
print(result)
