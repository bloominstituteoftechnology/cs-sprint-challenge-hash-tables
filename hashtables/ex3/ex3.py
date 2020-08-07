def intersection(arrays):

    # build hashtable and result arr
    catalog = {}
    result = []

    # loop to get each value from each inner array (needs a nested for loop)
    for array in arrays:
        for num in array:
            if num in catalog:
                catalog[num] += 1
            else:
                catalog[num] = 1

    # stash any key that has a value greater than 2 in the result arr
    for key, val in catalog.items():
        if val > 1:
            result.append(key)

    return result


if __name__ == "__main__":
    arrays = []

    arrays.append(list(range(1000000, 2000000)) + [1, 2, 3])
    arrays.append(list(range(2000000, 3000000)) + [1, 2, 3])
    arrays.append(list(range(3000000, 4000000)) + [1, 2, 3])

    print(intersection(arrays))
