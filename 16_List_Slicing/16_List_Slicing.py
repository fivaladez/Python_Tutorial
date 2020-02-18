lst = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
lst[::2]
# Output: ['a', 'c', 'e', 'g']
lst[::3]
# Output: ['a', 'd', 'g']

lst = ['a', 'b', 'c', 'd', 'e']
lst[2:4]
# Output: ['c', 'd']
lst[2:]
# Output: ['c', 'd', 'e']
lst[:4]
# Output: ['a', 'b', 'c', 'd']

a = [1, 2, 3, 4, 5]
# steps through the list backwards (step=-1)
b = a[::-1]
# built-in list method to reverse 'a'
a.reverse()
if a == b:
    print(True)
print(b)
# Output:
# True
# [5, 4, 3, 2, 1]


def shift_list(array, s):
    """Shifts the elements of a list to the left or right.
    Args:
    array - the list to shift
    s - the amount to shift the list ('+': right-shift, '-': left-shift)
    Returns:
    shifted_array - the shifted list
    """
    # calculate actual shift amount (e.g., 11 --> 1 if length of the array is 5)
    s %= len(array)
    # reverse the shift direction to be more intuitive
    s *= -1
    # shift array with list slicing
    shifted_array = array[s:] + array[:s]
    return shifted_array


my_array = [1, 2, 3, 4, 5]
# negative numbers
print(shift_list(my_array, -7))
# no shift on numbers equal to the size of the array
print(shift_list(my_array, 5))
# works on positive numbers
print(shift_list(my_array, 3))
