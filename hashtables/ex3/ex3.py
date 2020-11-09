def intersection(arrays):
    """
    YOUR CODE HERE
    """
    cache = {}
    second_cache = {}
    result = []
    for value in arrays[0]:
        cache[value] = True
    for i in range(1,len(arrays)):
        for value in arrays[i]:
            try:
                cache[value]
            except KeyError:
                cache[value] = False
            second_cache[value] = True
        for key in cache.keys():
            if cache[key]:
                try:
                    second_cache[key]
                except KeyError:
                    cache[key] = False
    for k,v in cache.items():
        if v:
            result.append(k)
    return result


if __name__ == "__main__":
    arrays = []

    arrays.append(list(range(1000000, 2000000)) + [1, 2, 3])
    arrays.append(list(range(2000000, 3000000)) + [1, 2, 3])
    arrays.append(list(range(3000000, 4000000)) + [1, 2, 3])

    print(intersection(arrays))
