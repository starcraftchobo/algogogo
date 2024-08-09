import sys
sys.stdin = open("sample_input.txt", "r")


def f(i, j):    # i~j번까지의 승자를 찾는 함수
    if i==j:    # 한 명만 남은 경우
        return i
    else:       # 두 명 이상인 경우 두 그룹의 승자를 찾차 최종 승자를 가림
        left = f(i, (i+j)//2)       # 왼쪽 그룹의 승자
        right = f((i+j)//2+1, j)    # 오른쪽 그룹의 승자
        return win(left, right)     # 두 그룹의 승자를 찾는 함수 구현

def win(left, right):
    if gawibawibo[left] == gawibawibo[right]:
        return left
    elif gawibawibo[left] == 1:         # 가위
        if gawibawibo[right] == 2:      # 바위
            return right
        else:               # 보
            return left
    elif gawibawibo[left] == 2:         # 바위
        if gawibawibo[right] == 3:      # 보
            return right
        else:               # 가위
            return left
        return
    elif gawibawibo[left] == 3:         # 보
        if gawibawibo[right] == 1:      # 가위
            return right
        else:
            return left


T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    N = int(input())
    gawibawibo = list(map(int, input().split()))

    print(f'#{test_case} {f(0, N-1)+1}')


