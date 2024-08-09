# import sys
# sys.stdin = open("input.txt", "r")


# stack.py

class Stack:
    def __init__(self, size):
        self.size = size
        self.items = [None] * self.size
        self.top = -1

    def is_empty(self):
        return True if (self.top == -1) else False

    def is_full(self):
        return True if (self.top + 1 == self.size) else False

    def push(self, item):
        if self.is_full():
            raise Exception('It is full')
        else:
            self.top += 1
            self.items[self.top] = item

    def peek(self):
        if self.is_empty():
            raise Exception('It is empty')
        else:
            return self.items[self.top]

    def pop(self):
        if self.is_empty():
            raise Exception('It is empty')
        else:
            value = self.items[self.top]
            self.items[self.top] = None
            self.top -= 1
            return value

    def __str__(self):
        result = '\n-----'
        for item in self.items:
            if item is None:
                result = f'\n|   |' + result
            else:
                result = f'\n| {item} |' + result
        return result


T = 10
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    calculator1 = Stack(2)
    N = int(input())
    sik = input()

    lst = []

    for i in range(N):
        if sik[i].isdigit():
            lst.append(int(sik[i]))
        else:
            lst.append(sik[i])


    # 후위표기법으로 변환
    for j in range(N-1):
        if lst[j] == '+':
            lst[j], lst[j+1] = lst[j+1], lst[j]

    # print(lst)
    # 후위 계산
    for y in lst:
        if y != '+':
            calculator1.push(y)
        else:
            a = calculator1.pop() + calculator1.pop()
            calculator1.push(a)
    print(f'#{test_case}', a)




    # 변환한 표기법으로 계산