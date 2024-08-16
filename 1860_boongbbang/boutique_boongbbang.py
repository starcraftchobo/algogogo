import sys
sys.stdin = open("test2.txt", "r")
# 진기가 파는 붕어빵은 겉은 바삭! 속은 말랑! 한입 물면 팥 앙금이 주르륵 흘러 입안에서 춤을 추며,
# 절로 어릴 적 호호 불며 먹었던 뜨거운 붕어빵의 추억이 떠올라 눈물이 나오게 되는 최고급 붕어빵
# 진기야 제발 친구하자

def bubble_sort(arr):
    for i in range(len(arr)):
        for j in range(len(arr)-i-2):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

def sell(M, K, clients):
    bbang = [0] * 11111
    howmany = 0
    a = clients.pop
    for i in range(M, a):
        if i % M == 0:
            howmany += K
    howmany = howmany - len(clients) -1
    if howmany < 0:
        return 'Impossible'
    else:
        return 'Possible'


T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    N, M, K = map(int, input().split())           # 사람 수, 붕빵나오는 시간, 붕빵나오는 개수
    clients = list(map(int, input().split()))
    bubble_sort(clients)                            # [1, 2, 3...]크기순으로 정렬
    # print(clients)
    # bbang = [0] * 11111                             # [0, 0, ...]
    #
    # howmany = 0                                     # 남아있는 붕빵 개수

    # for i in range(M, 11111, M):
    #     howmany += K
    #     for j in range(M):
    #         if i+j < 11111:
    #             bbang[i+j] = howmany
    # print(bbang)

    print(f'#{test_case}', sell(M, K, clients))
