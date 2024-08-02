import sys
sys.stdin = open("sample_input.txt", "r")

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    str1 = set(input())
    str2 = list(input())
    count_alpha = dict()

    for x in str2:
        if count_alpha.get(x) is None:
            count_alpha.update({x : 1})
        else:
            count_alpha.update({x : count_alpha.get(x)+1})

    maximum = 0
    for letter in str1:
        if maximum < count_alpha.get(letter):
            maximum = count_alpha.get(letter)

    print(f'#{test_case}', maximum)
