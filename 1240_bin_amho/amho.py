import sys
sys.stdin = open("input.txt", "r")

# 어떤 국가에서는 자국 내 방송국에서 스파이가 활동하는 사실을 알아냈다. 스파이는 영상물에
# 암호 코드를 삽입하여 송출하고 있었는데 이 암호코드들을 빠르고 정확하게 인식할 수 있는 스캐너를 개발하려고 한다.
# 문제 풀맛 나는 맛도리 스토리..!

'''
0. input을 어케 받을꼬..?
    일단 다 받고 0만잇는거 쳐내기로 ㄱㄱ
    하려다가 set로 받아버리기
1. 암호문을 어케 특정하지..? - 마지막 1 찾아서 슬라이싱
2. 숫자 암호는 규칙성이 안보이니 걍 10개 다만들지 뭐
3. 숫자 판별해주는 함수에 7개씩 나눈거 집어넣넣 
4. 시키는대로 한다음 나머지 0이면 다 더해뿐거, 아니면 0 출력
'''

def 변환기(숫자덩이):
    if 숫자덩이 == '0001101':
        return 0
    elif 숫자덩이 == '0011001':
        return 1
    elif 숫자덩이 == '0010011':
        return 2
    elif 숫자덩이 == '0111101':
        return 3
    elif 숫자덩이 == '0100011':
        return 4
    elif 숫자덩이 == '0110001':
        return 5
    elif 숫자덩이 == '0101111':
        return 6
    elif 숫자덩이 == '0111011':
        return 7
    elif 숫자덩이 == '0110111':
        return 8
    else:
        return 9

def valid(lst):
    hap = ans = 0
    for i in range(4):
        hap += 3*lst[2*i]
        hap += lst[2*i+1]

        ans += lst[2*i]
        ans += lst[2*i+1]

    if hap % 10:            # hap의 나머지가 0이 아니면
        return 0
    else:                   # ans 출력
        return ans

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    N, M = map(int, input().split())
    codes = set(input() for _ in range(N))  # {'00000000...', '0001010101011110..'}, 원소가 단 두개!
    # print(codes)

    while True:                             # 두개 중 코드 뽑기
        dirty_code = codes.pop()            # set에서는 무작위 원소가 뿅
        if int(dirty_code):                 # 0이 아니면 멈춰!
            break
    # print(dirty_code)
    for j in range(M-1, -1, -1):            # 뒤에서부터 1찾기
        if int(dirty_code[j]):              # 뒷덜미가 1이면
            code = dirty_code[j-55:j+1]     # 걔부터 앞에 56개 추출
            break
    # print(len(code), code)

    resol = []
    for k in range(0, 56, 7):               # 변환해서 resol에 넣어주는거
        num = 변환기(code[k:k+7])
        # print(num, end=' ')
        resol.append(num)                   # resol = [1, 2, 3, 4, 5, 6, 7, 8]
    # print()

    print(f'#{test_case} {valid(resol)}')