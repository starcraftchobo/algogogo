import sys
sys.stdin = open("GNS_test_input.txt", "r")

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    N= input()
    arr = list(input().split())
    # print(arr)
    counts = [0] * 10
    for word in arr:
        if word == 'ZRO':
            counts[0] += 1
        if word == 'ONE':
            counts[1] += 1
        if word == 'TWO':
            counts[2] += 1
        if word == 'THR':
            counts[3] += 1
        if word == 'FOR':
            counts[4] += 1
        if word == 'FIV':
            counts[5] += 1
        if word == 'SIX':
            counts[6] += 1
        if word == 'SVN':
            counts[7] += 1
        if word == 'EGT':
            counts[8] += 1
        if word == 'NIN':
            counts[9] += 1

    # print(counts)
    for i in range(9):
        counts[i+1] = counts[i] + counts[i+1]
    # print((counts))

    bandeut = [0] * counts[9]
    for word in arr:
        if word == 'ZRO':
            counts[0] -= 1
            bandeut[counts[0]] = word
        if word == 'ONE':
            counts[1] -= 1
            bandeut[counts[1]] = word
        if word == 'TWO':
            counts[2] -= 1
            bandeut[counts[2]] = word
        if word == 'THR':
            counts[3] -= 1
            bandeut[counts[3]] = word
        if word == 'FOR':
            counts[4] -= 1
            bandeut[counts[4]] = word
        if word == 'FIV':
            counts[5] -= 1
            bandeut[counts[5]] = word
        if word == 'SIX':
            counts[6] -= 1
            bandeut[counts[6]] = word
        if word == 'SVN':
            counts[7] -= 1
            bandeut[counts[7]] = word
        if word == 'EGT':
            counts[8] -= 1
            bandeut[counts[8]] = word
        if word == 'NIN':
            counts[9] -= 1
            bandeut[counts[9]] = word
    print(f'#{test_case}')
    print(' '.join(bandeut))