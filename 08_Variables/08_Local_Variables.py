# If a name is bound inside a function, it is by default accessible only within the function:


def foo():
    if True:
        a = 5
    print(a)  # ok


b = 3


def bar():
    if False:
        b = 5
    print(b)  # UnboundLocalError: local variable 'b' referenced before assignment
