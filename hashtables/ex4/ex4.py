def has_negatives(a):
    """
    YOUR CODE HERE
    """
    # Your code here
    result = []
    cache = {}
    for i in a:
        if i > 0:
            cache[i] = i
    for i in a:
        p_num = i * -1
        if p_num in cache:
            result.append(p_num)
    return result


if __name__ == "__main__":
    print(has_negatives([-1, -2, 1, 2, 3, 4, -4]))
