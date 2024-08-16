import sys
sys.stdin = open("s_input.txt", "r")

# 각 버정에 몇개 노선인가


T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    stn = [0] * 5001                    # 0번째 정류장이 없으므로 1개 추가 생성
    N = int(input())                    # 버스 노선 개수

    for _ in range(N):                  # 노선 받아오기
        a, b = map(int, input().split())
        for i in range(a, b+1):         # 받아오면서 정류장에 +도 해주기
            stn[i] += 1

    P = int(input())
    print(f'#{test_case}', end=' ')
    for i in range(P):
        print((stn[int(input())]), end=' ')
    print()