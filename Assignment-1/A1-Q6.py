# Topic -> bit masking and operations

# Finding the key for the 32 bit number
# Format: | Constant_8_bits | Gate_3 | Gate_2 | Gate_1 | -> each gate is 8 bits
# Formula: constant_8_bits = gate_1 ^ gate_2 ^ gate_3 ^ key

number = int(input("Enter a number: "))
gate_1 = number & 0xFF
gate_2 = (number >> 8) & 0xFF
gate_3 = (number >> 16) & 0xFF
constant_8_bits = number >> 24
print("Gate 1:", bin(gate_1))
print("Gate 2:", bin(gate_2))
print("Gate 3:", bin(gate_3))
print("Constant 8 bits:", bin(constant_8_bits))

key = (gate_1) ^ (gate_2) ^ (gate_3) ^ (constant_8_bits)

print("The key is:", bin(key))
