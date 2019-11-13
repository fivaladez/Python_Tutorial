class Foo(object):
    def __init__(self, item):
        self.my_item = item

    def __eq__(self, other):
        return self.my_item == other.my_item


a = Foo(5)
b = Foo(5)
a == b  # True
a != b  # False
a is b  # False
