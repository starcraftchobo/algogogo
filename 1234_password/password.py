import sys
sys.stdin = open('input.txt', 'r')
'''
1. stack 구현
2. 문자열 순회하며 스택에 하나씩 추가
3. 순회하는 문자가 top의 놈과 같으면 top pop
4. 스택 출력
'''
T = 10
for tc in range(1, T+1):
    N, password = input().split()

    stack = []
    top = -1
    for num in password:
        if stack and num == stack[top]:
            stack.pop()
            top += -1
        else:
            stack.append(num)
            top += 1

    print(f'#{tc}', ''.join(stack))