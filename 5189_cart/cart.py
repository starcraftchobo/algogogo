import sys
sys.stdin = open("sample_input.txt", "r")

'''
1. 1~N까지 한번씩 다 나와야됨
2. 앞에랑 뒤에랑 같으면 안됨
3. 뒤에 나오는 애는 중복 x
4. 그럼 종료조건은 N번 돈 경우겟다
'''



def search(start, level, n):
    if level == n:
        lst_total.append(sum(path))
        return
    for i in range(n):
        if visited[start]:  # 중복제거조건
            continue
        visited[i] = 1
        search(i, level+1, n)
        path.pop()



T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    N = int(input())
    office = list(map(int, input().split()))

    visited = [0] * (N + 1)
    path = []
    lst_total = []

    search(1, 0, N)
    print(max(lst_total))