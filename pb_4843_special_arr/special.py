import sys
sys.stdin = open("sample_input.txt", "r")

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    N = int(input())                    # int에 주의합시다...
    arr = list(map(int, input().split()))
    # print(arr)

    for i in range(0, N-1, 2):          # 0, 2, 4...  2칸씩 정렬 영역 설정
        max_idx = i                     # max, min 초기 인덱스 설정
        min_idx = i+1                   # min은 홀수

        for j in range(i, N):
            if arr[max_idx] < arr[j]:   # max index 찾기
                max_idx = j
        arr[i], arr[max_idx] = arr[max_idx], arr[i]     # max 값을 홀수 인덱스에 쏙
                                        # max, n1, n2, n3....
        for j in range(i+1, N):         # 이미 정렬된 i번째 다음인 i+1
            if arr[min_idx] > arr[j]:
                min_idx = j
        arr[i+1], arr[min_idx] = arr[min_idx], arr[i+1]
                                        # max, min, n1, n2, n3...
    print(f'#{test_case}', end=' ')
    for _ in range(10):                 # '10'개까지 출력한다...문제를 잘읽읍시다.......
        print(arr.pop(0), end=' ')      # arr 첫번째항 출력후 삭제
    print()
