# Examples


import time


def my_timer(origin_func):
    import time

    def wrapper(*args, **kwargs):
        t1 = time.time()
        result = origin_func(*args, **kwargs)
        t2 = time.time() - t1
        print('{} ran in: {} sec\n'.format(origin_func.__name__, t2))
        return result

    return wrapper


@my_timer
def display_info(name, age):
    time.sleep(1)
    print('display_info ran with arguments ({}, {})'.format(name, age))


display_info('Ivan', 24)
display_info('Susana', 23)
display_info('Aaron', 20)
