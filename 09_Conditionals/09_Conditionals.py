# Ternary Operator
n = 5
"Greater than 2" if n > 2 else "Smaller than or equal to 2"
# Out: 'Greater than 2'

#  if, elif, and else
m = 3
if n > 2 and m > 2:
    print("Number is bigger than 2.")
elif n < 2 or m < 2:  # Optional clause (you can have multiple elifs)
    print("Number is smaller than 2.")
else:  # Optional clause (you can only have one else)
    print("Number is 2.")
