list_bf = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]# 짝수는 제곱, 홀수는 그대로인 새 리스트를 생성하세요. (조건부 리스트 컴프리헨션 사용)
list_af = [a**2 if a%2==0 else a for a in list_bf]

print(list_af)