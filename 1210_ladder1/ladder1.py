# import sys
# sys.stdin = open("inpu2t.txt", "r")

# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, 11):
    N = int(input())
    ladder = [list(map(int, input().split())) for _ in range(100)]

    for i in range(100):
        ladder[i].insert(0, 0)
        ladder[i].insert(101, 0)
    x = 0
    y = 99

    # print(len(ladder))
    for i in range(101):  # 2 좌표 찾기
        if ladder[y][i] == 2:
            x = i
            break

    while y != 0:
        if ladder[y][x - 1] == 1:  # 일직선
            while ladder[y][x - 1] == 1:  # 왼 0일때까지
                x -= 1  # 왼

        elif ladder[y][x + 1] == 1:
            while ladder[y][x + 1] == 1:  # 오 0일때까지
                x += 1  # 오
        if ladder[y - 1][x] == 1:
            y -= 1

        else:  # 왼오 0 -> 위로 1
            y -= 1

    print(f'#{N}', x - 1)
