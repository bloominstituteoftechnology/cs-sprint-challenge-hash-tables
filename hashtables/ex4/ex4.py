def has_negatives(a):
    negatives_by_num = {}

    for num in a:
        negatives_by_num[num] = -num

    result = []

    for num in negatives_by_num.keys():
        if num > 0 and negatives_by_num[num] in negatives_by_num:
            result.append(num)

    return result


if __name__ == "__main__":
    print(has_negatives([-1, -2, 1, 2, 3, 4, -4]))
