def intersection(arrays):
    """
    YOUR CODE HERE
    """
    result = []
    dictionary = dict()

    for array in arrays: 
        for i in array:
              
            if i in dictionary:
                dictionary[i] += 1
            else:
                dictionary[i] = 1

    for i in dictionary.items():
        if i[1] == len(arrays):
            result.append(i[0])
    return result


if __name__ == "__main__":
    arrays = []

    arrays.append(list(range(1000000, 2000000)) + [1, 2, 3])
    arrays.append(list(range(2000000, 3000000)) + [1, 2, 3])
    arrays.append(list(range(3000000, 4000000)) + [1, 2, 3])

    print(intersection(arrays))
