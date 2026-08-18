# Topic -> loops

lines = 16
each_line_width = 32  # width of every line, i.e. the base of the staircase

# Total staircases
for line in range(lines):

    # Create staircase every 3rd line
    if line % 3 == 0:
        # 6 asterisks of tread, then the gap, then 1 asterisk of wall = 7 used
        spaces = each_line_width - 7 - ((line // 3) * 5)
        remaining_spaces = each_line_width - spaces - 7
        if line + 1 != lines:
            print(" " * spaces + "*" * 6 + " " * remaining_spaces + "*")
        else:
            print("*" * each_line_width)

    # Create staircase height
    else:
        # 1 asterisk of riser, then the gap, then 1 asterisk of wall = 2 used
        spaces = each_line_width - 7 - ((line // 3) * 5)
        remaining_spaces = each_line_width - spaces - 2
        print(" " * spaces + "*" + " " * remaining_spaces + "*")
