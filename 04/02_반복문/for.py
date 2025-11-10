# 1) string
print(f"{'1) string':=^50}")

str1 = 'Hello World'

for i in str1:
    print(i)

# 2) list
print(f"{'2) list':=^50}")
list1 = ['a', 'b', 'c', [1, 2, 3]]

for i in list1:
    print(i)

# 3) tuple
print(f"{'3) tuple':=^50}")
tuple1 = ('a', 'b', 'c', [1, 2, 3])

for i in tuple1:
    print(i)
# 4) dict
print("{0:=^50}".format('4) dict'))
dict1 = {'k1': 'v1', 'k2': 'v2', 'k3': 'v3'}

for i in dict1:
    print(i)

for k,v in dict1.items():
    print(k, v)

# 5) set
print(f'{"5) set":=^50}')
set1 = {'a', 'b', 'c'}

for i in set1:
    print(i)
