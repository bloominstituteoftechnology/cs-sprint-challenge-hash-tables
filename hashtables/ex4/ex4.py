def has_negatives(a):
    """
    YOUR CODE HERE
    """
    # Your code here
    cache = {}
    result = []

    for num in a:
        if abs(num) in cache:
            result.append(abs(num))
        else: 
            cache[abs(num)] = num
            
    return result


if __name__ == "__main__":
    print(has_negatives([-1, -2, 1, 2, 3, 4, -4]))
