import re

f = open("day02.txt", "r")

limits = {
    "red": 12,
    "green": 13,
    "blue": 14
}

def solve_line(line):
    pattern = "\d+ red|\d+ blue|\d+ green"
    cubes = re.findall(pattern, line)
    for cube in cubes:
        cube = cube.split(' ')
        if int(cube[0]) > limits[cube[1]]:
            return False
    return True

sum = 0
game_counter = 0
for line in f:
    game_counter += 1
    if solve_line(line):
        sum += game_counter

print(sum)