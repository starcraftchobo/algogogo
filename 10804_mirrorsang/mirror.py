import sys
sys.stdin = open("input.txt", "r")

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    s = list(input())
    N = len(s)
    mirror = []

    for i in range(N-1, -1, -1):
        if s[i] == 'b':
            mirror.append('d')
        elif s[i] == 'd':
            mirror.append('b')
        elif s[i] == 'p':
            mirror.append('q')
        else:
            mirror.append('p')

    mirror = "".join(mirror)
    print(f'#{test_case}', mirror)