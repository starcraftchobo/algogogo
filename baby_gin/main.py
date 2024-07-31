#baby_gin은 못하니까 순열만들기 ㅎㅎ..
for i1 in range(3):
    for i2 in range(3):
        if i2 != i1:
            for i3 in range(3):
                if i3 != i1 and i3 != i2:
                    print(i1, i2, i3)


#greey algorithm으로 구현 예시
i = 0
tri = run = 0
while i < 10