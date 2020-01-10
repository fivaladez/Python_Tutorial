d = {x: x * x for x in (1, 2, 3, 4)}
# Out: {1: 1, 2: 4, 3: 9, 4: 16}
print(d)

initial_dict = {'x': 1, 'y': 2}
{key: value for key, value in initial_dict.items() if key == 'x'}
# Out: {'x': 1}

# invert dictionary
my_dict = {1: 'a', 2: 'b', 3: 'c'}
swapped = {v: k for k, v in my_dict.items()}
