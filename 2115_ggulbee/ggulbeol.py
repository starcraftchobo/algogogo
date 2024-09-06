import sys
sys.stdin = open("sample_input.txt", "r")
# 두번째 값이 첫번째값 안에 잇으면 그 줄 경우의 수랑 각 라인 최대값만 비교
# 꿀판 하나 더 만들고 판매가 다 쏙쏙 집어넣자
# 첫번째랑 겹치지만 않음 뭐

# 재귀는 기저조건, 다음재귀 호출전, 다음재귀 호출, 호출 후
def add(sel, m, c, now):
    if :
        return money
    r, c = sel
    for i in range(m):
        honey[r][c+i]

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    N, M, C = map(int, input().split())
    honey = [list(map(int, input().split())) for _ in range(N)]
    print(honey)

    # max_tot = 0 # 최대값 저장할곳
    #
    # max_grid = [] # 최대 좌표 저장할곳
    # line = []     # 라인별 최대값 저장하려햇던곳
    totals = [[None]*N for _ in range(N)]
    # print(totals)

    for i in range(N):
        # max_line = 0
        # line_j = 0
        for j in range(N-M+1):
            # 1. 꿀 합이 C가 안넘을때
            honey_sum = sum(honey[i][j:j+M])
            if C <= honey_sum:
                total = # 값들의 제곱
            else:
                total = # 최대원소**2
            totals[i*N + j] = total


            # 현재 꿀양과 최대값 비교
            # if max_tot < total:     # 현재 꿀양이 최대값 이상이면
            #     second = max_tot    # 두번째 최대값 갱신
            #     max_tot = total     # 최대값 갱신
            #     other = max_grid    # 두번째값 꿀통 위치 갱신
            #     max_grid = [(i,j)]  # 최대값 꿀통 위치 갱신
            #
            # elif total == max_tot:  # 현재 꿀양이 최대값과 같으면
            #     max_grid.append((i,j))  # 최대값 꿀통 위치 하나 추가
            # elif total == second:   # 현재 꿀양이 두번째랑 같으면
            #     other.append((i, j))    # 두번째값 꿀통 위치 추가