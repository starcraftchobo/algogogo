import sys, time
sys.stdin = open('sample_input.txt', 'r')
'''
isdigit으로 숫자판별
아니면 각각에 따라 계산하고 append or return
숫자 하나밖에 없는데 연산자 나오는 경우
첫빠따부터 연산자 나오는 경우
숫자가 연산자보다 많은 경우는 error일수도 아닐수도
'''
start = time.time()
def cal(a):
    if a.isdigit():
        stack.append(int(a))
        return
    elif a == '.':

    else:
        while len(stack) >= 2:
            if a == '+':
                result = stack.pop() + stack.pop()
                stack.append(result)
                return
            elif a == '-':
                result = stack.pop() - stack.pop()
                stack.append(result)
                return
            elif a == '*':
                result = stack.pop() * stack.pop()
                stack.append(result)
                return
            elif a == '/':
                result = stack.pop() // stack.pop()
                stack.append(result)
                return
            else:
                return 'error'
        if a == '.':
            if stack:
                print(stack.pop())
                return
            else:
                return 'error'
        else:
            return 'error'



T = int(input())
for tc in range(1, T+1):
    stack = []
    numbers = input().split()
    print(f'#{tc}', end=' ')
    for number in numbers:
        if cal(number) == 'error':
            print('error')
            break
end = time.time()
print(end - start)