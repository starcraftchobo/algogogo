import sys
sys.stdin = open("sample_input.txt", "r")

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    N = int(input())

    answer = 0
    for i in range(11):
        # 일정 범위에서 일정값 이상이면 2**n
        # 일정 범위 이하이면 N-2**n

        # if N > 2**i:

        # n/2번 노드라..