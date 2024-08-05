import sys
sys.stdin = open("sample_input.txt", "r")

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    N, M = list(map(int, input().split()))
    print(N, M)
    text = list(input() for _ in range(N))
    print(text)

    for i in range(N):
        for j in range(N-M+1):
