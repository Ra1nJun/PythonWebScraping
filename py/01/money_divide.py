money = 10000
people = 3
penny = money % people

result = int((money-penny)/people)

print(f'각자 {result}원을 받고 {penny}원이 남습니다')