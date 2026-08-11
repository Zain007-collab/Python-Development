# Topic -> loops, increment, decrement

num = int(input("Enter a non-negative integer: "))

binary = ""

temp = num

if temp == 0:
    binary = "0"

else:
    for i in range(32):
        remainder = temp % 2
        binary = str(remainder) + binary
        temp = temp // 2

# Make binary 32 bits
while len(binary) < 32:
    binary = "0" + binary

# Four gates
gate1 = binary[0:10]
gate2 = binary[10:20]
gate3 = binary[20:30]
gate4 = binary[30:32]

print("Gate 1 =", gate1)
print("Gate 2 =", gate2)
print("Gate 3 =", gate3)
print("Gate 4 =", gate4)


# Gate 4 decides operation


# Operation 1 -> Binary to Decimal
if gate4 == "00":

    decimal = 0
    power = 0

    for i in range(31, -1, -1):

        if binary[i] == "1":
            decimal = decimal + (2 ** power)

        power = power + 1

    print("Decimal =", decimal)

# Operation 2 -> Binary to Hexadecimal
elif gate4 == "01":

    decimal = 0
    power = 0

    for i in range(31, -1, -1):

        if binary[i] == "1":
            decimal = decimal + (2 ** power)

        power = power + 1

    hex_value = ""

    for i in range(8):

        remainder = decimal % 16

        if remainder == 10:
            hex_value = "A" + hex_value
        elif remainder == 11:
            hex_value = "B" + hex_value
        elif remainder == 12:
            hex_value = "C" + hex_value
        elif remainder == 13:
            hex_value = "D" + hex_value
        elif remainder == 14:
            hex_value = "E" + hex_value
        elif remainder == 15:
            hex_value = "F" + hex_value
        else:
            hex_value = str(remainder) + hex_value

        decimal = decimal // 16

    print("Hexadecimal =", hex_value)


# Operation 3 -> Swap Gate 1 and Gate 2
elif gate4 == "10":

    temp = gate1
    gate1 = gate2
    gate2 = temp

    print("After swapping:")

    print("Gate 1 =", gate1)
    print("Gate 2 =", gate2)
    print("Gate 3 =", gate3)
    print("Gate 4 =", gate4)


# Operation 4 -> Multiply or Divide
elif gate4 == "11":

    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))

    choice = input("Enter M for multiply or D for divide: ")

    if choice == "M":

        # Multiplication using loop
        result = 0

        for i in range(num2):
            result = result + num1

        print("Multiplication =", result)


    elif choice == "D":

        # Division using subtraction
        quotient = 0
        remainder = num1

        for i in range(num1):

            if remainder >= num2:
                remainder = remainder - num2
                quotient = quotient + 1

        print("Quotient =", quotient)
        print("Remainder =", remainder)

    else:
        print("Invalid choice.")