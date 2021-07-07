def intersection(arrays):
    """
    YOUR CODE HERE
    """
    # Your code here
    
    # empty list
    result = []
    # empty dict
    cache = {}

    # subarray is a single list containing the integers within list
    for subarray in arrays:
        for num in subarray:
            if num not in cache:
                cache[num] = 1 # num = key, with 0 value
            else:
                # append num to the intersection list
                result.append(num)
    result = list(dict.fromkeys(result)) # creates new list, removing any potential duplicates from the list

    return result


if __name__ == "__main__":
    arrays = []

    arrays.append(list(range(1000000, 2000000)) + [1, 2, 3])
    arrays.append(list(range(2000000, 3000000)) + [1, 2, 3])
    arrays.append(list(range(3000000, 4000000)) + [1, 2, 3])

    print(intersection(arrays))
