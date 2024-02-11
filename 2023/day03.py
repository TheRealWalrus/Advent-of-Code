f = open("day03.txt", "r")

file_contents = f.read().splitlines()

def is_part_digit(row, column, board):
    for x in range(-1, 2):
        for y in range (-1, 2):
            try:
                char = board[row + y][column + x]
                if not char.isnumeric() and char != '.':
                    return True
            except:
                pass
    return False

print(is_part_digit(0, 2, file_contents))

sum = 0

for y in range(0, len(file_contents)):
    row = file_contents[y]
    num = ""
    is_part_number = False
    for x in range(0, len(row)):
        char = file_contents[y][x]
        if char.isnumeric():
            num += char
            is_part_number = is_part_number or is_part_digit(y, x, file_contents)
        else:
            if is_part_number:
                sum += int(num)
            num = ""
            is_part_number = False
    if is_part_number:
        sum += int(num)
    num = ""
    is_part_number = False

print(sum)
