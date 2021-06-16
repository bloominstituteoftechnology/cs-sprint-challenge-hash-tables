def has_negatives(a):
    """
    YOUR CODE HERE
    """
    # Your code here
    my_cache = {}
    result = []

    # will loop through the list and will cache them 
    # will also check to see if the neg value of that is in the list if it is 
    # then will add it to the list
    for theValue in a:
        if -theValue in my_cache:
            # need to put the value in the result array
            if theValue > -theValue:
                result.append(theValue)
            else:
                result.append(-theValue)
        else:
            # putting the value in the cache
            my_cache[theValue] = ""
    return result


if __name__ == "__main__":
    print(has_negatives([-1, -2, 1, 2, 3, 4, -4]))
