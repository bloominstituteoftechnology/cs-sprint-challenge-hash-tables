def intersection(arrays):
    """
    YOUR CODE HERE
    """
    # INFO: I CAN'T BELIEVE I PASSED THIS IN 10 MINUTES
    
    dict = {}
    results = []
    # for loop through first list
        # for loop through second list
    for outer in arrays:
        for inner in outer:
            if inner in dict:
                # If seen more than once increment
                dict[inner] += 1
            else:
                # I suppose I could of set it two one and changed the if clause further down
                # if only seen once st it two 0
                dict[inner] = 0
    for k, v in dict.items():
        # if I saw the dictionary key more than one put it into array
        if v >= 1:
            results.append(k)
    # Your code here

    return results


if __name__ == "__main__":
    arrays = []

    arrays.append(list([1,2,3]))
    arrays.append(list([1]))


    print(intersection(arrays))
