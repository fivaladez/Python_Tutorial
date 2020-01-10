# [ <expression> for <element> in <iterable> if <condition> ]

squares = [x * x for x in (1, 2, 3, 4)]  # squares: [1, 4, 9, 16]

# Get a list of uppercase characters from a string
[s.upper() for s in "Hello World"]
# ['H', 'E', 'L', 'L', 'O', ' ', 'W', 'O', 'R', 'L', 'D']

# When using if/else together use them before the loop
[x if x in 'aeiou' else '*' for x in 'apple']
# ['a', '*', '*', '*', 'e']

# Double iteration


def foo(i):
    return i, i + 0.5


for i in range(3):
    for x in foo(i):
        yield str(x)

#  [... for x in ... for y in ...]
[str(x) for i in range(3) for x in foo(i)]

[x if x % 2 == 0 else None for x in range(10)]
# Out: [0, None, 2, None, 4, None, 6, None, 8, None]


def merge_the_tools(string, k):
    ls = list()
    for i in range(0, len(string), k):
        if i < len(string):
            ls.append(string[i:k+i])
        elif i > len(string):
            ls.append(string[i:])

    st = set()
    for (index, item) in enumerate(ls):
        for e in item:
            st.add(e)
        ls[index] = "".join(sorted(st))
        st = set()
        print(ls[index])
