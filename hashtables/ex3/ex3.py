def intersection(arrays):
    counter = {}

    for array in arrays:
        for small_array in array:
            if small_array in counter:
                counter[small_array] += 1
            else:
                counter[small_array] = 1
    return [inter for inter in counter.keys() if counter[inter] == len(arrays)]


if __name__ == "__main__":
    arrays = []

    arrays.append(list(range(1000000, 2000000)) + [1, 2, 3])
    arrays.append(list(range(2000000, 3000000)) + [1, 2, 3])
    arrays.append(list(range(3000000, 4000000)) + [1, 2, 3])

    print(intersection(arrays))
