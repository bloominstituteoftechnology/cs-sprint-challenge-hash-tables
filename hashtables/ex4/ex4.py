cache = {}

def has_negatives(a):
    """
    YOUR CODE HERE
    """
    # Your code here
    for num in a: 
        if num >= 0:
            cache [num] = 0
    result = []
    
    for num in a:
        if num < 0 and -num in cache:
            result.append(-num)
    return result


if __name__ == "__main__":
    print(has_negatives([-1, -2, 1, 2, 3, 4, -4]))
