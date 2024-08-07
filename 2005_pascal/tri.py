# import sys
# sys.stdin = open("input.txt", "r")

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    N = int(input())

    tri = [[] for _ in range(N)]

    for i in range(N):
        if i == 0:
            tri[0].append(1)
        if i == 1:
            tri[i].append(1)
            tri[i].append(1)
        if i >= 2:
            tri[i].append(1)
            for j in range(1, i):
                a = tri[i-1][j-1]+tri[i-1][j]
                tri[i].append(a)
            tri[i].append(1)

    print(f'#{test_case}')
    for k in range(N):
        print(*tri[k])