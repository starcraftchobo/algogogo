import sys
sys.stdin = open("input.txt", "r")

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    N, M = map(int,input().split())
    a = list(map(int, input().split()))
    lst_guganhap = []

    for i in range(N-M+1):
        guganhap = 0
        for j in range(M):
            guganhap += a[i+j]
        lst_guganhap.append(guganhap)

    hap_max, hap_min = lst_guganhap[0], lst_guganhap[0]
    # print(lst_guganhap)
    for x in lst_guganhap:
        if hap_max < x:
            hap_max = x
        if hap_min > x:
            hap_min = x
    print(f'#{test_case} {hap_max - hap_min}')
