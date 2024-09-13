import sys
sys.stdin = open("input.txt", "r")
sys.setrecursionlimit(1000000)
'''
칸 돌면서 탐색 쥬르륵
탐색은 1큰거 or 작은거 append
cnt return hoo result eh kok
큰거 찾기랑 작은거 찾기로 나누자
'''
def small(r, c, cnt):
    visited[r][c] = 1
    now = rooms[r][c]
    for i in range(len(dxy)):
        nr, nc = r + dxy[i][1], c + dxy[i][0]
        if 0 <= nr < N and 0 <= nc < N and not visited[nr][nc]:
            if rooms[nr][nc] == now - 1:
                 return small(nr, nc, cnt+1)
    else:
        return rooms[r][c], cnt
    pass
def big(r, c, cnt):
    visited[r][c] = 1
    now = rooms[r][c]
    for i in range(len(dxy)):
        nr, nc = r + dxy[i][1], c + dxy[i][0]
        if 0 <= nr < N and 0 <= nc < N and not visited[nr][nc]:
            if rooms[nr][nc] == now + 1:
                 return big(nr, nc, cnt+1)
    else:
        return cnt
    pass
def search(r, c, cnt):
    if not visited[r][c]:
        visited[r][c] = 1
    now, least = rooms[r][c], rooms[r][c]
    s, b = cnt, cnt
    for i in range(len(dxy)):
        nr, nc = r + dxy[i][1], c + dxy[i][0]
        if 0 <= nr < N and 0 <= nc < N and not visited[nr][nc]:
            if rooms[nr][nc] == now + 1:
                b = big(nr, nc, cnt+1)
            elif rooms[nr][nc] == now - 1:
                least, s = small(nr, nc, cnt+1)
    return least, s+b-1

dxy = [(-1, 0), (0, -1), (1, 0), (0, 1)]

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    N = int(input())
    rooms = [list(map(int, input().split())) for _ in range(N)]
    visited = [[0] * N for _ in range(N)]
    result = -1
    number = 9999999
    for i in range(N):
        for j in range(N):
            num, r = search(i, j, 1)
            if result == r:
                if num < number:
                    number = num
            elif r > result:
                result = r
                number = num

    print(f'#{test_case}', number, result)
