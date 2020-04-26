# Functions that returns another function and save the scope of outer variables
def outer_function(msg):
    def inner_function(name):
        print(msg + ' ' + name)
    return inner_function


# Save parameter 'msg' as 'Hi'
hi_func = outer_function('Hi')
# Save parameter 'msg' as 'Bye'
bye_func = outer_function('Bye')
hi_func('Ivan')
bye_func('Aaron')
