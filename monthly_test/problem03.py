############## 주의 ##############
# 입력을 받기위한 input 함수는 절대 사용하지 않습니다.
# 리스트 메서드 count 를 사용하지 않습니다.
def count_treasures(treasure_list):
    # def remove(*asdf):
    dict = {}
    for key in treasure_list:
        if dict.get(key) == None:
            dict.update({f'{key}' : 1})
        else:
            dict.update({f'{key}' : dict[f'{key}']+1})
    return dict

# dict = {}
# dict = {'asdf' : 1}
# dict.update({'aaff' : 2})
# print(dict)

        # if dict(asdf) != None
        #     {asdf : dict{asdf}+1}
# 추가 테스트를 위한 코드 작성 가능
# 예) print(함수명(인자))

#####################################################
# 아래 코드를 삭제하는 경우 
# 모든 책임은 삭제한 본인에게 있습니다. 
############## 테스트 코드 삭제 금지 #################
print(count_treasures(["gold", "silver", "diamond", "gold", "silver"]))  # {'gold': 2, 'silver': 2, 'diamond': 1}
print(count_treasures(["pearl"]))  # {'pearl': 1}
#####################################################
