############## 주의 ##############
# 입력을 받기위한 input 함수는 절대 사용하지 않습니다.
# 내장함수 len 함수를 사용하지 않습니다.
def longest_string(str_list):
    lst_count = []
    length = 0
    for string in str_list:# 각 단어의 글자수 리턴
        count = 0
        length += 1
        for letter in string:
            count += 1
        lst_count.append(count)

    maximum = lst_count[0]
    for idx in range(length):
        if maximum < lst_count[idx]:
            maximum = lst_count[idx]
            a = idx

    return str_list[a]
        
    


# 추가 테스트를 위한 코드 작성 가능
# 예) print(함수명(인자))

#####################################################
# 아래 코드를 삭제하는 경우 
# 모든 책임은 삭제한 본인에게 있습니다. 

print(longest_string(["apple", "banana", "cherry", "date"]))  # "banana"
print(longest_string(["cat", "caterpillar", "dog", "elephant"]))  # "caterpillar"
print(longest_string(["a", "ab", "abc", "abcd"]))  # "abcd"
