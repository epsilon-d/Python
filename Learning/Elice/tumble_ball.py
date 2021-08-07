# 모의 코딩테스트 1회 3번 문제: 공 굴리기 문제

def main():
    N, M = map(int, input().split())
    arrow_list = []
    for i in range(N):
        arrow_list.append(list(map(int, input().split())))
    y, x = map(int, input().split())
    y = y - 1
    x = x - 1
    # print(arrow_list)

    record = [[y, x]]
    while True:
        if arrow_list[y][x] == 1:  # 위로 이동
            y = y - 1
            if y < 0:
                print(-1)
                break
        elif arrow_list[y][x] == 2:  # 좌로 이동
            x = x - 1
            if x < 0:
                print(-1)
                break
        elif arrow_list[y][x] == 3:  # 우로 이동
            x = x + 1
            if x >= M:
                print(-1)
                break
        else:  # 아래로 이동
            y = y + 1
            if y >= N:
                print(-1)
                break
        if [y, x] in record:
            rotation = len(record) - record.index([y, x])
            print(rotation)
            break
        record.append([y, x])
        # print(record)

    # 기존에 있던 곳을 다시 방문하면, 그 방문하는 회전 수를 계산하여


#    print(2)

if __name__ == "__main__":
    main()
