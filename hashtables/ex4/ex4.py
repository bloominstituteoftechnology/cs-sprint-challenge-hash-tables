def has_negatives(a):
    ht = {}
    for num in a:
        if num > 0:
            ht[num] = True

    result = []
    for num in a:
        if num < 0:
            num = abs(num)
            if num in ht:
                result.append(num)

    return result


if __name__ == "__main__":
    print(has_negatives([-1, -2, 1, 2, 3, 4, -4]))
