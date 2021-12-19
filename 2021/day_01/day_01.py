f = open("input.txt", "r")
file_contents = f.readlines()
measurements = [int(num) for num in file_contents]
counter = 0
print(len(measurements))
for i in range(0, len(measurements) - 3):
    first_window = measurements[i] + measurements[i + 1] + measurements[i + 2]
    second_window = measurements[i + 1] + measurements[i + 2] + measurements[i + 3]
    if int(first_window < second_window):
        counter = counter + 1

print(counter)
