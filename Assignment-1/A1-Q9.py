# Topic -> max

number_1 = int(input("Enter the first number: "))
number_2 = int(input("Enter the second number: "))
number_3 = int(input("Enter the third number: "))
number_4 = int(input("Enter the fourth number: "))

maximum = max(number_1, number_2, number_3, number_4)
second_maximum = min(
    max(number_1, number_2, number_3),
    max(number_1, number_2, number_4),
    max(number_1, number_3, number_4),
    max(number_2, number_3, number_4),
)

print("The maximum number is: ", maximum)
print("The second maximum number is: ", second_maximum)
