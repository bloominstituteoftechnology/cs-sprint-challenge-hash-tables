def has_negatives(a):
    hash_table = {}
    result = []

    for integer in a:
        abs_val = abs(integer)
        if abs_val not in hash_table:
            hash_table[abs_val] = integer
        else:
            if hash_table[abs_val] + integer == 0:
                result.append(abs_val)

    return result


if __name__ == "__main__":
    print(has_negatives([-1, -2, 1, 2, 3, 4, -4]))
