f = open("input.txt", "r")
file_contents = f.readlines()

vertical = 0
horizontal = 0
aim = 0

for line in file_contents:
    direction, value = line.split()
    value = int(value)
    if direction == 'forward':
        horizontal += value
        vertical += aim * value
    elif direction == 'down':
        aim += value
    elif direction == 'up':
        aim -= value


print(vertical * horizontal)
