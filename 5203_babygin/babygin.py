import sys
sys.stdin = open("sample_input.txt", "r")

'''
3번째부터 가능
run = 연속숫자 3개/ 정렬 후 연속 idx 3개 1차이
triplet = 같은숫자 3개/ 정렬 후 연속 idx 3개 같
'''

def runrun(player):
    player = sorted(player)
    for i in range(len(player)-2):
        if player[i+2] == (player[i+1]+1) and player[i+1] == (player[i]+1):
            return 1

def triplet(player):
    player = sorted(player)
    for i in range(len(player)-2):
        if player[i] == player[i+1] and player[i+1] == player[i+2]:
            return 1

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    print(f'#{test_case}', end=' ')
    card = list(map(int, input().split()))
    player_1 = []
    player_2 = []
    for i in range(6):
        player_1.append(card[i*2])
        if i >= 2:
            if runrun(player_1) or triplet(player_1):
                print(1)
                break
        player_2.append(card[i*2+1])
        if i >= 2:
            if runrun(player_2) or triplet(player_2):
                print(2)
                break
    else:
        print(0)