def bin_to_deci(number):
    return int(number, 2)

def changer(str_num):
    num_lst = []
    dec_lst = []
    for i in range(0, len(str_num), 7):
        num_lst.append(str_num[i:i+7])

    for num in num_lst:
        dec_num = bin_to_deci(num)
        dec_lst.append(dec_num)

    return dec_lst

bin_num = input()
print(*changer(bin_num))