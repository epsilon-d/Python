# 모의 코딩테스트 1회 1번: 울타리

def main():
    N, M, K = map(int, input().split())
    min_m = 1000
    max_m = 0
    min_n = 1000
    max_n = 0

    for i in range(K):
        m, n = map(int, input().split())
        max_m = max(max_m, m)
        min_m = min(min_m, m)
        max_n = max(max_n, n)
        min_n = min(min_n, n)

    length = 2 * ((max_m - min_m + 2) + (max_n - min_n + 2))
    print(length)


if __name__ == "__main__":
    main()
