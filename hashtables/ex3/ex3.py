def intersection(arrays):
    # Create an empty dict
    counts = {}

    # We'll use a nested for loop to go through our array
    for i in arrays:
        for j in i:
            # If j is not in our dictionary
            if j not in counts:
                # Set it to 0
                counts[j] = 0
            # We'll increment by 1
            counts[j] += 1

    result = []

    # We'll grab the key-value pairs using the items() method
        # Items() returns the dictionary's key-value pairs
    for k, v in counts.items():
        # If the value is equal to the number of items in our list
        if v == len(arrays):
            # We can append the key to our result list
            result.append(k)
    # Then we'll return the result
    return result


if __name__ == "__main__":
    arrays = []

    arrays.append(list(range(1000000, 2000000)) + [1, 2, 3])
    arrays.append(list(range(2000000, 3000000)) + [1, 2, 3])
    arrays.append(list(range(3000000, 4000000)) + [1, 2, 3])

    print(intersection(arrays))
