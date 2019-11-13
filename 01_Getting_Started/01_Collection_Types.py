# =========== Strings ===========
str = "Hello World!"
print(str)  # output will be whole string. Hello World
print(str[0])  # output will be first character. H
print(str[0:5])  # output will be first five characters. Hello
# =========== Lists ===========
int_list = [1, 2, 3]
string_list = ['abc', 'defghi']
empty_list = []
mixed_list = [1, 'abc', True, 2.34, None]
nested_list = [['a', 'b', 'c'], [1, 2, 3]]

names = ['Alice', 'Bob', 'Craig', 'Diana', 'Eric', 'Alice']
print(names[0])  # Alice
print(names[2])  # Craig
print(names[-1])  # Eric
print(names[-4])  # Bob

# Lists are mutable, so you can change the values in a list:
names[0] = 'Ann'
print(names)
names.append("Sia")
print(names)
names.insert(1, "Nikki")
print(names)
names.remove("Bob")
print(names)
print(names.index("Alice"))
print(len(names))
print(names.count('Alice'))
names.reverse()
print(names)
names.pop()
print(names)
# Iterate a list
for name in names:
    print(name)

# =========== Tuples ===========
# A tuple is similar to a list except that it is fixed-length and immutable.
ip_address = ('10.20.30.40', 8080)
one_member_tuple = ('Only member',)
one_member_tuple = 'Only member',  # No brackets
one_member_tuple = tuple(['Only member'])

# =========== Dictionaries ===========
# A dictionary in Python is a collection of key-value pairs.
state_capitals = {
    'Arkansas': 'Little Rock',
    'Colorado': 'Denver',
    'California': 'Sacramento',
    'Georgia': 'Atlanta'
}
print(state_capitals['California'])
for k in state_capitals.keys():
    print('{} is the capital of {}'.format(state_capitals[k], k))
# Dictionaries strongly resemble JSON syntax.

# =========== Sets ===========
# A set is a collection of elements with no repeats and without insertion order but sorted order.
first_names = {'Adam', 'Beth', 'Charlie'}
my_list = [1, 2, 3]
my_set = set(my_list)
if 'Beth' in first_names:
    print('Beth')
