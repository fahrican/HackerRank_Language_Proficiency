"""
Designer Door Mat
"""


def print_dashes_or_parameter(logo_or_pattern):
    number_of_dashes = columns - len(logo_or_pattern)
    half_of_number_of_dashes = (number_of_dashes / 2) - 1
    for column in range(columns):
        if column < half_of_number_of_dashes:
            print("-", end="")
        elif column == (half_of_number_of_dashes + 1):
            print(logo_or_pattern, end="")
        elif column > number_of_dashes:
            break
        else:
            print("-", end="")


def generate_designer_door_mat(rows, columns):
    row_for_welcome = int((rows / 2))
    design_pattern = ".|."
    welcome_logo = "WELCOME"
    for row in range(rows):
        if row < row_for_welcome:
            print_dashes_or_parameter(design_pattern)
            if row < (row_for_welcome - 1):
                design_pattern = ".|." + design_pattern + ".|."
        elif row == row_for_welcome:
            print_dashes_or_parameter(welcome_logo)
        else:
            print_dashes_or_parameter(design_pattern)
            design_pattern = design_pattern[3:]
            design_pattern = design_pattern[:-3]
        print()


if __name__ == '__main__':
    row_and_column = input().split(" ")
    rows = int(row_and_column[0])
    columns = int(row_and_column[1])
    generate_designer_door_mat(rows, columns)
