import sys

sys.stdin = open("sample_input.txt", "r")


def bfs(S, G, V):
    # 초기화
    q = [S]  # 큐를 만들고 시작점 인큐
    visited = [0] * (V + 1)  # visited 만들고 인큐할때 콕찍
    visited[S] = 1
    # print(visited)
    # 탐색
    while q:
        t = q.pop(0)  # 가는곳 디큐
        # print(t)
        for w in (adj_l)[t]:  # 디큐한놈 인접 인큐(visited 제외)
            if visited[w] == 0:
                q.append(w)
                visited[w] = visited[t] + 1
    if visited[G] == 0:
        return 0        # s g가 연결 돼있지 않은경우 0 처리
    return visited[G] - 1   # 시작점도 count되서 빼줘야함

    # 큐가 빌때까지 달려잇


T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    V, E = map(int, input().split())
    arr = [tuple(map(int, input().split())) for _ in range(E)]
    S, G = map(int, input().split())

    adj_l = [[] for _ in range(V + 1)]
    for i in range(E):
        v1, v2 = arr[i][0], arr[i][1]
        adj_l[v1].append(v2)
        adj_l[v2].append(v1)
    # print(adj_l)

    print(f'#{test_case}', bfs(S, G, V))


