T = int(input())

for test_case in range(1, T+1):
    N = int(input())
    food = [list(map(int, input().split())) for _ in range(N)]  # 실험판 2차원 배열

    dx = [-1, 0, 1, 0]
    dy = [0, -1, 0, 1]  # 좌상우하
    amount = list([] * N for _ in range(N))                     # 총 먹이량 받는 리스트

    for y in range(N):
        for x in range(N):
            total = food[y][x]
            for i in range(4):
                if x + dx[i] < 0 or y + dy[i] < 0:              # index가 0보다 작을시 continue
                    continue
                elif x + dx[i] >= N or y + dy[i] >= N:          # index가 N 이상일 시 continue
                    continue
                else:
                    total += food[y + dy[i]][x + dx[i]]
            amount[y].append(total)                             # amount에 각 좌표별 먹이량 넣기

    maximum = amount[0][0]                                      # 최대 먹이량 초기화
    for y in range(N):
        for x in range(N):
            if maximum <= amount[y][x]:                         # max
                maximum = amount[y][x]

    print(f'#{test_case}', maximum)