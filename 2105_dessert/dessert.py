import sys
sys.stdin = open('sample_input.txt', 'r')

dy = [1, 1, -1, -1]
dx =  [-1, 1, 1, -1]

def food_fight(d, y, x, N):
    cnt = [0] * 4
    dessert = set()
    dessert.
    if d <= N // 2:  # i가 N 절반 미만
        for j in range(d):  # 인덱스 에러 안날때
            if ny < 0 or nx < 0 or ny >= N or nx >= N: continue
            elif cafe[ny][nx]
            return
        for k in range(N - 2 - i):


T = int(input())
for tc in (1, T+1):
    N = int(input())
    cafe = [list(map(int, input().split()))]

    for i in range(1, 19):          # 방향전환 횟수의 절반
        for r in range(i):          # y
            for c in range(1, N-1): # x
