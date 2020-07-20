def intersection(arrays):
    # Create a cache
    cache = {}

    # Traverse the arr of arrays
    for arr in arrays:
        # Traverse the arr
        for val in arr:
            # If val in cache inc count val
            if val in cache:
                cache[val] += 1
            # Otherwise, add it to the cache
            else:
                cache[val] = 1
    # Return a list of all arr items(keys in the cache) with a value equal to the number of arrays
    # in the original input arr
    return [key for key in cache.keys() if cache[key] == len(arrays)]


if __name__ == "__main__":
    arrays = []

    arrays.append(list(range(1000000, 2000000)) + [1, 2, 3])
    arrays.append(list(range(2000000, 3000000)) + [1, 2, 3])
    arrays.append(list(range(3000000, 4000000)) + [1, 2, 3])

    print(intersection(arrays))
