import sys
sys.stdin = open("sample_input.txt", "r")

def search(x, y):
    stack = [(x,y)]
    visited[x][y] = 1
    # 언제까지탐색할까 --> 3나올때까지?
    while stack:
        x, y = stack.pop()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            # 미로 범위 벗어나지 않는지 &&
            if 0 <= nx < N and 0 <= ny < N and nemo[nx][ny] != 1 and visited[nx][ny] != 1:
                if nemo[nx][ny] == 3:
                    return 1                        # 1 반환 후 종료
                # 3이 아니라면
                stack.append((nx, ny))
                # 방문 처리
                visited[nx][ny] = 1
    return 0

dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]
'''
for dx, dy in [(-1, 0) (0, -1), (1, 0), (0, 1)]
'''

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    N = int(input())

    nemo = [list(map(int, input()))  for _ in range(N)]
    visited = [[0] * N for _ in range(N)]

    # find 2 == 출발점
    for i in range(N):
        for j in range(N):
            if nemo[i][j] == 2:
                print(f'#{test_case} {search(i,j)}')

