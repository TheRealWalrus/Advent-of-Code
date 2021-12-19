f = open("input.txt", "r")
file_contents = f.readlines()

vertical = 0
horizontal = 0

for line in file_contents:
    direction, distance = line.split()
    distance = int(distance)
    if direction == 'forward':
        horizontal += distance
    elif direction == 'down':
        vertical += distance
    elif direction == 'up':
        vertical -= distance

print(vertical * horizontal)
