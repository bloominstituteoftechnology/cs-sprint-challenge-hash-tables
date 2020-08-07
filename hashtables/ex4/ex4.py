def has_negatives(a):
    """
    YOUR CODE HERE
    """
    # Your code here

    hash_table = {}
    result = []

    for x in a:
        if x != 0:
            hash_table[x] = 1
            if -x in hash_table:
                result.append(abs(x))
    return result


if __name__ == "__main__":
    print(has_negatives([-1, -2, 1, 2, 3, 4, -4]))
