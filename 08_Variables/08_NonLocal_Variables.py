# Python 3 added a new keyword called nonlocal. The nonlocal keyword adds a scope override
# to the inner scope


def counter():
    num = 0

    def incrementer():
        nonlocal num  # It shall be inside a nested function
        num += 1
        return num

    return incrementer


c = counter()
print(c())  # = 1
print(c())   # = 2
print(c())   # = 3
