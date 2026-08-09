# Topic -> bitwise operations and bit masking

# Binary to gray code conversion

binary_number = int(input("Enter a binary number: "), 2)
gray_code = binary_number ^ (binary_number >> 1)
print("Gray code:", bin(gray_code))
