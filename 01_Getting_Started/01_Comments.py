# This is a single line comment in Python
# This is a single line comment in Python
"""
This type of comment spans multiple lines.
These are mostly used for documentation of functions, classes and modules.
"""

# Syntax conventions - Sphinx
# Sphinx is a tool to generate HTML based documentation for Python projects based on docstrings.


def greet(name, greeting="Hello"):
    """Say hello to a person.

    :param name: the name of the person
    :type name: str
    :param greeting: the greeting to the person
    :type greeting: str
    :return:
    :rtype:
    """

    print("{} {}".format(greeting, name))


help(greet)
