# https://www.acmicpc.net/problem/10951
# EOF: End of file

import sys

while True:
    try:
        A, B = map(int, sys.stdin.readline().split())
        print(A + B)
    except EOFError:
        break
