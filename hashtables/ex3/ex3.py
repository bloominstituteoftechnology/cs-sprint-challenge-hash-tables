def intersection(arrays):
    intersection_dict = {}

    for list in arrays:
        for item in list:
            if item in intersection_dict:
                intersection_dict[item] += 1
            elif item not in intersection_dict:
                intersection_dict[item] = 1

    result = []

    for key, value in intersection_dict.items():
        if value == len(arrays):
            result.append(key)

    return result


if __name__ == "__main__":
    arrays = []

    arrays.append(list(range(1000000, 2000000)) + [1, 2, 3])
    arrays.append(list(range(2000000, 3000000)) + [1, 2, 3])
    arrays.append(list(range(3000000, 4000000)) + [1, 2, 3])

    print(intersection(arrays))
