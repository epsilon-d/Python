# 1~10을 담는 리스트를 만들어 봅시다.
_list = [i for i in range(1, 11)]
print('1 번째 문제 결과: ', ' '.join(map(str, _list)))

# 2, 4, 6, 8, 10, ... 20을 담는 리스트를 만들어 봅시다.
_list = [i * 2 for i in range(1, 11)]
print('2 번째 문제 결과: ', ' '.join(map(str, _list)))

# 주어진 리스트를 받아 3의 배수인 값만 저장하는 리스트를 만들어 봅시다.
target_list = [2, 4, 6, 8, 10, 12]
_list = [i for i in target_list if i % 3 == 0]
print('3 번째 문제 결과: ', ' '.join(map(str, _list)))

# 값이 두개 들어있는 튜플을 담은 리스트를 받아 리스트를 생성하되, 튜플 내부의 값을 뒤집어서 저장하세요.
target_list = [(1, 2), (3, 4), (5, 6), (7, 8)]
_list = [(y, x) for x, y in target_list]
print('4 번째 문제 결과: ', ' '.join(map(str, _list)))

# 주어진 리스트를 그대로 담되, 15가 넘어가는 값은 15로 저장하는 리스트를 만들어 봅시다.
target_list = [1, 5, 11, 16, 24, 10]
_list = [x if x < 15 else 15 for x in target_list]
print('5 번째 문제 결과: ', ' '.join(map(str, _list)))
