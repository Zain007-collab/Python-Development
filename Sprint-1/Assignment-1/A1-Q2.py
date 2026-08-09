# Concept -> Bitwise operations

number1 = int(input("Enter the first number: "))
number2 = int(input("Enter the second number: "))
number3 = int(input("Enter the third number: "))

number1_rightmost_digit = number1 % 10
number2_rightmost_digit = number2 % 10
number3_rightmost_digit = number3 % 10

result = (
    (number1_rightmost_digit == number2_rightmost_digit)
    or (number2_rightmost_digit == number3_rightmost_digit)
    or (number1_rightmost_digit == number3_rightmost_digit)
) and (number1 > 0 and number2 > 0 and number3 > 0)

print("The Result is", result)
