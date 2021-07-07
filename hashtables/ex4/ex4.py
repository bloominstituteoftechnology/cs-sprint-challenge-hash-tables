def has_negatives(a):
    """
    YOUR CODE HERE
    """
    # Your code here
    negative = {}
    positive = {}
    result = []
    for num in a:
        if num >= 0:
            positive[num] = None
        else:
            negative[num] = None
    for key, _ in negative.items():
        if abs(key) in positive:
            result.append(abs(key))
    return result


if __name__ == "__main__":
    print(has_negatives([-1, -2, 1, 2, 3, 4, -4]))
