def intersection(arrays):
    # Initialize hash table for storage
    dictionary = {}
    result = []

    # Loop through the list of arrays
    for array in arrays:
        # Loop through each item in the array
        for item in array:
            # If this value is in the dictionary, append the count
            if item in dictionary:
                dictionary[item] +=1
            # Item is not in the dictionary, initialize a count
            else:
                dictionary[item] = 1

    # Loop through the items in the dictionary

    for val in dictionary:
        # print(f'value:{dictionary[val]}, array length: {len(arrays)}')

        # If the item count is equal to the number of lists
        # Then that item must exist in all the sub-arrays
        if dictionary[val] == len(arrays):
            # Add the value to the result
            result.append(val)

    return result


if __name__ == "__main__":
    arrays = []

    arrays.append(list(range(1000000, 2000000)) + [1, 2, 3])
    arrays.append(list(range(2000000, 3000000)) + [1, 2, 3])
    arrays.append(list(range(3000000, 4000000)) + [1, 2, 3])

    print(intersection(arrays))
