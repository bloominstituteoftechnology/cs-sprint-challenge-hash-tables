def intersection(arrays):
    """
    YOUR CODE HERE
    """
    # Your code here
    dict = {}
    results = []

    # nested for loop to go through the list of arrays
    for array in arrays:
        for i in array:
            dict[i] = dict[i] + 1 if i in dict else 1

    for i in dict:
        if dict[i] > 1:
            results.append(i)

    return results


if __name__ == "__main__":
    arrays = []

    arrays.append(list(range(1000000, 2000000)) + [1, 2, 3])
    arrays.append(list(range(2000000, 3000000)) + [1, 2, 3])
    arrays.append(list(range(3000000, 4000000)) + [1, 2, 3])

    print(intersection(arrays))
