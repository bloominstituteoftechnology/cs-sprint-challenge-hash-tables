def has_negatives(a):
    """
    YOUR CODE HERE
    """
    # Your code here

    hashtable = {}

    for i in a:
        if i < 0:
            hashtable[abs(i)] = i

    result = [i for i in a if i in hashtable]

    # for i in a:
    #     if i in hashtable:
    #         result.append(i)

    return result


if __name__ == "__main__":
    print(has_negatives([-1, -2, 1, 2, 3, 4, -4]))
