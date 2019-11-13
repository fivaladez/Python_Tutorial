# Chai comparisions
x, y, z = 1, 2, 3
x > y > z  # Short for of x > y and y > z
# As soon as one comparison returns False, the expression evaluates immediately to False,
# skipping all remaining comparisons.

a = 'Python is fun!'
b = 'Python is fun!'
a == b  # returns True
a is b  # returns False

# a == b compares the value of a and b.
# a is b will compare the identities of a and b.

# Exeptions
a = 'short'
b = 'short'
c = 5
d = 5
a is b  # True
c is d  # True

#  strings will be compared lexicographically, which is similar to alphabetical order.
"alpha" < "beta"
# True
"gamma" > "beta"
# True
"gamma" < "OMEGA"
# False

'12' != '12'
# False
'12' == '12'
# True
