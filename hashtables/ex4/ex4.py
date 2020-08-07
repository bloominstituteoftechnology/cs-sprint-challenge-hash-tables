def has_negatives(arr):

    ht = {}
    result = []

    for num in arr:
        negative = num * -1

        if negative in ht:
            result.append(max(num, negative))

        else:
            ht[num] = negative

    return result


if __name__ == "__main__":
    print(has_negatives([-1, 1, -1, -4, -2, 1, 2, 3, 4, -4, -4, -7, 7]))
