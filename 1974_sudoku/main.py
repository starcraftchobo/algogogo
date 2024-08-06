# import sys
# sys.stdin = open("input.txt", "r")

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    print(f'#{test_case}', end=' ')
    sudoku = list()
    result = 1

    for _ in range(9):
        sudoku.append(list(map(int, input().split())))
    
    for i in range(0, 9, 3):
        for j in range(0, 9, 3):
            c = len({sudoku[i][j], sudoku[i][j+1], sudoku[i][j+2], sudoku[i+1][j], sudoku[i+1][j+1], sudoku[i+1][j+2],sudoku[i+2][j],sudoku[i+2][j+1], sudoku[i+2][j+2]})
            if c !=9:
                result = 0
                break

    if c!= 9:
        result = 0
    else:
        for i in range(9):
            a = len(set(sudoku[i]))
            if a !=9:
                result = 0
                break
    # for i in range(9):
            b = len({sudoku[x][i] for x in range(9)})
            if b !=9:
                result = 0
                break
        

    print(result)