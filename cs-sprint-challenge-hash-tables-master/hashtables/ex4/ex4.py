def has_negatives(a):
    """
    YOUR CODE HERE
    """
    # Your code here
    cache = {}
    result = []

    for i in a:

        cache[i] = i
        
        if i and -i in cache:
            if i > 0:
                result.append(i)
            else:
                result.append(-i)

    return result

if __name__ == "__main__":
    print(has_negatives([-1, -2, 1, 2, 3, 4, -4]))