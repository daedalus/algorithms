import numpy as np

def fft_multiply(x, y):
    """
    Multiply two integers using Fast Fourier Transform (FFT).
    This implementation handles large integers and ensures precision.
    
    :param x: First integer
    :param y: Second integer
    :return: Product of x and y
    """
    # Convert the integers to digit lists (reverse to facilitate processing)
    x_digits = list(map(int, str(x)))[::-1]  # Reverse digits to process least significant first
    y_digits = list(map(int, str(y)))[::-1]

    # Determine the size for FFT, which should be at least the sum of the two numbers' lengths
    size = 1
    while size < len(x_digits) + len(y_digits):
        size *= 2
    size *= 2  # To ensure no wraparound effects during FFT

    # Pad both lists with zeros to the determined size
    x_digits.extend([0] * (size - len(x_digits)))
    y_digits.extend([0] * (size - len(y_digits)))

    # Apply FFT to both number digit arrays
    fft_x = np.fft.fft(x_digits)
    fft_y = np.fft.fft(y_digits)

    # Perform element-wise multiplication in the frequency domain
    fft_product = fft_x * fft_y

    # Apply inverse FFT to convert the result back to the time domain
    result_digits = np.fft.ifft(fft_product).real

    # Round and convert the result to integers, handling potential small errors
    result_digits = np.round(result_digits).astype(int)

    # Convert the result digits back into proper base-10 digits, handling carries
    result = []
    carry = 0
    for digit in result_digits:
        digit += carry
        carry = digit // 10
        result.append(digit % 10)

    # If there's a carry left, append it as new digits
    while carry:
        result.append(carry % 10)
        carry //= 10

    # Remove any leading zeros in the final result
    while len(result) > 1 and result[-1] == 0:
        result.pop()

    # Reverse the result to match the correct order (since we processed least significant digits first)
    return int(''.join(map(str, result[::-1])))

# Example usage
x = 12345678901234567890
y = 98765432109876543210

fft_result = fft_multiply(x, y)
naive_result = x * y

print("Product (FFT):", fft_result)
print("Product (Naive):", naive_result)
