# Topic -> Multiply

Day = int(input("Enter the day number: "))
Month = int(input("Enter the month number: "))
Year = int(input("Enter the year number: "))

Magic = Day * Month == Year % 100
print("It is " + str(Magic) + " that the date is magical.")
