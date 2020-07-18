def has_negatives(a):
    """
    YOUR CODE HERE
    """
    # Your code here
    storage = {}
    result = []

    for number in a:
        storage[number] = 1  # adds numbers to storage
        if (-1*number) in storage: # looks for opposite of the numbers in storage
            result.append(abs(number)) # appends the absolute value of the number into storage


    return result


if __name__ == "__main__":
    print(has_negatives([-1, -2, 1, 2, 3, 4, -4]))
