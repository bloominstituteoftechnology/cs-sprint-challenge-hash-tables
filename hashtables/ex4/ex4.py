def has_negatives(array):
    cache = {}
    result = []
    for item in array:
        cache[item] = item
        if -item in cache and item != 0:
            result.append(abs(item))
    return result


if __name__ == "__main__":
    print(has_negatives([-1, -2, 1, 2, 3, 4, -4]))
