def intersection(arrays):
    """
    YOUR CODE HERE
    """
    # Your code here
    storage = dict()
    result = []

    for a in arrays:        
        for num in a:
            # storage[num] = 1
            if num in storage:
                storage[num] += 1
            else:
                storage[num] = 1

            for num in storage:                
                result = [num for num in storage if num in storage]

            # for num in storage:
            #     result.append(num)

    return result


if __name__ == "__main__":
    arrays = []

    arrays.append(list(range(1000000, 2000000)) + [1, 2, 3])
    arrays.append(list(range(2000000, 3000000)) + [1, 2, 3])
    arrays.append(list(range(3000000, 4000000)) + [1, 2, 3])

    print(intersection(arrays))

    # for i in arrays:
    #     a = arrays[i]
    #     for value in a:
    #         result = [value for value in a if value in a] 
    # return result 
