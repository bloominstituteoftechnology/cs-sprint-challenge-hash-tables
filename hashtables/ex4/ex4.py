def has_negatives(a):
    """
    YOUR CODE HERE
    """
    # Your code here
    storage = dict()
    result = []

    for num in a:
        storage[num] = 0

        if num != 0 and -num in storage:
            result.append(abs(num))       

    return result


if __name__ == "__main__":
    print(has_negatives([-1, -2, 1, 2, 3, 4, -4]))
