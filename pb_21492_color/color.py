# 기본 제공코드는 임의 수정해도 관계 없습니다. 단, 입출력 포맷 주의
# 아래 표준 입출력 예제 필요시 참고하세요.

# 표준 입력 예제
'''
a = int(input())                        정수형 변수 1개 입력 받는 예제
b, c = map(int, input().split())        정수형 변수 2개 입력 받는 예제
d = float(input())                      실수형 변수 1개 입력 받는 예제
e, f, g = map(float, input().split())   실수형 변수 3개 입력 받는 예제
h = input()                             문자열 변수 1개 입력 받는 예제
'''

# 표준 출력 예제
'''
a, b = 6, 3
c, d, e = 1.0, 2.5, 3.4
f = "ABC"
print(a)                                정수형 변수 1개 출력하는 예제
print(b, end = " ")                     줄바꿈 하지 않고 정수형 변수와 공백을 출력하는 예제
print(c, d, e)                          실수형 변수 3개 출력하는 예제
print(f)                                문자열 1개 출력하는 예제
'''




'''
아래의 구문은 input.txt 를 read only 형식으로 연 후,
앞으로 표준 입력(키보드) 대신 input.txt 파일로부터 읽어오겠다는 의미의 코드입니다.
여러분이 작성한 코드를 테스트 할 때, 편의를 위해서 input.txt에 입력을 저장한 후,
아래 구문을 이용하면 이후 입력을 수행할 때 표준 입력 대신 파일로부터 입력을 받아올 수 있습니다.
따라서 테스트를 수행할 때에는 아래 주석을 지우고 이 구문을 사용하셔도 좋습니다.
아래 구문을 사용하기 위해서는 import sys가 필요합니다.
단, 채점을 위해 코드를 제출하실 때에는 반드시 아래 구문을 지우거나 주석 처리 하셔야 합니다.
'''
# import sys
# sys.stdin = open("sample_input.txt", "r")

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    print(f'#{test_case}', end=' ')
    N = int(input())
    a = [list(map(int, input().split())) for _ in range(N)] # 각 박스들의 모서리 index&color
    pan = [[0] * 10 for _ in range(10)]                     # 10*10짜리 판

    count = 0

    def box(num): # 모서리 정보대로 박스 만들기
        global count
        r1, c1 = a[num][0:2]
        r2, c2 = a[num][2:4]
        color = a[num][4]
        # print(r1, r2, c1, c2, color)
        for i in range(r1, r2+1):                           # box 대로 색칠시작
            for j in range(c1, c2+1):
                if pan[i][j] == 0 or pan[i][j] == color:
                    pan[i][j] = color
                else:                                       # 판의 원래 색이 다른색깔이면 +1
                    count += 1

    for i in range(N):
        box(i)
    print(count)

        # arr = [[color] * (r2-r1) for _ in range(c1, c2+1)]
        # print(arr)
        # return arr

    box(1)
    # for i in range(N):                    # box index 설정
    #     box(i)

        # for j in range(r1,r2+1):
        #     for k in range(c1, c2+1):

