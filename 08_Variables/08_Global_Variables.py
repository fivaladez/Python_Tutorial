x = 'Hi'


def change_local_x():
    x = 'Bye'  # x appears in an assignment, therefore it's local
    print(x)


def see_global_x():
    print(x)  # x is just referenced, therefore assumed global


def change_global_x():
    global x
    # The global keyword means that assignments will happen at the module's top level,
    # not at the program's top level
    x = 'Good Bye'
    print(x)


change_local_x()  # prints Bye
see_global_x()  # prints Hi
change_global_x()  # prints Good Bye
