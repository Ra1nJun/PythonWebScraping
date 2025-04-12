a_list = [1,2,3]
b_list = [4,5,6]

c_list = list(map(lambda x,y: x+y, a_list, b_list))
print(c_list)