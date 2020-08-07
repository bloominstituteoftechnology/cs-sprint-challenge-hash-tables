def has_negatives(a):
    """
    YOUR CODE HERE
    """
    # Your code here
    numbs = {i:i for i in a}
    result = []
    for key in numbs.keys():
        if key > 0 and numbs.get(key * -1):
            result.append(key)
    return result


if __name__ == "__main__":
    print(has_negatives([-1, -2, 1, 2, 3, 4, -4]))
