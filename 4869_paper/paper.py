import sys
sys.stdin = open('sample_input.txt', 'r')

def paper(length):
    if length == 10:
        return 1
    elif length == 20:
        return 3
    else:
        return paper(length-10) + paper(length-20)*2

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    print(f'#{tc}', paper(N))