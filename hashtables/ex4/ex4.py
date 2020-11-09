def has_negatives(a):
    result = []
    negatives = {}
    a.sort()
    for num in a:
        if num < 0:
            negatives[-num] = num
        if num > 0 and num in negatives:
            result.append(num)
    return result


def has_negatives(arr):
    store = {}
    result = []
    for each in arr:
        if (each * -1) in store:
            result.append(abs(each))
        else:
            store[each] = each
    return result


if __name__ == "__main__":
    print(has_negatives([-1, -2, 1, 2, 3, 4, -4]))
