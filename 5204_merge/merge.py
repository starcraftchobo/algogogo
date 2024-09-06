import sys
sys.stdin = open("sample_input.txt", "r")


def div(lst):
    n = len(lst)
    if n == 1:
        return lst

    left = lst[0 : n//2]
    right = lst[n//2 : n]

    left = div(left)
    right = div(right)

    return merge(left, right)

def merge(left, right):
    global cnt
    result = [0] * (len(left) + len(right))
    if left[-1] > right[-1]:
        cnt += 1

    l = r = 0
    while l <len(left) and r < len(right):
        if left[l] < right[r]:
            result[l+r] = left[l]
            l += 1
        else:
            result[l+r] = right[r]
            r += 1

    while l < len(left):
        result[l+r] = left[l]
        l += 1

    while r < len(right):
        result[l+r] = right[r]
        r += 1

    return result




T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    N = int(input())
    arr = list(map(int, input().split()))
    cnt = 0
    print(f'#{test_case} {div(arr)[N//2]} {cnt}')