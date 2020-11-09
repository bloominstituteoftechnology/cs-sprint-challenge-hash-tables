def has_negatives(a):
    """
    YOUR CODE HERE
    """
    # Your code here

    dict = {}
    result = []

    # Let's do it so the abs value of a number increments how many times it's found

    for i in a:
        if not abs(i) in dict:
            dict[abs(i)] = 1
        else:
            dict[abs(i)] += 1
            result.append(abs(i))
        # print(dict)
    # print(result)

    return result


if __name__ == "__main__":
    print(has_negatives([-1, -2, 1, 2, 3, 4, -4]))
