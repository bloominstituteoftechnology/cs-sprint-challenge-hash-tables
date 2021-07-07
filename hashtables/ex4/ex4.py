def has_negatives(a):
    """
    YOUR CODE HERE
    """
    # Your code here
    
    # empty list
    result = []
    # empty htable
    cache = {}

    for num in a:
        # add intgs to htable
        cache[num] = 1
    for num in a:
        # if intg * -1 is in the htable and positive int exsists, add intgs to result array
        if (num*-1) in cache and num > 0:
            result.append(num)

    return result


if __name__ == "__main__":
    print(has_negatives([-1, -2, 1, 2, 3, 4, -4]))
