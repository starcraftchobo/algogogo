import sys
sys.stdin = open('sample_input.txt', 'r')

T = int(input())
for tc in range(1, T+1):
    print(f'#{tc}', end=' ')
    letters = input()
    stack = []
    pointer = -1

    for letter in letters:
        if stack and letter == '}' and stack[pointer]

        if letter == '{' or letter == '(':
            stack.append(letter)
            pointer += 1




        elif stack and letter == '}':
            if stack[pointer] == '{':
                stack.pop()
                pointer -= 1
            else:
                print('0')
                break
        elif stack and letter == ')':
            if stack[pointer] == '(':
                stack.pop()
                pointer -= 1
            else:
                print('0')
                break
    if stack:
        print('0')
    else:
        print('1')