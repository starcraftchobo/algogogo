import sys
sys.stdin = open('sample_input.txt', 'r')

'''
여는괄호면 집어넣고
닫는괄호면 짝에 맞는 여는괄호를 빼고
닫는괄호인데 top이 짝에 맞지않으면
암것도 아니면 continue
break&print 0
'''
def inspection(letters):
    stack = []
    top = -1
    for letter in letters:
        if letter == '{' or letter == '(':
            stack.append(letter)
            top += 1
        elif letter != '}' and letter != ')':
            continue
        else:
            if letter == '}':
                if stack and stack[top] == '{':
                    stack.pop()
                    top -= 1
                else:
                    return 0
            elif letter == ')':
                if stack and stack[top] == '(':
                    stack.pop()
                    top -= 1
                else:
                    return 0
    else:
        if stack:
            return 0
        else:
            return 1

T = int(input())
for tc in range(1, T+1):
    print(f'#{tc}', end=' ')
    letters = input()

    print(inspection(letters))
