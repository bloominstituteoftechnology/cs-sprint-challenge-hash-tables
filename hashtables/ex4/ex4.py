def has_negatives(a):
    """
    YOUR CODE HERE
    """
    # Your code here
    cache = {i: False for i in a}
    result = []
    for i in a:
        if i != 0 and -i in cache and not cache[i] and not cache[-i]:
            cache[-i] = True
            cache[i] = True
            result.append(abs(i))
    return result


if __name__ == "__main__":
    print(has_negatives([-1, -2, 1, 2, 3, 4, -4]))
