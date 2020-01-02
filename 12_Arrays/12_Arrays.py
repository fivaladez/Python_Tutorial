# An array is a data structure that stores values of same data type. In Python, this is the main
# difference between arrays and lists.
from array import *

my_array = array('i', [1, 2, 3, 4])

for i in my_array:
    print(i)
my_array.append(6)
my_array.insert(0, 0)

my_extnd_array = array('i', [7, 8, 9, 10])
my_array.extend(my_extnd_array)
# array('i', [0, 1, 2, 3, 4, 6, 7, 8, 9, 10])

c = [11, 12, 13]
my_array.fromlist(c)
# array('i', [0, 1, 2, 3, 4, 6, 7, 8, 9, 10, 11, 12, 13])

my_array.remove(4)
my_array.pop()
print(my_array.index(3))

my_array.reverse()
print(my_array.buffer_info())
my_array.count(3)


my_array = array('i', [1, 2, 3, 4, 5])
c = my_array.tolist()
# [1, 2, 3, 4, 5]
