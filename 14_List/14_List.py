a = [1, 2, 3, 4, 5]
# Append values
a.append(7)
a.append(7)
# Append another list
b = [8, 9]
a.append(b)
# Append an element of a different type, as list elements do not need to have the same type
my_string = "hello world"
a.append(my_string)
# a: [1, 2, 3, 4, 5, 6, 7, 7, [8, 9], "hello world"]
a = [1, 2, 3, 4, 5, 6, 7, 7]
b = [8, 9, 10]
# Extend list by appending all elements from b
a.extend(b)
# a: [1, 2, 3, 4, 5, 6, 7, 7, 8, 9, 10]
# Extend list with elements from a non-list enumerable:
a.extend(range(3))
# a: [1, 2, 3, 4, 5, 6, 7, 7, 8, 9, 10, 0, 1, 2]

a = [1, 2, 3, 4, 5, 6] + [7, 7] + b
# a: [1, 2, 3, 4, 5, 6, 7, 7, 8, 9, 10]

a.index(7)  # Returns: 6
a.pop(7)    # Returns 7
a.pop()     # Returns 10
a.remove(9)
a.reverse()
a.count(7)
a.sort()
a.sort(reverse=True)
# removes all items from the list
a.clear()
# a = []
b = ["blah"] * 3
# b = ["blah", "blah", "blah"]
a = list(range(10))
del a[::2]
# a = [1, 3, 5, 7, 9]
del a[-1]
# a = [1, 3, 5, 7]
del a[:]
# a = []

# Copy a list
new_list = a[:]
lst = [1, 2, 3, 4]
lst[1:]  # [2, 3, 4]
lst[:3]  # [1, 2, 3]
lst[::2]  # [1, 3]
lst[::-1]  # [4, 3, 2, 1]
lst[-1:0:-1]  # [4, 3, 2]
lst[5:8]  # [] since starting index is greater than length of lst, returns empty list
lst[1:10]  # [2, 3, 4] same as omitting ending index

# Checking if list is empty
if lst:
    print("List not empty")

# Iterating
my_list = ['foo', 'bar', 'baz']
for item in my_list:
    print(item)

for (index, item) in enumerate(my_list):
    print('The item in position {} is: {}'.format(index, item))

# Checking whether an item is in a lis
lst = ['test', 'twest', 'tweast', 'treast']
'test' in lst
# Out: True
'toast' in lst
# Out: False

# Any and All
# You can use all() to determine if all the values in an iterable evaluate to True
nums = [1, 1, 0, 1]
all(nums)
# False
chars = ['a', 'b', 'c', 'd']
all(chars)
# True

# any() determines if one or more values in an iterable evaluate to True
nums = [1, 1, 0, 1]
any(nums)
# True
vals = [None, None, None, False]
any(vals)
# False

# zip returns a list of tuples
alist = ['a1', 'a2', 'a3']
blist = ['b1', 'b2', 'b3']
for a, b in zip(alist, blist):
    print(a, b)
# Output:
# a1 b1
# a2 b2
# a3 b3
