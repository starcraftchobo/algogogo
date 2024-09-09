import sys
sys.stdin = open("sample_input.txt", "r")
'''
델타 탐색으로
1 못가고
visited 만들어서 한번 간곳은 못가게 하고
pop해서 3이면 return 1
'''
def search(r, c):
    stack = [(r, c)]
    visited[r][c] = 1
    # 언제까지탐색할까 --> 3나올때까지?
    while stack:
        y, x = stack.pop()
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            # 미로 범위 벗어나지 않는지 &&
            if 0 <= nx < N and 0 <= ny < N and nemo[ny][nx] != 1 and visited[ny][nx] != 1:
                if nemo[ny][nx] == 3:
                    return 1                        # 1 반환 후 종료
                # 3이 아니라면
                stack.append((ny, nx))
                # 방문 처리
                visited[ny][nx] = 1
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

