import sys
sys.stdin = open("sample_input.txt", "r")

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    K, N, M = list(map(int, input().split()))
    stn = list(map(int, input().split()))
    stn.insert(0,0)                     # 최초 출발지점 위해 맨앞에 0 삽입
    # print(K, N, M, stn)               # stn = [0, 1, 3, ...]

    idx = cnt = 0

    def charging(stn, K, N, M):
        global idx, cnt
        if stn[idx] + K >= N:               # 현재 위치 + 주행거리 >= 종점이면 cnt 반환
            return cnt
        elif stn[idx+1] > stn[idx] + K:     # 다음 역이 주행거리보다 멀어서 못가면 0 반환
            return 0
        else:
            a = idx                         # 밑의 for문에서 현재 인덱스 값이 바뀌는걸 방지
            for i in range(a+1,M+1):        #
                if stn[i] <= stn[a] + K:    # 역이 주행거리 내에 있으면
                    idx = i                 # 해당 역 인덱스 저장
                else:                       # 범위 이상이면 그만
                    break

        cnt += 1                            # 충전횟수 1 증가

        return charging(stn, K, N, M)

    print(f'#{test_case}', charging(stn, K, N, M))