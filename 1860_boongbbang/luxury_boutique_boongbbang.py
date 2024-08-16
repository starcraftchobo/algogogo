# 진기가 파는 붕어빵은 겉은 바삭! 속은 말랑! 한입 물면 팥 앙금이 주르륵 흘러 입안에서 춤을 추며,
# 절로 어릴 적 호호 불며 먹었던 뜨거운 붕어빵의 추억이 떠올라 눈물이 나오게 되는 최고급 붕어빵
# 진기야 제발 친구하자
import sys
sys.stdin = open("input.txt", "r")

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    print(f'#{test_case}', end=' ')
    N, M, K = map(int, input().split())           # 사람 수, 붕빵나오는 시간, 붕빵나오는 개수
    clients = list(map(int, input().split()))
    max = 0                                         # 젤 늦게 오는 느림보
    for client in clients:
        if max < client:
            max = client

    howmany = -K                                    # 붕빵 개수

    # 붕빵이 나오는 한 주기씩 생각
    for i in range(0, max+M, M):
        # 최초 붕빵 0개, M초마다 따끈따끈 붕빵 출하
        howmany += K
        for client in clients:
            # 손님들이 i초부터 i+M초 사이에 있을때
            if i <= client < i+M:   # ex) 76 <= client(98, 79, 84, 100) < 108
                howmany -= 1
        if howmany < 0:                             # 내다팔 붕빵이 모자라면?!
            print('Impossible')                     # 샤따 내려
            break
    else:
        print('Possible')                           # for문을 모두 통과하면 장사가 원활했단 뜻
