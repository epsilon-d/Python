# https://kdt.elice.io/courses/12255/lectures/102877/materials/7
# [2기-02-04] 알고리즘 I (7/1)
# 실습 해설 2. 퀵정렬 구현하기

def quickSort(array):
    '''
    퀵정렬을 통해 오름차순으로 정렬된 array를 반환하는 함수를 작성하세요.
    '''
    if len(array) <= 1:
        return array

    pivot = array[0]

    left = getSmall(array[1:], pivot)
    right = getLarge(array[1:], pivot)

    return quickSort(left) + [pivot] + quickSort(right)


def getSmall(array, pivot):
    data = []

    for a in array:
        if a <= pivot:
            data.append(a)
    return data


def getLarge(array, pivot):
    data = []
    for a in array:
        if a > pivot:
            data.append(a)
    return data


def main():
    line = [int(x) for x in input("정렬할 수를 입력하세요 (예시:10 2 3 4 5 6 9 7 8 1): ").split()]

    print('정렬 결과:', *quickSort(line))


if __name__ == "__main__":
    main()
