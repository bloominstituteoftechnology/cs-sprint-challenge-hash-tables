def has_negatives(a):
    result = []
    has_neg_dict = {}

    for num in a:
        has_neg_dict[num] = num

        if num != 0 and -num in has_neg_dict:
            result.append(abs(num))

    return result


if __name__ == "__main__":
    print(has_negatives([-1, -2, 1, 2, 3, 4, -4]))
