number_of_gallons = int(input("Enter the number of gallons: "))

bill = 0

# First 100 gallons @ $0.45
bill += min(number_of_gallons, 100) * 0.45

# Next 250 gallons @ $0.85
bill += max(min(number_of_gallons - 100, 250), 0) * 0.85

# Next 250 gallons @ $1.45
bill += max(min(number_of_gallons - 350, 250), 0) * 1.45

# Above 600 gallons @ $2.60
bill += max(number_of_gallons - 600, 0) * 2.60

# 14% service charge
bill = max(bill * 1.14, 0)

print(f"The water consumption bill is {bill:.2f}")
