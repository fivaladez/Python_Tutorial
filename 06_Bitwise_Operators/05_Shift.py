# 2 = 0b0010
2 << 2
# Out: 8
# 8 = 0b1000
bin(2 << 2)
# Out: 0b1000

# Performing a left bit shift of 1 is equivalent to multiplication by 2:
7 << 1
# Out: 14

# 8 = 0b1000
8 >> 2
# Out: 2
# 2 = 0b10
bin(8 >> 2)
# Out: 0b10

# Performing a right bit shift of 1 is equivalent to integer division by 2
36 >> 1
# Out: 18
