def has_negatives(a):
    """
    YOUR CODE HERE
    """
    # Your code here
    s = dict()
    result = []
    for i in a:
        s[i] = 1
        if i != 0 and -i in s:
            result.append(abs(i))

    return result


if __name__ == "__main__":
    print(has_negatives([-1, -2, 1, 2, 3, 4, -4]))
