# Topic -> condition

square_1 = int(input("Enter the number from 1 to 36: "))
square_2 = int(input("Enter the number from 1 to 36: "))

# Green -> 1,6,7,12,17,28,33
green = (
    (square_1 == 1)
    | (square_1 == 6)
    | (square_1 == 7)
    | (square_1 == 12)
    | (square_1 == 17)
    | (square_1 == 28)
    | (square_1 == 33)
) & (
    (square_2 == 1)
    | (square_2 == 6)
    | (square_2 == 7)
    | (square_2 == 12)
    | (square_2 == 17)
    | (square_2 == 28)
    | (square_2 == 33)
)

# Red -> 2,11,13,18,19,24,29,32
red = (
    (square_1 == 2)
    | (square_1 == 11)
    | (square_1 == 13)
    | (square_1 == 18)
    | (square_1 == 19)
    | (square_1 == 24)
    | (square_1 == 29)
    | (square_1 == 32)
) & (
    (square_2 == 2)
    | (square_2 == 11)
    | (square_2 == 13)
    | (square_2 == 18)
    | (square_2 == 19)
    | (square_2 == 24)
    | (square_2 == 29)
    | (square_2 == 32)
)

# Blue -> 3,10,14,23,25,30,31,36
blue = (
    (square_1 == 3)
    | (square_1 == 10)
    | (square_1 == 14)
    | (square_1 == 23)
    | (square_1 == 25)
    | (square_1 == 30)
    | (square_1 == 31)
    | (square_1 == 36)
) & (
    (square_2 == 3)
    | (square_2 == 10)
    | (square_2 == 14)
    | (square_2 == 23)
    | (square_2 == 25)
    | (square_2 == 30)
    | (square_2 == 31)
    | (square_2 == 36)
)

# Orange -> 4,9,15,22,26,35
orange = (
    (square_1 == 4)
    | (square_1 == 9)
    | (square_1 == 15)
    | (square_1 == 22)
    | (square_1 == 26)
    | (square_1 == 35)
) & (
    (square_2 == 4)
    | (square_2 == 9)
    | (square_2 == 15)
    | (square_2 == 22)
    | (square_2 == 26)
    | (square_2 == 35)
)

# Cyan -> 5,8,16,21,27,34
cyan = (
    (square_1 == 5)
    | (square_1 == 8)
    | (square_1 == 16)
    | (square_1 == 21)
    | (square_1 == 27)
    | (square_1 == 34)
) & (
    (square_2 == 5)
    | (square_2 == 8)
    | (square_2 == 16)
    | (square_2 == 21)
    | (square_2 == 27)
    | (square_2 == 34)
)

same_color = green | red | blue | orange | cyan

print("Same Color:", same_color)
