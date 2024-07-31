############## 주의 ##############
# 입력을 받기위한 input 함수는 절대 사용하지 않습니다.
# 내장 함수 sum, len 함수를 사용하지 않습니다.
def average_population(population_list):
    count = 0 #마을 개수+유령 마을
    sum_people = 0 # 마을 사람 총합

    for village in population_list:
        count += 1
    print(count)
    
    for people in population_list:
        sum_people += people
    print(sum_people)

    avg = sum_people / count
    
    print(type(avg))#반환값 타입 확인
    
    return avg
# 추가 테스트를 위한 코드 작성 가능
# 예) print(함수명(인자))

#####################################################
# 아래 코드를 삭제하는 경우 
# 모든 책임은 삭제한 본인에게 있습니다. 
############## 테스트 코드 삭제 금지 #################
print(average_population([1000, 2000, 3000, 4000, 5000]))   # 3000.0
print(average_population([1500, 2500, 3500]))               # 2500.0
print(average_population([1234, 5678, 91011]))              # 32641.0
#####################################################