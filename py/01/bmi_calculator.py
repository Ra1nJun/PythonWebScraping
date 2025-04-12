weight = int(input("몸무게(kg)를 입력해주세요"))
height = int(input("키(cm)를 입력해주세요"))
BMI = weight/(height/100)**2
# BMI = weight / height**2

print(f'체중(kg): {weight}')
print(f'키(cm): {height}')
print(f'BMI: {BMI:.1f}')