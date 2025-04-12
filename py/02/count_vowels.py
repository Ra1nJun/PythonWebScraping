a = "Python is awesome"
b = "aeiouAEIOU"
cnt = 0

for c in a:
    if c in b:
        cnt+=1

print(cnt)