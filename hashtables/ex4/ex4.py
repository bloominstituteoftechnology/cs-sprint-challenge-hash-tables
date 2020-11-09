def has_negatives(a):
    cache = {}
    a.sort()
    result = []
    for value in a:
        if value < 0:
            cache[abs(value)] = True
    for value in a:
        if value in cache:
            result.append(value)
    return result


if __name__ == "__main__":
    print(has_negatives([-1, -2, 1, 2, 3, 4, -4]))
