import sys
sys.stdin = open("input.txt", "r")

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    ladder = [list(map(int, input().split()))]
    print(ladder)
    x = 0
    y = 99

    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]


    for i in range(100):                # 2 좌표 찾기
        if ladder[y][i] == 2:
            a = i
            break

    status = 0

    while y != 0:
        if ladder[y][x-1] and ladder[y][x+1] == 0:  # 왼오 0 -> 위로 1
            y -= 1
        elif ladder[y][x+dx[0]] == 1:                                 # 일직선
            while ladder[y][x+dx[0]]:                                 # 왼 0일때까지
                a -= 1                                                # 왼
            else:
                y -= 1
        else:
            while dx+1 == 1:                                        # 오 0일때까지
                a += 1                                              # 오
            else:
                y -= 1

    print(a)



        # if ladder[y][x] and ladder[y][x] == 0:  # 위 0이면
        #     if :                                # 전에 왼
        #         if ladder[y][x-1] == 0 and ladder[y][x-1] == 0: # 가로 먼저 확인                                            # 방향 그대로
        #     else:                               # 전에 오
        #         if ladder[y][x-1] == 0 and ladder[y][x-1] == 0: # 가로 먼저 확인




