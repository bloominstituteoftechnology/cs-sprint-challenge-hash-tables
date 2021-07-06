
result1 = {}
def intersection(arrays):
    result = []
    for array in arrays:
        for arr in array:
            result1[arr] = arr
            if result1[arr] == arr:
                result.append(arr)

    return result


if __name__ == "__main__":
    arrays = []

    arrays.append(list(range(1000000, 2000000)) + [1, 2, 3])
    arrays.append(list(range(2000000, 3000000)) + [1, 2, 3])
    arrays.append(list(range(3000000, 4000000)) + [1, 2, 3])

    print(intersection(arrays))
