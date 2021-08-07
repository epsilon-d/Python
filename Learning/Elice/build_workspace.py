# 모의 코딩테스트 1회 4번 문제: 사무실 짓기

def main():
    population = int(input())
    num_list = list(map(int, input().split()))
    distance_list = []

    avg = int(sum(num_list) / len(num_list))

    for i in range(max(1, avg - 49000), min(1000001, avg + 12000)):
        distance = 0
        for j in range(population):
            distance = distance + abs(num_list[j] - i)
            # print(i, distance)
        distance_list.append(distance)

    min_distance = min(distance_list)
    result = distance_list.count(min_distance)
    # print(distance_list)

    print(result)

if __name__=="__main__":
    main()
