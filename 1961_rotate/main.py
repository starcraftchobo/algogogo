# import sys
# sys.stdin = open("input.txt", "r")

T = int(input())
for test_case in range(1, T + 1):
    print(f'#{test_case}')
    N = int(input())
    arr = list()
    for _ in range(N):
        arr.append(list(map(int, input().split())))
    #90
    arr_90 = list()
    for i in range(N):
        arr_90.append([arr[N-x-1][i] for x in range(N)])
    #180
    arr_180 = list()
    for i in range(N):
        arr_180.append([arr[N-i-1][N-x-1] for x in range(N)])
    #270
    arr_270 = list()
    for i in range(N):
        arr_270.append([arr[x][N-1-i] for x in range(N)])
    
    for i in range(N):
        print(*arr_90[i], *arr_180[i], *arr_270[i])