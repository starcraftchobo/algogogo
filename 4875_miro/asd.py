dx = [-1, 1, 0, 0, ]  # 상하좌우
dy = [0, 0, -1, 1]
'''
for dx, dy in [(-1, 0),(1, 0),(0, -1),(0, 1)]:
'''


def search(x, y):
    stack = [(x, y)]
    visited[x][y] = 1
    while stack:
        x, y = stack.pop()
        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]
            # 미로의 범위를 벗어나지 않고, 벽이 아니고, 처음 방문하는 곳인 경우
            if 0 <= nx < N and 0 <= ny < N and maze[nx][ny] != 1 and visited[nx][ny] != 1:
                if maze[nx][ny] == 3:  # 출구 도착
                    return 1  # 1 반환 후 함수 종료
                # 3이 아니라면 스택에 추가, 방문체크
                stack.append((nx, ny))
                visited[nx][ny] = 1
    return 0


T = int(input())
for tc in range(1, T + 1):
    N = int(input())

    maze = [list(map(int, input().strip())) for _ in range(N)]
    visited = [[0] * N for _ in range(N)]

    # 2가 담긴 곳 == 출발점
    for i in range(N):
        for j in range(N):
            if maze[i][j] == 2:
                print(f'#{tc} {search(i, j)}')