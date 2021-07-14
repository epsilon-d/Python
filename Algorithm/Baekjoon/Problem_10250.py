# https://www.acmicpc.net/problem/10250

T = int(input())

for i in range(T):
    H, W, N = map(int, input().split())
    room = N / H
    if room == int(room):
        room = int(room)
        if room < 10:
            room = "0" + str(room)
        else:
            room = str(room)
    else:
        room = int(room) + 1
        if room < 10:
            room = "0" + str(room)
        else:
            room = str(room)
    floor = N % H
    if floor == 0:
        floor = H

    number = str(floor) + room
    print(number)
