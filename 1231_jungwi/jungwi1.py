# 라이브 코드에 충실(?)해보기

# import sys
# sys.stdin = open("input.txt", "r")


def pre_order(T):
    if T:
        pre_order(left[T])
        print(arr[T-1][1], end='')
        pre_order(right[T])


for test_case in range(1, 11):

    N = int(input())  # 1번부터 N번까지인 정점
    arr = [list(input().split()) for _ in range(N)]
    left = [0] * (N + 1)  # 부모를 인덱스로 왼쪽자식번호 저장
    right = [0] * (N + 1)  #
    par = [0] * (N + 1)  # 자식을 인덱스로 부모 저장

    for i in range(N):
        if len(arr[i]) == 4:  # 왼쪽자식이 없으면
            p = i + 1
            c1, c2 = int(arr[i][2]), int(arr[i][3])

            left[p], right[p] = c1, c2
            par[c1] = p
            par[c2] = p
        elif len(arr[i]) == 3:
            p = i + 1
            c = int(arr[i][2])
            left[p] = c
            par[c] = p
        else:
            continue
    # print(left)
    # print(right)
    # print(par)
    c = N
    while par[c] != 0:  # 부모가 있으면
        c = par[c]  # 부모를 새로운 자식으로 두고
    root = c  # 더이상 부모가 없으면 root
    # print(root)
    print(f'#{test_case}', end=' ')
    pre_order(root)
    print()