def cl_mul(a, b):
    r = 0  # Initialize the result to 0
    while a > 0:
        if a & 1:  # Check if the least significant bit of 'a' is 1
            r ^= b  # Perform XOR (carry-less addition)
        a >>= 1  # Right-shift 'a' by 1
        b <<= 1  # Left-shift 'b' by 1
    return r

# Example usage
a = 5  # Binary: 11
b = 3  # Binary: 101
result = cl_mul(a, b)
print(f"cl_mul({a}, {b}) = {result}")  # Output: cl_mul(3, 5) = 15

# Example usage
a = 3  # Binary: 11
b = 5  # Binary: 101
result = cl_mul(a, b)
print(f"cl_mul({a}, {b}) = {result}")  # Output: cl_mul(3, 5) = 15


def or_mul(a, b):
    r = 0  # Initialize the result to 0
    while a > 0:
        if a & 1:  # Check if the least significant bit of 'a' is 1
            r |= b  # Perform XOR (carry-less addition)
        a >>= 1  # Right-shift 'a' by 1
        b <<= 1  # Left-shift 'b' by 1
    return r

# Example usage
a = 5  # Binary: 11
b = 3  # Binary: 101
result = cl_mul(a, b)
print(f"or_mul({a}, {b}) = {result}")  # Output: cl_mul(3, 5) = 15

# Example usage
a = 3  # Binary: 11
b = 5  # Binary: 101
result = cl_mul(a, b)
print(f"or_mul({a}, {b}) = {result}")  # Output: cl_mul(3, 5) = 15
