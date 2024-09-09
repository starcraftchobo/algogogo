import sys
sys.stdin = open('sample_input.txt', 'r')

T = int(input())

for tc in range(1, T+1):
    V, E = map(int, input().split())
    adj_matrix = [[0] * (V+1) for _ in range(V+1)]
    # print(adj_matrix)

    for i in range(E):
        start, end = map(int, input().split())
        adj_matrix[start][end] = 1

    S, G = map(int, input().split())
    stack = [S]
    visited = [0] * (V + 1)

    while stack:
        current = stack.pop()
        visited[current] = 1

        for next_n in range(V+1):
            if adj_matrix[current][next_n] == 1 and visited[next_n] == 0:
                stack.append(next_n)

    if visited[G] == 1:
        print(f'#{tc} 1')
    else:
        print(f'#{tc} 0')