import sys
sys.stdin = open("sample_input.txt", "r")

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    str1 = input()
    str2 = input()

    N = 0
    M = 0
    result = 0

    for x in str1:
        N += 1
    for y in str2:
        M += 1

    for i in range(M-N+1):
        if str1 == str2[i:i+N]:
            result = 1
            break

    print(f'#{test_case}', result)