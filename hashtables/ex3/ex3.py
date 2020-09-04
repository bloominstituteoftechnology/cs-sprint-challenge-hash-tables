def intersection(arrays):
    """
    YOUR CODE HERE
    """
    # Your code here
    cache = {}
    result = []

    list_len = len(arrays)

    # going through each list in the array
    for num_list in arrays:
        # going through each number in the list
        for number in num_list:
            # checks if number is already in the cache, if not it will initialize number with 1
            if number in cache:
                cache[number] += 1
            else:
                cache[number] = 1
            
            if cache[number] == list_len:
                result.append(number)
    # return result
    return result


if __name__ == "__main__":
    arrays = []

    arrays.append(list(range(1000000, 2000000)) + [1, 2, 3])
    arrays.append(list(range(2000000, 3000000)) + [1, 2, 3])
    arrays.append(list(range(3000000, 4000000)) + [1, 2, 3])

    print(intersection(arrays))
