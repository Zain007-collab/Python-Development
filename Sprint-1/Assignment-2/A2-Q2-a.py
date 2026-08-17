# Topic -> loops

lines = 19
each_line_elements = 30

# Total staircases
for line in range(lines):

    # Create staircase every 3rd line
    if line % 3 == 0:
        spaces = each_line_elements - ((line // 3) * 5)
        remaining_spaces = each_line_elements - spaces
        if line + 1 != lines:
            print(" " * spaces + "*" * 6 + " " * remaining_spaces + "*")
        else:
            print("*" * spaces + "*" * 6 + "*" * remaining_spaces + "*")

    # Create staircase height
    else:
        spaces = each_line_elements - ((line // 3) * 5)
        remaining_spaces = each_line_elements - spaces + 5
        print(" " * spaces + "*" + " " * remaining_spaces + "*")
