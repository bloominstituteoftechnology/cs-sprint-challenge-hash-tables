def has_negatives(a):
    """
    YOUR CODE HERE
    """
    # Your code here
    result = []
    hash = set(a)
    for x in hash:
        if x > 0 and (x * -1 in hash):
            result.append(x)
            
    if len(result) < 100:
        print('RESULT', result)
    return result


if __name__ == "__main__":
    print(has_negatives([-1, -2, 1, 2, 3, 4, -4]))
