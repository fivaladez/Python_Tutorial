d = {}  # empty dict
d = {'key': 'value'}  # dict with initial values

# dict comprehension
d = {k: v for k, v in [('key', 'value',)]}

d = dict()  # empty dict
d = dict(key='value')  # explicit keyword arguments
d = dict([('key', 'value')])  # passing in a list of key/value pairs

d['newkey'] = 42
del d['newkey']

# Avoiding KeyError Exceptions
mydict = {}
print(mydict)  # {}
print(mydict.get("foo", "bar"))  # bar

try:
    value = mydict["foo"]
except KeyError:
    value = "bar"

if "foo" in mydict:
    value = mydict["foo"]
else:
    value = "bar"

# Iterating
d = {'a': 1, 'b': 2, 'c': 3}
for key in d:
    print(key, d[key])
# print([key for key in d])

for key, value in d.items():
    print(key, value)

# Merging Dictionaries
fish = {'name': "Nemo", 'hands': "fins", 'special': "gills"}
dog = {'name': "Clifford", 'hands': "paws", 'color': "red"}
fishdog = {**fish, **dog}
print(fishdog)

# Values can also be lists
mydict = {'a': [1, 2, 3], 'b': ['one', 'two', 'three']}
# Use list.append() method to add new elements to the values list
mydict['a'].append(4)  # => {'a': [1, 2, 3, 4], 'b': ['one', 'two', 'three']}
mydict['b'].append('four')  # => {'a': [1, 2, 3, 4], 'b': ['one', 'two', 'three', 'four']}

dict(a=1, b=2, c=3)  # {'a': 1, 'b': 2, 'c': 3}
dict([('d', 4), ('e', 5), ('f', 6)])  # {'d': 4, 'e': 5, 'f': 6}
dict([('a', 1)], b=2, c=3)  # {'a': 1, 'b': 2, 'c': 3}
dict({'a': 1, 'b': 2}, c=3)  # {'a': 1, 'b': 2, 'c': 3}
