def has_negatives(a):
    """
    YOUR CODE HERE
    """
    # Your code here
    storage = {} # create an empty dictionary
    result = [] # instantiate list for numbers that meet the criteria

    for number in a:   
        if (-number) in storage: # looks for opposites of the numbers in storage
            result.append(abs(number)) # appends the absolute value of the number into storage
        else:
            storage[number] = 1  
    return result


if __name__ == "__main__":
    print(has_negatives([-1, -2, 1, 2, 3, 4, -4]))
