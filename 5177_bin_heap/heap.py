import sys
sys.stdin = open("sample_input.txt", "r")

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    N = int(input())
    nums = list(map(int, input().split()))
    tree = [0]*(N + 1)

    idx = 0
    result = 0
    for num in nums:
        idx += 1
        tree[idx] = num
        parent = idx // 2
        child = idx
        # print(parent)
        while parent >= 1:
            if tree[parent] > tree[child]:
                tree[child], tree[parent] = tree[parent], tree[child]
            parent //= 2
            child //= 2
    # print(tree, idx)
    while idx > 1:
        idx //= 2
        # print(tree[idx])
        result += tree[idx]
    print(f'#{test_case}', result)
