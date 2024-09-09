import sys
sys.stdin = open("sample_input.txt", "r")
'''
1. 첫번쨰는 인덱스, 두번째는 노드 갈곳
2. start를 넣어서 end에 도착하면 1, 그전에 스택이 비면 0
3. 그 인덱스에 잇는 놈들은 다 때려넣자
4. pop한 놈이 g면 그만~
'''
def path(s, g):
    stack = [0] * 5000
    top = 0
    stack[top] = s
    while top >= 0:
        a = stack[top]
        top -= 1
        if a == g:
            return 1
        for node in arr[a]:
            top += 1
            stack[top] = (node)
    return 0

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    V, E = map(int, input().split())
    arr = list(list() for _ in range(V+1))
    # print(arr)
    for _ in range(E):
        start, end = map(int, input().split())
        arr[start].append(end)

    S, G = map(int, input().split())
    # print(arr)
    print(f'#{test_case} {path(S, G)}')

