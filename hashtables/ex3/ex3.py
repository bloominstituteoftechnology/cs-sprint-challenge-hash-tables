def intersection(arrays):
    """
    YOUR CODE HERE
    """
    # Your code here

    arrays_count = len(arrays) 
    storage = {}
    result= []

    for numbers in arrays:
        for number in numbers:
            if number in storage:
                storage[number] += 1
            else:
                storage[number] = 1
      
    for key in storage:
        if storage[key]==arrays_count:
            result.append(key)
        

    return result


if __name__ == "__main__":
    arrays = []

    arrays.append(list(range(1000000, 2000000)) + [1, 2, 3])
    arrays.append(list(range(2000000, 3000000)) + [1, 2, 3])
    arrays.append(list(range(3000000, 4000000)) + [1, 2, 3])

    print(intersection(arrays))
