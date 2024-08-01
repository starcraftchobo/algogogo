############## 주의 ##############
# 입력을 받기위한 input 함수는 절대 사용하지 않습니다.
def max_adjacent_sum(matrix):
    matrix.insert([0]*len(matrix), 0)
    matrix.append([0]*len(matrix))
    for column in matrix:
        column.insert(0, 0)
        matrix.append(0)
    
    di = [0, -1, 0, 1]
    dj = [-1, 0, 1, 0]   
    
    sum_list = []

    for i in range(1, N+1):
        for j in range(1, N+1):
            for k in range(4):
                sum = matrix[][]

# 추가 테스트를 위한 코드 작성 가능
# 예) print(함수명(인자))

# 예시 행렬 데이터
matrix1 = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

matrix2 = [
    [9, 2, 3],
    [4, 5, 6],
    [7, 8, 1]
]

#####################################################
# 아래 코드를 삭제하는 경우 
# 모든 책임은 삭제한 본인에게 있습니다. 
############## 테스트 코드 삭제 금지 #################
print(max_adjacent_sum(matrix1))  # 29
print(max_adjacent_sum(matrix2))  # 25
#####################################################
