def intersection(arrays):
    
    map = {}
    for a in arrays:
        for n in a:
            value = map.get(n)
            if value is None:
                map[n] = 1
            else:
                map[n] = value+1
    count = len(arrays)
    result = []
    for n in map.keys():
        value = map[n]
        if value == count:
            result.append(n)

    # print(result)

    return result


if __name__ == "__main__":
    arrays = []

    arrays.append(list(range(1000000, 2000000)) + [1, 2, 3])
    arrays.append(list(range(2000000, 3000000)) + [1, 2, 3])
    arrays.append(list(range(3000000, 4000000)) + [1, 2, 3])

    print(intersection(arrays))
