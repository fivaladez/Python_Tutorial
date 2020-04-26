# Function that takes another function as argument (callback) and returns a function


def decorator_function(original_function):
    #  *args and **kwards allow us to pass any number of parameters - the name is given for convention
    def wrapper_function(*args, **kwargs):
        print('wrapper executed this before {}'.format(
            original_function.__name__))
        return original_function(*args, **kwargs)
    return wrapper_function


class decorator_class():
    def __init__(self, original_function):
        self.original_function = original_function

    def __call__(self, *args, **kwargs):
        print('call method executed this before {}'.format(
            self.original_function.__name__))
        return self.original_function(*args, **kwargs)


def display():
    print('display function ran\n')

# It mean that display2 will be pass automatically as argument to decorator_function
@decorator_function
# @decorator_class
def display2():
    print('display2 function ran\n')


@decorator_function
# @decorator_class
def display_info(name, age):
    print('display_info ran with arguments ({}, {})\n'.format(name, age))


decorated_display = decorator_function(display)
decorated_display()

display2()

display_info('Ivan', 24)