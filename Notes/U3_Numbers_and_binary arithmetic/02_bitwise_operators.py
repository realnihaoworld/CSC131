

# Bitwise OR is | (pipe)
# Bitwise AND is &
# Bitwise NOT is ~
# Bitwise XOR is ^

#Examples
x = 0b0101
y = 0b1111

# AND
z = x & y
# should produce 0101
print(bin(z))

# OR
z = x | y
# should produce 1111
print(bin(z))

# XOR
z = x ^ y
# should produce 1010
print(bin(z))

# NOT
z = ~x
#should produce 1010
print(bin(z)) # python gives strange result because of two's complement
print(bin(z & 0b1111))
