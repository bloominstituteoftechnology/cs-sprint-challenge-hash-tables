def intersection(arrays):
    store = {}
    result = []
    for arr in arrays:
        for each in arr:
            if each in store:
                store[each] += 1
            else:
                store[each] = 1

            if store[each] == len(arrays):
                result.append(each)
    return result


if __name__ == "__main__":
    arrays = []

    arrays.append(list(range(1000000, 2000000)) + [1, 2, 3])
    arrays.append(list(range(2000000, 3000000)) + [1, 2, 3])
    arrays.append(list(range(3000000, 4000000)) + [1, 2, 3])

    print(intersection(arrays))
