############## 주의 ##############
# 입력을 받기위한 input 함수는 절대 사용하지 않습니다.
def calculate_days_to_fill_tank(tank_capacity, fill_amount, evaporation_amount):
    current_amount = 0 #현재 물의 양
    count = 0 #걸린 날짜
    
    while tank_capacity > current_amount: #현재 용량이 총 용량보다 작으면 물 채우고 날짜 +1
        current_amount += fill_amount
        count += 1
        if current_amount < tank_capacity: #현재 용량이 총 용량보다 작으면 물 증발
            current_amount -= evaporation_amount

    return count    

        


# 추가 테스트를 위한 코드 작성 가능
# 예) print(함수명(인자))

#####################################################
# 아래 코드를 삭제하는 경우 
# 모든 책임은 삭제한 본인에게 있습니다. 
############## 테스트 코드 삭제 금지 #################
print(calculate_days_to_fill_tank(100, 20, 5))  # 7
print(calculate_days_to_fill_tank(1000, 100, 10))  # 11
print(calculate_days_to_fill_tank(100, 10, 1))  # 11
#####################################################
