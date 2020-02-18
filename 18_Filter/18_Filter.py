names = ['Fred', 'Wilma', 'Barney', 'Ivan', 'Francisco']


def long_name(name):
    return len(name) > 5


print(list(filter(long_name, names)))
# Out: ['Barney']
[name for name in names if len(name) > 5]  # equivalent list comprehension
# Out: ['Barney']
