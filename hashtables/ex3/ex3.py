def intersection(arrays):
    """
    YOUR CODE HERE

    put the first array into has table with the value as key and index as value
    loop thru each item in 2nd and on to check intersection elements
    if no insection, remove item in the hash table

    """
    # Your code here
    hash = {}
    hash2 = {}
    for i in range(len(arrays[0])):
        hash[arrays[0][i]] = i

    for key in hash:
        if key in arrays[1]:
            hash2[key] = hash[key]
    print(hash2)
    
    for i in range(2, len(arrays)):
        for key in hash2:
            if key not in arrays[i]:
                hash2[key] = None

    list1 = [key for key in hash2 if hash2[key] != None]       
    result = list1

    return result


if __name__ == "__main__":
    arrays = []

    arrays.append(list(range(1000000, 2000000)) + [1, 2, 3])
    arrays.append(list(range(2000000, 3000000)) + [1, 2, 3])
    arrays.append(list(range(3000000, 4000000)) + [1, 2, 3])

    print(intersection(arrays))

    # arrays = [
    # [1, 2, 3, 4, 5],
    # [12, 7, 2, 9, 1],
    # [99, 2, 7, 1,]
    # ]
    # print(intersection(arrays))