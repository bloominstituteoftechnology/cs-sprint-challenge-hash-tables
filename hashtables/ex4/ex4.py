def has_negatives(a):
    """
    YOUR CODE HERE
    """
    # Your code here
    result = []
    for num_1 in a:
        for num_2 in a:
            if num_1 == num_2 * -1:
                result.append(num_1)
    return result


if __name__ == "__main__":
    print(has_negatives([-1, -2, 1, 2, 3, 4, -4]))
