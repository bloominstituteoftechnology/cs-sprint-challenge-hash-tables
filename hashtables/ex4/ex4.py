def has_negatives(a):
    """
    YOUR CODE HERE
    """
    # Your code here
    cache = {}

    for num in a:
        if num is not None:
            cache[num] = 0

    result = []
    
    for element in a:
        if element > 0:
            if element-element-element in cache:
                result.append(element)
        elif element < 0:
            if element+element+element in cache:
                result.append(element)
    for element in result:
        if element < 0:
            result.pop(element)
    return result


if __name__ == "__main__":
    print(has_negatives([-1, -2, 1, 2, 3, 4, -4]))
