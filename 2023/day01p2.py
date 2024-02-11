import re

f = open("day01p2.txt", "r")

digits = {
    "one": "1",
    "two": "2",
    "three": "3",
    "four": "4",
    "five": "5",
    "six": "6",
    "seven": "7",
    "eight": "8",
    "nine": "9"
}

search_term = "\\d"

for key, value in digits.items():
    search_term += f"|{key}"

print(search_term)

def numberify(string):
    if string.isnumeric():
        return string
    return digits[string]

def solve(line):
    matches = re.finditer(f'(?=({search_term}))', line)
    numbers = [numberify(match.group(1)) for match in matches]
    return int(numbers[0] + numbers[-1])

def solve_without_overlap(line):
    matches = re.findall(search_term, line)
    numbers = [numberify(match) for match in matches]
    return int(numbers[0] + numbers[-1])

sum = 0

for line in f:
    num = solve(line)
    num_without_overlap = solve_without_overlap(line)
    if (num != num_without_overlap):
        print(num)
        print(num_without_overlap)
        print(line)
    sum += num

print(sum)
