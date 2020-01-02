# enumerate
print("\n")
ls = ['one', 'two', 'three', 'four']
for index, item in enumerate(ls):
    print(index, '::', item)
else:
    print("Done")

# Map
print("\n")
x = list(map(lambda e: e.upper(), ls))
print(x)

# Dictionaries
print("\n")
d = {"a": 1, "b": 2, "c": 3}
for key in d:
    print(key)
for value in d.values():
    print(value)
for key, value in d.items():
    print(key, "::", value)

# Unpacking
print("\n")
collection = [('a', 'b', 'c'), ('x', 'y', 'z'), ('1', '2', '3')]
for item in collection:
    i1 = item[0]
    i2 = item[1]
    i3 = item[2]
    print(i1, i2, i3)
for item in collection:
    i1, i2, i3 = item
    print(i1, i2, i3)
for i1, i2, i3 in collection:
    print(i1, i2, i3)

for s in ls:
    print(s[:1])  # print the first letter
# list[start:end:amount]
for s in ls[1::2]:
    print(s)
