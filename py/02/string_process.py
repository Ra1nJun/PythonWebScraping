a = "Hello"
b = "World"
c = a+" "+b
d = "Python is fun"
e = "abcdef"

print(c)

print(c.upper())

print(c[6:])

print(d.split(" "))

for i in range(len(e)):
    if i%2 == 0:
        print(e[i], end="")
print("")

for i in range(3):
    print(a, end="")
print("")
