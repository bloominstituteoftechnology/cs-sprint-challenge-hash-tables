def has_negatives(a):
    """
    YOUR CODE HERE
    """
    # Your code here

    cache = {}
    result = []

    for number in a:

        if number is not 0:
            cache[number] = 1
        print(cache)

    
        if -number in cache:

            result.append(abs(number))


    return result


if __name__ == "__main__":
    print(has_negatives([-1, -2, 1, 2, 3, 4, -4]))
