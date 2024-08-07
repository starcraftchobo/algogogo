# import sys
# sys.stdin = open("input.txt", "r")
#
def DFS(p1, p2):
    stack = [path1[0], path2[0]]            # 0에서 출발하는 두 갈림길
    visited = [0] * (100)

    while stack:
        current = stack.pop()               # 현재 조사할 노드
        if current == 0:                    # 현재 값이 0이면
            continue
        elif current == 99:
            return 1
            break
        if visited[current] == 0:           # 방문 표시
            visited[current] == 1
            #탐색
            if visited[path1[current]] == 0:            # 방문하지 않았다면
                stack.append(p1[current])
            if visited[path2[current]] == 0:            # 방문하지 않았다면
                stack.append(p2[current])               # 다음 방문지 저장
    return 0


T = 10
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    tc, N = map(int, input().split())
    arr = list(map(int, input().split()))
    path1 = [0] * 100
    path2 = [0] * 100
    for i in range(N):
        if path1[arr[i*2]] == 0:
            path1[arr[i*2]] = arr[i*2+1]
        else:
            path2[arr[i*2]] = arr[i*2+1]
    # print(path2)
    # print(path1)

    print(f'#{test_case}',DFS(path1, path2))

