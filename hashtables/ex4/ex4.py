def has_negatives(a):
    """
    YOUR CODE HERE
    """
    # Your code here
    cache = {}
    result = []

    for num in a:
        # see if there is another instance of the number in our array positive or negative
        if cache.get(abs(num)):
            if (cache.get(abs(num)) + num) == 0:
                result.append(abs(num))
        else:
            cache[abs(num)] = num 

    return result


if __name__ == "__main__":
    print(has_negatives([-1, -2, 1, 2, 3, 4, -4]))
