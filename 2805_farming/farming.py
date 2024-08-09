import sys
sys.stdin = open("input.txt", "r")
#
T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    N = int(input())
    nongjang = [list(map(int, input())) for _ in range(N)]  # 이상한 룰의 농장
    # print(nongjang)
    mid = int(N / 2)                                        # 가운데
    maechul = 0                                             # 매출

    for i in range(N):
        if i <= mid:                                        # y좌표가 절반 이하면
            # suhwak.append(nongjang[i][mid-i:mid+i+1])
            for x in nongjang[i][mid-i:mid+i+1]:            # 점점 늘어나는 범위
               maechul += x                                 # 매상이 올라가욧
        else:                                               # y좌표가 N/2 초과면
            # suhwak.append(nongjang[i][mid-(N-i):mid+(N-i)+1])
            for x in nongjang[i][mid-(N-(i+1)):mid+(N-i)]:  # 점점 줄어드는 범위
                maechul += x                                # 매출이 올라가욧

    print(f'#{test_case}', maechul)