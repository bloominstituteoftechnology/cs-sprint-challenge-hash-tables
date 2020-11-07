def has_negatives(a):
    store = {}
    result = {}
    for num in a:
        store[num] = num

    for key, value in store.items():
        if key * -1 in store:
            result[abs(key)] = 1

    if result == {}:
        return []

    result_array = []
    for item in result.items():
        if item[0] != 0:
            result_array.append(item[0])

    return result_array


if __name__ == "__main__":
    print(has_negatives([-1, -2, 1, 2, 3, 4, -4]))
