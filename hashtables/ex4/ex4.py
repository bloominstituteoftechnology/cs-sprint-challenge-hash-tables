def has_negatives(a):
    """
    YOUR CODE HERE
    """
    # Your code here
    table = {}

    for ele in a:
        table[abs(ele)] = table.get(abs(ele), 0) + ele

    result = []
    for key in table:
        if table[key] == 0:
            result.append(key)

    return result


if __name__ == "__main__":
    print(has_negatives([-1, -2, 1, 2, 3, 4, -4]))
