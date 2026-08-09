# Topic -> mathematical operations
import cmath

# Formula -> N = (-1/c) * (ln(1 + (b/p)*(1-(1+i)^c)) / ln(1+i))

# Constant factor c is set to 30
c = 30

# Balance amount b
b = int(input("Enter the balance amount: "))

# Monthly payment p
p = int(input("Enter the monthly payment amount: "))

# Yearly interest rate / 365 (e.g. 0.18 for 18%)
i = float(input("Enter the yearly interest rate: ")) / 365

# Calculate the time to pay off the loan using the formula
N = (-1 / c) * (cmath.log(1 + (b / p) * (1 - (1 + i) ** c)) / cmath.log(1 + i))

# Print the result
print("The time to pay off the loan is:", f"{N.real:.2f}", "months")
