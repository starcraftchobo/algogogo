############## 주의 ##############
# 입력을 받기위한 input 함수는 절대 사용하지 않습니다.
# 내장 함수 min, max, sorted 함수 리스트 메서드 sort 를 사용하지 않습니다.
def population_difference(population_list):
    population_max = 0
    
    for population in population_list:
        if population_max <= population:
            population_max = population #인구수가 더 큰 값을 max에 넣음

    population_min = population_max #최초 min값을 max로 설정

    for population in population_list:
        if population_min >= population:
            population_min = population #인구수가 더 작은 값을 min에 넣음

    difference = population_max - population_min
    return difference

# 추가 테스트를 위한 코드 작성 가능
# 예) print(함수명(인자))

#####################################################
# 아래 코드를 삭제하는 경우 
# 모든 책임은 삭제한 본인에게 있습니다. 
############## 테스트 코드 삭제 금지 #################
print(population_difference([100, 200, 300, 400, 500]))  # 400
print(population_difference([50, 150, 250]))  # 200
print(population_difference([10, 20, 30, 40, 50, 60, 70, 80, 90, 100]))  # 90
#####################################################
