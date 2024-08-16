import sys
sys.stdin = open("input1.txt", "r")

def pang(x, y, arr):
    ggot = arr[y][x]
    for i in range(1, ggot+1):
        a, b, c, d = x+i, x-i, y+i, y-i
        if 0 <= a < M:
            ggot += arr[y][a]
        if 0 <= b < M:
            ggot += arr[y][b]
        if 0 <= c < N:
            ggot += arr[c][x]
        if 0 <= d < N:
            ggot += arr[d][x]
    garu.append(ggot)

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    N, M = map(int, input().split())
    poong = [list(map(int, input().split())) for _ in range(N)]

    garu = []

    for i in range(N):
        for j in range(M):
            pang(j, i, poong)
    # print(garu)
    max = 0
    for x in garu:
        if max < x:
            max = x

    print(f'#{test_case}', max)

