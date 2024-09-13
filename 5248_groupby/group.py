import sys
sys.stdin = open('sample_input.txt', 'r')
'''
앞의 앞의꺼가 바뀌는게 구현이 안된다!
10 1 / 8 9 / 9 10이면 8도 1로 바껴야하는데...8인게 다 1로 바뀌게?
'''
def make_set(n):
    p = [i for i in range(n+1)]
    return p

def find_p(x):
    if parent[x] == x:
        return x
    return find_p(parent[x])

def union(a, b):
    root_a = find_p(a)
    root_b = find_p(b)

    if root_a == root_b:
        return

    if root_a < root_b:
        for i in range(1, len(parent)):
            if parent[i] == root_b:
                parent[i] = root_a
    else:                   # parent[a]가 더 크면
        for j in range(1, len(parent)):
            if parent[j] == root_a:
                parent[j] = root_b


T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    group = list(map(int, input().split()))
    # print(len(group))

    parent = make_set(N)
    total = set()

    for i in range(len(group)//2):
        a, b = group[2*i], group[2*i + 1]
        union(a, b)
    for j in range(1, N+1):
        total.add(find_p(j))

    print(f'#{tc} {len(total)}')