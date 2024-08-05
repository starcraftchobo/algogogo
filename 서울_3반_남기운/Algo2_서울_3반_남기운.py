T = int(input())

for test_case in range(1, T+1):
    N = int(input())
    mount = list(map(int, input().split()))

    road = [[]]
    idx = 0                               # road의 index
    road[idx].append(mount[0])              # mount의 첫 원소 append
    for i in range(1, N):
        if mount[i] < mount[i-1]:           # 앞의 경사도가 더 클경우
           idx += 1                         # index 1추가
           road.append([])                  # road에 새 오르막길 list 추가
           road[idx].append(mount[i])       # 추가한 list에 append
        else:
            road[idx].append(mount[i])

    # print(road)

    a = []                                  # 경사도 담을 list

    for lst in road:
        high, low = lst[0], lst[0]          # 최대 최소값 초기화
        for i in lst:
            if high < i:
                high = i
            if low > i:
                low = i
        a.append((high-low) / len(lst))     # 경사도 계산 후 a에 추가
    # print(a)

    for j in range(1, idx):                 # road에 접근할 index 구하는 loop
        if a[j] < a[j-1]:                   # j번째의 경사도가 j-1번째보다 크면
            index = j                       # index에 j 추가
        elif a[j] == a[j-1]:                # 두개의 경사도가 같을때
            if len(road[j]) > len(road[j-1]):   # j번째 road의 길이가 더 크면
                index = j
            else:                           # road의 길이가 작거나 같으면
                index = j-1
        else:                               # index가 0일 경우(0번째 경사도가 제일 작을 경우 추가가 안되었음)
            index = 0

    print(f'# {test_case}', len(road[index]))   # road의 j번째 길이 출력