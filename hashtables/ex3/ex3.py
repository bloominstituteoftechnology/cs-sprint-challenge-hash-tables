def intersection(arrays):
    """
    YOUR CODE HERE
    """
    # Your code here
    cache = {}

    total_array_list = len(arrays) 

    for list in arrays:
        for element in list:
            if element in cache:
                cache[element] += 1 #counter for repeating element in all list
            else:
                cache[element] = 1
    
    result = []
    for a in cache:
        if cache[a] == total_array_list:
            result.append(a)
    return result


if __name__ == "__main__":
    arrays = []

    arrays.append(list(range(1000000, 2000000)) + [1, 2, 3])
    arrays.append(list(range(2000000, 3000000)) + [1, 2, 3])
    arrays.append(list(range(3000000, 4000000)) + [1, 2, 3])

    print(intersection(arrays))
