def has_negatives(a):
    """
    YOUR CODE HERE
    """
    # Your code here
    # dict to hold all numbers in `a`
    storage = {}
    # arr to return matches
    result = []
    # loop through each num in arr
    for num in a:
        # print(storage, result)
        # if the num has a corresponding number in the dict
        if storage.get(
                abs(num)):  # The abs() function is used to return the absolute value of a number.get method returns the value for the given key
            # check if they add to 0
            if (storage.get(abs(num)) + num) == 0:
                # if it does, add to match list
                result.append(abs(num))
            pass
        else:
            # if no value is found, pass num as new key along with it's value
            storage[abs(num)] = num

    return result


if __name__ == "__main__":
    print(has_negatives([-1, -2, 1, 2, 3, 4, -4]))
