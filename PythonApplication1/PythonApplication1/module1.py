def print_string_backwards(to_reverse):
    list = []
    count = 1
    for word in range(0, len(to_reverse)):
        list.append(to_reverse[len(to_reverse) - count])
        count += 1
    list = ''.join(list)

    return list

print(print_string_backwards("Taking my Test!"))