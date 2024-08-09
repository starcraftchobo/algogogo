import sys
sys.stdin = open("input.txt", "r")

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    N = int(input())
    box_list = list(map(int, input().split()))
    # print(test_case, N, box_list)

    result = 0  # 최종 결과값

    for i in range(N - 1):
        # 방해받지 않았을때 i번째 상자가 떨어질수 있는 최대 높이
        # 전체 길이 - (내 위치 + 1)
        max_h = len(box_list) - (i+1)
        #뒤에 오는 박스 중 얘보다 같거나 더 큰 박스
        for j in range(i+1, len(box_list)):
            # i와 j 비교
            # print(box_list[i] <= box_list[j])
            if box_list[i] <= box_list[j]:
                max_h -= 1

    # 여기서, 지금 검사한 상자 높이가 result 값보다 크면 갱신
        if result < max_h:
            result = max_h

    print(f'#{test_case} {result}')