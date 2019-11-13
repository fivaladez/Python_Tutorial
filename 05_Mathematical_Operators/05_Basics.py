import operator  # contains 2 argument arithmetic functions for the examples
import math

a, b = 1, 2

# Using the "+" operator:
print(a + b)  # = 3
operator.add(a, b)  # = 5 since a is set to 3 right before this line

# Using the "-" operator:
print(b - a)  # = 1
operator.sub(b, a)  # = 1

print(a * b)  # = 2
operator.mul(a, b)  # = 2

print(a / b)  # = .5
operator.truediv(a, b)  # = .5
operator.floordiv(a, b)  # = 1
# In Python 3 the / operator performs 'true' division regardless of types.
# In Python 2 the result of the '/' operator depends on the type of the numerator and denominator

print(a ** b)  # = 1
pow(a, b)  # = 1
math.pow(a, b)  # = 1.0 (always float; does not allow complex results)
operator.pow(a, b)  # = 1

print(a % b)  # 1
operator.mod(a, b)  # 1
