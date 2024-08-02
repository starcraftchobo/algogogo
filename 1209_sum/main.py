
import sys
sys.stdin = open("sum_input.txt")

for _ in range(10):
    arr = list()
    tc = int(input())
    print(f'#{tc}')
    for _ in range(100):
        arr.append(list(map(int, input().split())))
    # print(arr)
    sum_col = [sum(x) for x in arr]
    max_col = max(sum_col)

    row = list()
    for i in range(100):
        row.append([arr[x][i] for x in range(100)])
    
    sum_row = [sum(x) for x in row]
    max_row = max(sum_row)

    cross_for = list()
    for i in range(100):
        cross_for.append(arr[i][99-i])
        sum_cross1 = sum(cross_for)
    cross_rev = list()
    for i in range(100):
        cross_rev.append(arr[i][i])
        sum_cross2 = sum(cross_rev)

    print(max(max_col, max_row, sum_cross1, sum_cross2))

