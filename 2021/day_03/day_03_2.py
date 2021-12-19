def solve(data):
    o2_array = data.copy()
    co2_array = data.copy()

    i = 0
    while len(o2_array) > 1:
        o2_count = 0
        for rating in o2_array:
            if rating[i] == '1':
                o2_count += 1
        o2_dominant_digit = '1' if o2_count >= len(o2_array) / 2 else '0'
        o2_array = [rating for rating in o2_array if rating[i] == o2_dominant_digit]
        i += 1

    i = 0
    while len(co2_array) > 1:
        co2_count = 0
        for rating in co2_array:
            if rating[i] == '1':
                co2_count += 1
        co2_dominant_digit = '0' if co2_count >= len(co2_array) / 2 else '1'
        co2_array = [rating for rating in co2_array if rating[i] == co2_dominant_digit]
        i += 1

    return int(o2_array[0], 2) * int(co2_array[0], 2)


if __name__ == "__main__":
    f = open("input.txt", "r")
    file_contents = f.read().splitlines()
    print(solve(file_contents))
