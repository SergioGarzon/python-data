f: lambda x : x ** 2
g: lambda x: x + 1
h: lambda x: g(f(x))

print(h(3))

# print error