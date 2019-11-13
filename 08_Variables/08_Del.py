x = 5


def foo():
    global x
    x = 4
    y = 0

    def foo2():
        nonlocal y
        y = 7

    foo2()
    print(y)
    print(x)

    del x
    del y


foo()

"""
Note that del is a binding occurrence, which means that unless explicitly stated otherwise
(using nonlocal or global), del v will make v local to the current scope. If you intend to
delete v in an outer scope, use nonlocal v or global v in the same scope of the del v statement.
"""
