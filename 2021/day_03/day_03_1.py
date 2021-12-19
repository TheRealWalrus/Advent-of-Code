def solve(data):
    num_length = len(data[0])
    counters = [0] * num_length
    for num in data:
        for i, digit in enumerate(num):
            if digit == "1":
                counters[i] += 1

    gamma_bin = ""
    for counter in counters:
        if counter > len(data) / 2:
            gamma_bin += "1"
        else:
            gamma_bin += "0"

    gamma = int(gamma_bin, 2)
    epsilon = 2 ** num_length - gamma - 1

    return gamma * epsilon


if __name__ == "__main__":
    f = open("input.txt", "r")
    file_contents = f.read().splitlines()
    print(solve(file_contents))
