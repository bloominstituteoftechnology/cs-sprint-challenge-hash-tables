def intersection(arrays):
    """
    And we need to compute the _intersection_, that is, numbers that exist
    in all lists. Output can be in any order.
    """
    
    result = []
    cache = {}
    for arr in arrays:
        for x in arr:
            if x in cache:
                cache[x] += 1
                if cache[x] == len(arrays):
                    result.append(x)
            else:
                cache[x] = 1

    return result


if __name__ == "__main__":
    arrays = []

    arrays.append(list(range(1000000, 2000000)) + [1, 2, 3])
    arrays.append(list(range(2000000, 3000000)) + [1, 2, 3])
    arrays.append(list(range(3000000, 4000000)) + [1, 2, 3])

    print(intersection(arrays))
