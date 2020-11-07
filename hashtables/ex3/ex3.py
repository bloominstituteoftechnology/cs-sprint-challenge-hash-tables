def intersection(arrays):
    """
    YOUR CODE HERE
    """
    # Your code here
    dictionary = {}
    result = []

    for array in arrays:
        for element in array:
            if element not in dictionary:
                dictionary[element] = 1
            else:
                dictionary[element] += 1

            if dictionary[element] == len(arrays):
                result.append(element)

    return result

if __name__ == "__main__":
    arrays = []

    arrays.append(list(range(1000000, 2000000)) + [1, 2, 3])
    arrays.append(list(range(2000000, 3000000)) + [1, 2, 3])
    arrays.append(list(range(3000000, 4000000)) + [1, 2, 3])

    print(intersection(arrays))
