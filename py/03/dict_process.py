dict_a = {"name": "John", "age": 30}
dict_b = {"math": 90, "science": 85, "history": 78} 
dict_c = {'apple': 3, 'banana': 5}

print(f'나이: {dict_a["age"]}')

print(f'과목들: {list(dict_b.keys())}')

dict_c["apple"] += 2
print(dict_c)