def intersection(arrays):
    """
    YOUR CODE HERE
    """
    # Your code here
    d = {}

    for index, l in enumerate(arrays):
        for num in l:
            if num not in d:
                # set a key for that number with it's value as an array containing the index of list it appeared in 
                d[num] = [index]
            else:
                # add the current list index to the entry for this num 
                d[num].append(index)

    result = []

    for key in d:
        # might need to change to tuple here 
    
        if len(d[key]) == len(arrays):
            result.append(key)

    return result


if __name__ == "__main__":
    arrays = []

    arrays.append(list(range(1000000, 2000000)) + [1, 2, 3])
    arrays.append(list(range(2000000, 3000000)) + [1, 2, 3])
    arrays.append(list(range(3000000, 4000000)) + [1, 2, 3])

    print(intersection(arrays))
