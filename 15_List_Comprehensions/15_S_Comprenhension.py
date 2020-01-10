# A set containing every value in range(5):
{x for x in range(5)}
# Out: {0, 1, 2, 3, 4}
# A set of even numbers between 1 and 10:
{x for x in range(1, 11) if x % 2 == 0}
# Out: {2, 4, 6, 8, 10}
# Unique alphabetic characters in a string of text:
text = "When in the Course of human events it becomes necessary for one people..."
{ch.lower() for ch in text if ch.isalpha()}
# Out: set(['a', 'c', 'b', 'e', 'f', 'i', 'h', 'm', 'l', 'o',
# 'n', 'p', 's', 'r', 'u', 't', 'w', 'v', 'y'])
