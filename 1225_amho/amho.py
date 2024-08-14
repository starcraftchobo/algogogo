import sys
sys.stdin = open("input.txt", "r")

T = 10
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    tc = int(input())
    amho = list(map(int, input().split()))

    def cycle(lst):
        while 0 not in lst:      # lst의 애들중 0 이하가 없으면
            for i in range(1,6):
                lst = [lst[1], lst[2], lst[3], lst[4], lst[5], lst[6], lst[7], lst[0]]
                lst[7] -= i
                if lst[7] <= 0:
                    lst[7] = 0
                    break
        return lst

    a = cycle(amho)
    print(f'#{test_case}', *a)