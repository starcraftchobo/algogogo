def box(brush):                                         # 색칠하는 함수
    global count
    r1, c1 = info_box[brush][0:2]
    r2, c2 = info_box[brush][2:4]
    color = info_box[brush][4]
    # print(r1, r2, c1, c2, color)
    for i in range(r1, r2+1):                           # box 대로 색칠시작
        for j in range(c1, c2+1):
            if board[i][j] == 0 or board[i][j] == color:    # 판이 안칠해져있거나 같은 색깔이면
                board[i][j] = color
            else:                                       # 판의 원래 색이 다른색깔이면 +1
                count += 1

T = int(input())
for test_case in range(1, T + 1):
    N = int(input())                                        # int에 주의합시다....
    info_box = [list(map(int, input().split())) for _ in range(N)] # 각 박스들의 모서리 index&color
    board = [[0] * 10 for _ in range(10)]                     # 10*10짜리 판

    count = 0

    for i in range(N):                                      # 문제해결
        box(i)

    print(f'#{test_case} {count}')