import sys, itertools
sys.stdin = open('sample_input.txt', 'r')
'''
가로세로 바꿔받은다음
a, b로 바꿔가며 탐색
'''
T = int(input())
for tc in range(1, T+1):
    D, W, K = map(int, input().split())
    film = [list(map(int, input().split())) for _ in range(D)]
    print(film)


    print(new_film)

    D C (K-1)

    dcr* r**2



    new_film = [list(film[i][j] for i in range(D)) for j in range(W)]   # D가 가로 W가 세로