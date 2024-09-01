
# class Search:
#     def __init__(self, size):
#         self.size = size
#         self.rear = self.front = -1
#         self.queue = [None]*size
#
#     def is_empty(self):
#         return self.front == -1
#
#     def is_full(self):
#         return self.rear == self.size - 1
#
#     def enqueue(self, item):
#         # 큐가 꽉찻을때
#         if self.is_full():
#             print("Que is full")
#             return
#         if self.is_empty():
#             self.rear = self.front = 0
#         else:
#             self.rear += 1
#         self.queue[self.rear] = item



    # sel
    # q = [None]*N*M
    # visited = [None]*N*M
    # front = rear = -1
    # enque
    # deque
# def search(google_map, y, x):                   # not minimum result
#     cnt = 1
#
#     for i in range(4):
#         y = r + dy[i]
#         x = c + dx[i]
#         if 0 <= y + dy[i] < N and 0 <= x + dx < M:
#             if google_map[y][x] == 'W':
#                 return cnt
#             else:
#                 if google_map[y][x]:
#                     google_map[y][x] = 0
#                     return search(google_map, y, x)
#         return cnt
import sys
sys.stdin = open("sample_input.txt", "r")
# BFS 너비우선탐색
# 큐 만들기

dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]

def bfs(mapmap, y, x, n, m):  # 시작jwapyo
    # visited = [[0] * m for _ in range(n)]  # visited 생성
    q = []  # 큐 생성
    q.append([y, x, 0])  # 시작점 인큐
    # visited[y][x] = 1  # 시작점 방문표시
    while q:  # 큐에 정점이 남아있으면 front != rear
        yy, xx, cnt = q.pop(0)  # 디큐
        if mapmap[yy][xx] == 'W':
            return cnt
        elif mapmap[yy][xx] == 'L':
            cnt += 1
            mapmap[yy][xx] = 0
            for i in range(4):
                if 0 <= yy+dy[i] < n and 0 <= xx+dx[i] < m:
                    if mapmap[yy+dy[i]][xx+dx[i]]:
                        q.append([yy+dy[i], xx+dx[i], cnt])
        else:                   # 0/already searched
            continue


T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    N, M = map(int, input().split())
    grid = [list(input()) for _ in range(N)]
    # print(grid)
    answer = 0
    for r in range(N):
        for c in range(M):
            if grid[r][c] == 'L':
                answer += bfs(grid, r, c, N, M)