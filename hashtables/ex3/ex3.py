def intersection(arrays):
    """
    YOUR CODE HERE
    """
    # Your code here

    #set hash table and set results array
    hash_table = {}
    results = []

    ## nested for loop to go through the list of arrays
    for array in arrays:
        for i in array:
            key = i
            #if the key is not in the hash table - add it
            if key not in hash_table:
                hash_table[key] = 1
            else:
                #if key is in the hash table - add one
                hash_table[key] += 1

    #iterate over the hash table after it has been populated
    for i in hash_table:
        if hash_table[i] > 1:
            #if the hash table has more than one item in it - append it to the results table
            results.append(i)
    return results


if __name__ == "__main__":
    arrays = []

    arrays.append(list(range(1000000, 2000000)) + [1, 2, 3])
    arrays.append(list(range(2000000, 3000000)) + [1, 2, 3])
    arrays.append(list(range(3000000, 4000000)) + [1, 2, 3])

    print(intersection(arrays))