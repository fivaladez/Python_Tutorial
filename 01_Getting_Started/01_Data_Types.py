# Boolean types
x, y = False, True
x or y  # if x is False then y otherwise x
x and y  # if x is False then x otherwise y
not x  # if x is True then False, otherwise True

# =========== Sequences and collections ===========

# tuple: An ordered collection of n values  (n >= 0) that can't be modified
tuple = (1, 2, 3)
print(type(tuple))
# list: An ordered collection of n values (n >= 0). Not hashable; mutable.
list = [1, 2, 3]
print(type(list))
# set: An unordered collection of unique values. Items must be hashable.
set = {1, 2, 'a'}
print(type(set))
# dict: An unordered collection of unique key-value pairs; keys must be hashable.
dictionary = {1: 'one', 2: 'two'}
print(type(dictionary))

# An object is hashable if it has a hash value which never changes during its lifetime

# =========== Converting between datatypes ===========

a = '123'
print(int(a))

a = 'hello'
print(list(a))   # ['h', 'e', 'l', 'l', 'o']
print(set(a))    # {'o', 'e', 'l', 'h'}
print(tuple(a))  # ('h', 'e', 'l', 'l', 'o')
