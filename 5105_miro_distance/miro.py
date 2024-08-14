# 출발~도착까지 최소 칸수, 경로가 없으면 0
# bfs는 갈림길에서 유용
#

dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]

def bfs(a, b, N):                  # 시작 좌표
    q = [a, b] # 큐 생성
    visited = [[0] * N for _ in range(N)]
    visited[b][a] = 1

    while q:
        x = q.pop(0)
        y = q.pop(0)
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < N and 0 <= ny < N and miro[ny][nx] == 0 and visited[ny][nx] == 0:
                q.append(nx)
                q.append(ny)
                visited[ny][nx] = visited[y][x] + 1
            elif 0 <= nx < N and 0 <= ny < N and miro[ny][nx] == 3:
                return visited[y][x] -1
            else:
                continue
    return 0
            # 디큐하면서 가다가
        # 큐가 비면 0
        # 3 만나면 visited 퉤


import sys
sys.stdin = open("sample_input.txt", "r")


T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    N = int(input())
    miro = [list(map(int, input())) for _ in range(N)]

    for i in range(N):
        for j in range(N):
            if miro[i][j] == 2:
                y = i
                x = j   # y, x
                break
    a = bfs(x, y, N)
    print(f'#{test_case}', a)