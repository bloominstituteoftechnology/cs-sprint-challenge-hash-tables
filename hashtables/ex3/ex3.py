def intersection(arrays):
    """
    YOUR CODE HERE
    """
    # store number of intersected for each number
    intersected = {}

    for array in arrays:

        for number in array:

            if number in intersected:
                intersected[number] += 1
            else:
                intersected[number] = 1
    
    # return only the items that have an occurence equal to the length of the arrays
    return [key for key, value in intersected.items() if value == len(arrays)]
   

if __name__ == "__main__":
    arrays = []

    arrays.append(list(range(1000000, 2000000)) + [1, 2, 3])
    arrays.append(list(range(2000000, 3000000)) + [1, 2, 3])
    arrays.append(list(range(3000000, 4000000)) + [1, 2, 3])

    print(intersection(arrays))
