id = "901212-1234567"

birth_y = id[:2]
birth_m = id[2:4]
birth_d = id[4:6]

if (int(birth_y) > 25):
    print(f'19{birth_y}년 {birth_m}월 {birth_d}일')
else:
    print(f'20{birth_y}년 {birth_m}월 {birth_d}일')