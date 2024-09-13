import sys
sys.stdin = open('s_input.txt', 'r')
'''
rank가 같은거는 +1 해주고 아니면 걍 합치기만
'''
def make_set(n):
    p = [i for i in range(n+1)]
    r = [0]*(n+1)
    return p, r

def find_p(x):
    if parents[x] == x:
        return x
    parents[x] = find_p(parents[x])
    return parents[x]

def union(a, b):
    root_a = find_p(a)
    root_b = find_p(b)

    if root_a == root_b:
        return

    if ranks[root_a] < ranks[root_b]:
        for i in range(1, len(parents)):
            if parents[i] == root_a:
                parents[i] = root_b
    elif ranks[root_a] > ranks[root_b]:
        for i in range(1, len(parents)):
            if parents[i] == root_b:
                parents[i] = root_a
    else:
        parents[root_b] = root_a
        for i in range(1, len(parents)):
            if parents[i] == root_b:
                parents[i] = root_a
        ranks[root_a] += 1

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())

    parents, ranks = make_set(N)
    teams = set()

    for _ in range(M):
        a, b = map(int, input().split())
        union(a, b)

    for j in range(1, len(parents)):
        teams.add(parents[j])
    print(f'#{tc} {len(teams)}')