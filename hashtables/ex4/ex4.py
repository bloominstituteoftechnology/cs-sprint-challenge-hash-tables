def has_negatives(a):
    """
    YOUR CODE HERE
    """
    # Your code here
    result = []
    cache = {}
    for num in a:
        if num != 0:
            cache[num] = num

        if(-num) in cache:
            result.append(abs(num)) 
            print(result)
    return result


if __name__ == "__main__":
    print(has_negatives([-1, -2, 1, 2, 3, 4, -4]))
