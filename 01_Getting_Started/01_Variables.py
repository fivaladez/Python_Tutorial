# Verify if Python is installed: python --version
# Run commands as a string:  python -c 'print("Hello, World")'

# Rules for variable naming:
# 1. Variables names must start with a letter or an underscore.
# 2. The remainder of your variable name may consist of letters, numbers and underscores
# 3. Names are case sensitive

import keyword

# Integer
a = 2
print(type(a))
# Integer
b = 9223372036854775807
print(type(b))
# Floating point
pi = 3.14
print(type(pi))
# String
c = 'A'
print(type(c))
# String
name = 'John Doe'
print(type(name))
# Boolean
q = True
print(type(q))
# Empty value or null data type
x = None
print(type(x))

print(keyword.kwlist)

a, b, c = 1, 2, 3
print(a, b, c)
a = b = c = 1  # all three names a, b and c refer to same int object with value 1
print(a, b, c)
x = y = [7, 8, 9]  # x and y refer to the same list object just created, [7, 8, 9]
print(x, y)

# Python uses indentation (4 spaces) to define control and loop constructs.
