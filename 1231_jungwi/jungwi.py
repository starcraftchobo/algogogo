# import sys
# sys.stdin = open("input.txt", "r")

# 가독성이 구리구리.. 양해바람돠

def jungwi_travel(n):
    # 길이가 2이면 자식 노드가 없음 ex) (7 E) (8 S)
    if len(nodes[n-1]) == 2:            # nodes에서 n번째의 인덱스는 n-1
        print(nodes[n-1][1], end='')    # 자기 넘버에 해당하는 알파뱃
        return                          # 재귀 끝!
    # 길이가 3이면 왼쪽 노드 자식이 잇음 ex) (4 O 8)
    elif len(nodes[n-1]) == 3:
        jungwi_travel(int(nodes[n-1][2]))   # 왼쪽 노드 자식 먼저 돌고
        print(nodes[n-1][1], end='')        # 자기 알파뱃 출력
    # 길이가 4면 양쪽 자식들이 다 잇음 ex) (1 W 2 3) (2 F 4 5)
    else:
        jungwi_travel(int(nodes[n - 1][2])) # 왼
        print(nodes[n-1][1], end='')        # 자기
        jungwi_travel(int(nodes[n - 1][3])) # 오


# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, 11):
    N = int(input())
    nodes = [list(input().split()) for _ in range(N)]

    print(f'#{test_case}', end=' ')
    jungwi_travel(1)
    print()