def has_negatives(a):
    """
    YOUR CODE HERE
    """
    # Your code here
    cache = {}
    result = []

    for number in a:
        #if the num is not equal to 0 then add a value count of 1
        if number is not 0:
            cache[number] = 1
        print(cache)

        #if negative number (-number) is in the cache
        if -number in cache:
            #append the corresponding "absolute" number to the result list
            #example: absolute value of -1 is 1 (so absolute value of a negative number is it's positive value)
            #The abs() method returns the absolute value of the given number
            result.append(abs(number))

    return result


if __name__ == "__main__":
    print(has_negatives([-1, -2, 1, 2, 3, 4, -4]))
