import sys
sys.stdin = open('sample_input.txt', 'r')

T = int(input())
for tc in range(1, T+1):
    print(f'#{tc}', end=' ')
    letters = input()
    stack = []
    pointer = -1
    for letter in letters:
        if stack and stack[pointer] == letter:
            stack.pop()
            pointer -= 1
        else:
            stack.append(letter)
            pointer += 1
    if stack:
        print(len(stack))
    else:
        print('0')