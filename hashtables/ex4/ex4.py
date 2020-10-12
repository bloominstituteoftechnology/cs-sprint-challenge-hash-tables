def has_negatives(a):
    cache = {}
    for number in a:
        if number not in cache:
            cache[number] = 0
    result = []
    for item in a:
        if item > 0:
            if item-item-item in cache:
                result.append(item)
        elif item < 0:
            if item+item+item in cache:
                result.append(item)
    for item in result:
        if item < 0:
            result.pop(item)
    return result


if __name__ == "__main__":
    print(has_negatives([-1, -2, 1, 2, 3, 4, -4]))
