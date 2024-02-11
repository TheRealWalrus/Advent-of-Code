import re

f = open("day02.txt", "r")

def solve_line(line):
    peaks = {
        "red": 0,
        "green": 0,
        "blue": 0
    }

    pattern = "\d+ red|\d+ blue|\d+ green"
    cubes = re.findall(pattern, line)
    for cube in cubes:
        value, key = cube.split(' ')
        value = int(value)
        peaks[key] = max(peaks[key], value)
    power = 1
    for key, value in peaks.items():
        power = power * value
    
    return power

sum = 0
for line in f:
    sum += solve_line(line)

print(sum)
